"""Define all the orchestration functionality required by the program to work.

Classes and functions that connect the different domain model objects with the adapters
and handlers to achieve the program's purpose.
"""

import contextlib
import difflib
import filecmp
import logging
import os
import re
import shutil
import subprocess
from io import StringIO
from pathlib import Path
from typing import List, Optional, Tuple, Union

import git
from git.exc import InvalidGitRepositoryError, NoSuchPathError
from ruyaml import YAML
from ruyaml.comments import CommentedMap

from argops.exceptions import GitRepositoryError
from argops.model import YamlDiff

log = logging.getLogger(__name__)


GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"

PathOrStr = Union[Path, str]


def promote_changes(
    src_dir: Optional[Path] = None,
    dest_dir: Optional[Path] = None,
    filters: Optional[List[str]] = None,
    dry_run: bool = False,
) -> None:
    """Promote changes from the source directory to the destination directory.

    Args:
        src_dir (str): The name of the source directory.
        dest_dir (str): The name of the destination directory.
        filters (List[str]): List of filters the applications must match.
        dry_run (bool): If True, perform a dry run showing changes without
            copying files.
    """
    src_dir = src_dir or Path("staging")
    dest_dir = dest_dir or Path("production")
    filters = filters or []

    repository_root, initial_path = find_repository_root_path(src_dir=src_dir)
    os.chdir(repository_root)
    if initial_path == Path("."):
        initial_path = src_dir

    # Ensure the destination directory exists
    if not dest_dir.exists():
        dest_dir.mkdir(parents=True, exist_ok=True)
        log.info(f"Created destination directory: {dest_dir}")

    application_directories = find_application_directories(filters, initial_path)

    # Sync each directory
    for directory in application_directories:
        print_application_name(directory)
        sync_src = directory.resolve().relative_to(repository_root)
        sync_dest = dest_dir / directory.relative_to(src_dir)

        if not sync_dest.exists():
            sync_dest.mkdir(parents=True, exist_ok=True)
            log.info(f"Created destination directory: {sync_dest}")

        comparison = filecmp.dircmp(sync_src, sync_dest)
        sync_directory(
            comparison,
            sync_src,
            sync_dest,
            dry_run,
        )


def find_application_directories(
    filters: List[str], start_dir: Optional[Path] = None
) -> List[Path]:
    """Find directories containing a Chart.yaml file that match the filters.

    The filters can be either environments, application sets or applications.

    Args:
        filters (List[str]): List of filters that the directories need to match.
        start_dir (Path): The path of the directory to start form.

    Returns:
        List[Path]: List of application directory absolute paths to sync.

    Raises:
        ValueError: If no applications are found
    """
    start_dir = start_dir or Path("staging")
    directories = []

    # If cwd is an application directory
    if (start_dir / "Chart.yaml").exists() and (
        len(filters) == 0
        or any(directory in filters for directory in str(start_dir).split("/"))
    ):
        return [start_dir]

    # If cwd is the root, an environment or an application set directory
    for element in start_dir.rglob("**/*"):
        if (
            element.is_dir()
            and (element / "Chart.yaml").exists()
            and (
                len(filters) == 0
                or any(directory in filters for directory in str(element).split("/"))
            )
        ):
            directories.append(element)

    if len(directories) == 0:
        if len(filters) == 0:
            filters = ["None"]
        raise ValueError(
            f"No application was found with the selected filters: {','.join(filters)}"
        )

    return directories


def find_repository_root_path(src_dir: Path) -> Tuple[Path, Path]:
    """Finds the path at the top of the argocd repository.

    Walk upwards the directory tree starting from the current working directory until
    it finds the src_dir directory to promote.

    Args:
        src_dir (str): The name of the source directory to promote.

    Returns:
        str: The full path of the found repository root directory.
        str: The relative path of the found repository root directory.

    Raises:
        FileNotFoundError: If the repository with the given name is not found.
    """
    initial_path = Path.cwd()
    current_path = initial_path

    while current_path != current_path.parent:  # Stop at the filesystem root
        target_path = current_path / src_dir
        if target_path.is_dir():
            log.debug(f"Found '{src_dir}' at {target_path.resolve()}")
            return current_path.resolve(), initial_path.relative_to(current_path)

        current_path = current_path.parent

    raise FileNotFoundError(
        f"No repository named '{src_dir}' found in the directory tree."
    )


def sync_new_file(file_name: str, src_dir: Path, dest_dir: Path, dry_run: bool) -> None:
    """Handle new files and directories.

    By copying them from the source to the destination directory.

    Args:
        file_name (str): The name of the file or directory.
        src_dir (Path): The path to the source directory.
        dest_dir (Path): The path to the destination directory.
        dry_run (bool): If True, only log the changes without performing any
                        operations.
    """
    src_path = src_dir / file_name
    dest_path = dest_dir / file_name.replace("-staging", "-production")

    if file_name in ("values-staging.yaml", "secrets.yaml"):
        promote_environment_specific_files(file_name, src_dir, dest_dir, dry_run)
    else:
        log.info(f"{GREEN}New{RESET}: {src_path} -> {dest_path}")
        if not dry_run:
            if src_path.is_dir():
                shutil.copytree(src_path, dest_path)
            else:
                shutil.copy2(src_path, dest_path)


def sync_deleted_file(file_name: str, dest_dir: Path, dry_run: bool) -> None:
    """Handle files and directories that have been deleted from the source.

    By removing them from the destination directory.

    Args:
        file_name (str): The name of the file or directory.
        dest_dir (str): The path to the destination directory.
        dry_run (bool): If True, only log the changes without performing any
                        operations.
    """
    dest_path = dest_dir / file_name

    if file_name in ["values-production.yaml"]:
        return

    log.info(f"{RED}Deleting{RESET}: {dest_path}")
    if not dry_run:
        if dest_path.is_dir():
            shutil.rmtree(dest_path)
        else:
            os.remove(dest_path)


def sync_updated_file(
    file_name: str, src_dir: Path, dest_dir: Path, dry_run: bool
) -> None:
    """Handle updated files.

    By copying them from the source to the destination directory
    and logging differences.

    Args:
        file_name (str): The name of the file.
        src_dir (str): The path to the source directory.
        dest_dir (str): The path to the destination directory.
        dry_run (bool): If True, only log the changes without performing any
                        operations.
    """
    src_path = src_dir / file_name
    dest_path = dest_dir / file_name

    log.info(f"{YELLOW}Updating file{RESET}: {src_path} -> {dest_path}\n")
    show_file_diff(src_path, dest_path)

    if file_name in ("values-staging.yaml", "secrets.yaml"):
        promote_environment_specific_files(file_name, src_dir, dest_dir, dry_run)
    else:
        if not dry_run:
            shutil.copy2(src_path, dest_path)


# ignore: Missing type parameters for generic type dircmp
# The standard filecmp.dircmp class from Python's standard library
# does not require or support type parameters.
def sync_directory(
    comparison: filecmp.dircmp,  # type: ignore
    src_dir: Path,
    dest_dir: Path,
    dry_run: bool,
) -> None:
    """Synchronize the changes between two directories.

    It performs the following operations:
    - Copy new and updated files from the source directory to the destination
      directory.
    - Delete files and directories that are not in the source directory.

    Args:
        comparison (filecmp.dircmp): The directory comparison object.
        src_dir (Path): The path to the source directory.
        dest_dir (Path): The path to the destination directory.
        dry_run (bool): If True, only log the changes without performing any
                        operations.
    """
    for file_name in comparison.left_only:
        sync_new_file(file_name, src_dir, dest_dir, dry_run)

    for file_name in comparison.right_only:
        sync_deleted_file(file_name, dest_dir, dry_run)

    for file_name in comparison.diff_files:
        sync_updated_file(file_name, src_dir, dest_dir, dry_run)

    for subdir_name in comparison.common_dirs:
        subdir_comparison = comparison.subdirs[subdir_name]
        sync_directory(
            subdir_comparison,
            src_dir / subdir_name,
            dest_dir / subdir_name,
            dry_run,
        )


def promote_environment_specific_files(
    file_name: str, src_dir: PathOrStr, dest_dir: PathOrStr, dry_run: bool = False
) -> None:
    """Promote changes of environment specific files (values and secrets).

    This function compares the YAML contents of the source and destination files.
    If `dry_run` is True, it only shows the diff without making any changes.

    It also substitutes the environment in the content of the files. For
    example if it contains a key `domain: staging.example.com` it will be promoted
    in production as `domain: production.example.com`.

    Args:
        file_name (str): The name of the YAML file (e.g., "values-staging.yaml").
        src_dir (str): The source directory containing the staging file.
        dest_dir (str): The destination directory containing the production file.
        dry_run (bool, optional): If True, only show the diff without making any
            changes. Defaults to False.
    """
    if isinstance(src_dir, str):
        src_dir = Path(src_dir)
    if isinstance(dest_dir, str):
        dest_dir = Path(dest_dir)
    staging_file_path = src_dir / file_name
    production_file_path = dest_dir / file_name.replace(src_dir.name, dest_dir.name)
    log.info(f"Promoting the changes from {staging_file_path}")

    last_promoted_commit = get_last_promoted_commit_id(production_file_path)
    last_commit = get_last_commit_id()
    log.debug(f"Last promoted commit of {staging_file_path} is {last_promoted_commit}")
    log.debug(f"Last commit is {last_commit}")

    # Get the different contents
    if not last_promoted_commit:
        last_promoted_content = ""
    else:
        last_promoted_content = get_content(staging_file_path, last_promoted_commit)

    log.debug(
        f"Creating the updated values of {production_file_path} "
        f"from the latest version of {staging_file_path}"
    )
    old_production_content = get_content(production_file_path)
    new_content = update_values(
        last_promoted_content,
        get_content(staging_file_path).replace(src_dir.name, dest_dir.name),
        old_production_content,
        last_commit,
    )

    if not dry_run:
        set_content(production_file_path, new_content)
        log.debug(f"Promotion completed. Changes applied to {production_file_path}")


def update_values(
    last_promoted_source_content: str,
    source_content: str,
    destination_content: str,
    last_promoted_commit_id: str = "HEAD",
) -> str:
    """Updates the destination YAML content.

    By applying changes from the source content, including new, changed,
    and deleted properties. Updates the last promoted commit ID in the destination
    content.

    Args:
        last_promoted_source_content (str): The previous source YAML content.
        source_content (str): The current source YAML content.
        destination_content (str): The current destination YAML content.
        last_promoted_commit_id (str): The last promoted git commit id.

    Returns:
        str: The updated YAML content with comments.
    """
    log.debug("Comparing source contents.")
    diff = compare_yaml_contents(last_promoted_source_content, source_content)

    if not diff.has_changed:
        log.debug("The source has not changed since the last promoted commit")
        return destination_content

    # Read the current production file
    if destination_content == "":
        log.debug("Destination content is empty, initializing from the source content.")
        new_content = YAML().load(source_content)
        diff.new = diff.new + diff.unchanged + diff.changed
        diff.changed = []
        diff.deleted = []
    else:
        log.debug("Loading existing destination content.")
        new_content = YAML().load(destination_content)

    def apply_diff(
        new_content: CommentedMap, diff: YamlDiff, parent_key: Optional[str] = ""
    ) -> None:
        """Recursively applies differences to the content, handling nested structures.

        Args:
            new_content (Dict[str, Any]): The content to be updated.
            diff (Any): The difference object containing new, changed, and
                deleted items.
            parent_key (Optional[str]): The parent key path for nested structures.
                Defaults to "".
        """
        log.debug(f"Applying differences to parent key: {parent_key}")

        for key, value in diff.new:
            new_content[key] = value
            comment = "New key in source"
            new_content.yaml_add_eol_comment(
                key=key,
                comment=comment,
            )
            log.debug(
                f"Added new key '{key}' with value '{value}' at path '{parent_key}'"
            )

        for key, value in diff.changed:
            if isinstance(value, dict):
                log.debug(f"Recursively applying changes to nested key: {key}")
                string_stream = StringIO()
                YAML().dump(new_content[key], string_stream)
                source_yaml = string_stream.getvalue()
                string_stream.close()
                string_stream = StringIO()
                YAML().dump(value, string_stream)
                destination_yaml = string_stream.getvalue()
                string_stream.close()

                apply_diff(
                    new_content[key],
                    compare_yaml_contents(
                        source_yaml,
                        destination_yaml,
                    ),
                    key,
                )
            else:
                comment = f"Key changed in source to {value}"
                new_content.yaml_add_eol_comment(key=key, comment=comment)
                log.info(f"Updated key '{key}' to '{value}' at path '{parent_key}'")

        for key in diff.deleted:
            if key in new_content:
                comment = "Key deleted in source"
                new_content.yaml_add_eol_comment(key=key, comment=comment)
                log.info(f"Marked key '{key}' as deleted at path '{parent_key}'")

    apply_diff(new_content, diff)

    log.debug("Updating the last promoted commit ID.")
    new_content.yaml_set_start_comment(
        f"Last promoted commit id: {last_promoted_commit_id}"
    )

    log.debug("Finished updating values.")

    string_stream = StringIO()
    YAML().dump(new_content, string_stream)
    new_content_text = string_stream.getvalue()
    string_stream.close()

    show_diff(new_content_text, destination_content)

    return new_content_text


def get_last_commit_id(repo_path: str = ".") -> str:
    """Get the last commit ID of the Git repository at the specified path.

    Args:
        repo_path (str): The path to the Git repository.
            Defaults to the current directory.

    Returns:
        str: The last commit ID.

    Raises:
        GitRepositoryError: If there is an issue accessing the repository
            or retrieving the commit ID.
    """
    try:
        repo = git.Repo(repo_path)
        last_commit = repo.head.commit
        return last_commit.hexsha
    except InvalidGitRepositoryError as e:
        raise GitRepositoryError(f"Invalid Git repository at path: {repo_path}") from e
    except NoSuchPathError as e:
        raise GitRepositoryError(f"Path does not exist: {repo_path}") from e
    except Exception as e:
        raise GitRepositoryError(f"Error retrieving last commit ID: {e}") from e


def get_last_promoted_commit_id(file_path: PathOrStr) -> Optional[str]:
    """Extract the last promoted commit ID from a values-staging.yaml file.

    Args:
        file_path (str): The path to the values-staging.yaml file.

    Returns:
        str: The last promoted commit ID or None if the line doesn't exist.
    """
    commit_id_pattern = re.compile(r"# Last promoted commit id: (\w+)")

    with contextlib.suppress(FileNotFoundError), open(
        file_path, "r", encoding="utf8"
    ) as file:
        for line in file:
            match = commit_id_pattern.match(line)
            if match:
                return match.group(1)

    return None


def get_content(
    file_path: PathOrStr, commit_id: str = "HEAD", repo_path: str = "."
) -> str:
    """Get YAML content of the file at a specific commit.

    If the file name matches ".*secrets.*", it will decrypt the content
    using `load_sops_file`.

    Args:
        file_path (str): The path to the file within the repository.
        commit_id (str): The commit ID to retrieve the file from. Defaults to "HEAD".
        repo_path (str): The path to the repository. Defaults to the current directory.

    Returns:
        str: The content of the file at the specified commit, or an empty string if
        the file doesn't exist.
    """
    if isinstance(file_path, Path):
        file_path = str(file_path)
    try:
        repo = git.Repo(repo_path)
        commit = repo.commit(commit_id)
        blob = commit.tree / file_path
        commit_content = blob.data_stream.read().decode("utf-8")
    except KeyError as e:
        log.warning(f"The '{file_path}' at commit '{commit_id}' doesn't exist: {e}")
        return ""

    except Exception as e:  # noqa: W0718
        # W0718: Catching too general exception Exception. But it's what we want
        log.error(
            f"Error retrieving content for '{file_path}' at commit '{commit_id}': {e}"
        )
        return ""

    if re.search(r".*secrets.*", file_path, re.IGNORECASE):
        log.info(f"File '{file_path}' matches secrets pattern, decrypting with sops.")
        temp_file = Path(f"{repo_path}/argops-temporal-secret.yaml")
        temp_file.write_text(commit_content, encoding="utf8")
        try:
            content = load_sops_file(str(temp_file))
        except RuntimeError as e:
            log.warning(f"The '{file_path}' at commit '{commit_id}' doesn't exist: {e}")
            content = ""
        temp_file.unlink()  # Clean up the temporary file
    else:
        content = commit_content

    return content


def set_content(file_path: PathOrStr, content: str) -> None:
    """Set YAML content of the file.

    If the file name matches ".*secrets.*", it will encrypt the content
    using `save_sops_file`. Otherwise, it will write the content directly to the file.

    Args:
        file_path (str): The path to the file on the filesystem.
        content (str): The new content to be written into the file.
    """
    if isinstance(file_path, Path):
        file_path = str(file_path)
    log.info(f"Writing content to '{file_path}'")
    if re.search(r".*secrets.*", file_path, re.IGNORECASE):
        log.info(f"File '{file_path}' matches secrets pattern, encrypting with sops.")
        save_sops_file(file_path, content)
    else:
        Path(file_path).write_text(content, encoding="utf-8")


def compare_yaml_contents(yaml_content_1: str, yaml_content_2: str) -> YamlDiff:
    """Compare the YAML contents from two plain text YAML strings.

    Args:
        yaml_content_1 (str): The plain text content of the first YAML.
        yaml_content_2 (str): The plain text content of the second YAML.

    Returns:
        YamlDiff: The differences between the two YAML contents.
    """
    content_1 = YAML().load(yaml_content_1)
    content_2 = YAML().load(yaml_content_2)

    # Initialize the YamlDiff object
    diff = YamlDiff()

    if not content_1:
        diff.new = [(key, content_2[key]) for key in content_2.keys()]
    elif not content_2:
        diff.deleted = content_1.keys()
    else:
        # Compare the contents
        all_keys = set(content_1.keys()).union(set(content_2.keys()))
        for key in all_keys:
            if key not in content_1:
                diff.new.append((key, content_2[key]))
            elif key not in content_2:
                diff.deleted.append(key)
            else:
                if content_1[key] != content_2[key]:
                    diff.changed.append((key, content_2[key]))
                else:
                    # E1101: Instance of FiledInfo has no append member, but it does
                    # https://github.com/pylint-dev/pylint/issues/4899
                    diff.unchanged.append((key, content_1[key]))  # noqa: E1101

    return diff


def show_diff(src: str, dest: str) -> None:
    """Show the differences between two strings.

    Args:
        src (str): The source text.
        dest (str): The destination text.
    """
    diff = difflib.unified_diff(dest.splitlines(), src.splitlines())
    for line in diff:
        printeable_line = line.rstrip("\n")
        if line.startswith("+++"):
            printeable_line = "+++ New"
        elif line.startswith("---"):
            printeable_line = "--- Old"
        if line.startswith("+"):
            log.info(f"{GREEN}{printeable_line}{RESET}")
        elif line.startswith("-"):
            log.info(f"{RED}{printeable_line}{RESET}")
        else:
            log.info(printeable_line)


def show_file_diff(src_file: Path, dest_file: Path) -> None:
    """Show the differences between two files.

    Args:
        src_file (Path): The path to the first file.
        dest_file (Path): The path to the second file.
    """
    show_diff(
        src_file.read_text(encoding="utf8"),
        dest_file.read_text(encoding="utf8"),
    )


def load_sops_file(file_path: str) -> str:
    """Decrypt and load content from a sops-encrypted file.

    Args:
        file_path (str): The path to the sops-encrypted file.

    Returns:
        str: The decrypted content of the file as a string.

    Raises:
        RuntimeError: If decryption fails due to a subprocess error.
    """
    try:
        log.debug(f"Decrypting file: {file_path}")
        result = subprocess.run(
            ["sops", "--decrypt", file_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        log.debug(f"File {file_path} decrypted successfully")
        return result.stdout.decode("utf-8")
    except subprocess.CalledProcessError as e:
        error_message = e.stderr.decode().strip()
        log.error(f"Error decrypting the file: {error_message}")
        raise RuntimeError(
            f"Failed to decrypt file {file_path}: {error_message}"
        ) from e


def save_sops_file(file_path: str, content: str) -> None:
    """Encrypt and save content to a file using sops.

    The function saves the content to a decrypted file with '{file_path}-decrypted',
    encrypts it with `sops`, and then renames it to the desired encrypted filename.

    Args:
        file_path (str): The path where the encrypted file will be saved, including
            the '.yaml' extension.
        content (str): The content to be encrypted and saved.

    Example:
        content = 'secret_key: super_secret_value'
        save_sops_file('secrets.yaml', content)
    """
    log.debug(f"Encrypting and saving content to {file_path}")

    # Remove the '.yaml' extension from file_path for decrypted_file_path
    decrypted_file_path = (
        Path(file_path).parent / f"{Path(file_path).stem}-decrypted.yaml"
    )
    decrypted_file_path.write_text(content)
    log.debug(f"Decrypted content saved at {decrypted_file_path}")

    # Get the current working directory
    if decrypted_file_path.parent.is_absolute():
        cwd = decrypted_file_path.parent
    else:
        cwd = decrypted_file_path.cwd()

    try:
        # Encrypt the decrypted file using sops
        subprocess.run(
            ["sops", "--encrypt", "--in-place", str(decrypted_file_path)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=cwd,
        )
        log.debug("File successfully encrypted with sops")

        # Rename the decrypted file to have the '.yaml'
        # extension and match the desired filename
        decrypted_file_path.rename(file_path)
        log.debug(f"Encrypted file saved as {file_path}")
    except subprocess.CalledProcessError as e:
        log.error(f"Error encrypting the file: {e.stderr.decode().strip()}")
        raise
    except Exception as e:
        log.error(f"Unexpected error: {str(e)}")
        raise


def print_application_name(application_path: Path) -> None:
    """Print application name from given path.

    Args:
        application_path (Path): The application directory.

    Example:
        >>> print_application_name(Path("/path/to/app"))
        ###########
        ##  app  ##
        ###########
    """
    name = application_path.name
    box_size = len(name) + 8
    log.info(
        f"\n\n{'#' * box_size}\n" f"##  {name.title()}  ##\n" f"{'#' * box_size}\n"
    )
