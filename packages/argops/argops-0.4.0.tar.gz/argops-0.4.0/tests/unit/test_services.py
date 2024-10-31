"""Test the services."""

import logging
import os
import re
import shutil
from pathlib import Path
from textwrap import dedent

import git
import pytest
from _pytest.logging import LogCaptureFixture

from argops.exceptions import GitRepositoryError
from argops.services import (
    GREEN,
    RED,
    RESET,
    compare_yaml_contents,
    find_application_directories,
    get_content,
    get_last_commit_id,
    load_sops_file,
    promote_changes,
    save_sops_file,
    set_content,
    show_diff,
    update_values,
)


@pytest.fixture(name="repo")
def repo_(work_dir: Path) -> Path:
    """Create a temporary Git repository with some test files."""
    # Create a temporary directory for the repo
    repo_path = work_dir / "repo"
    repo = git.Repo.init(repo_path)

    # Create a new file in the repo
    file_path = repo_path / "test.yaml"
    with open(file_path, "w", encoding="utf8") as f:
        f.write("key: value\n")

    # Create a secrets file in the repo
    shutil.copyfile("tests/assets/sops/encrypted.yaml", repo_path / "secrets.yaml")

    # Stage and commit the file
    repo.index.add(["*.yaml"])
    repo.index.commit("Initial commit")

    return repo_path


class TestGetContent:

    def test_get_content(self, repo: Path) -> None:
        result = get_content("test.yaml", repo_path=str(repo))

        assert result == "key: value\n"

    def test_get_content_non_existent_file(
        self, repo: Path, caplog: LogCaptureFixture
    ) -> None:
        """Test getting content of a non-existent file."""
        result = get_content("non_existent_file.yaml", repo_path=str(repo))

        assert result == ""
        assert (
            "The 'non_existent_file.yaml' at commit 'HEAD' doesn't exist: "
            in caplog.text
        )

    def test_get_secret(self, repo: Path) -> None:
        result = get_content("secrets.yaml", repo_path=str(repo))

        assert "foo: bar" in result
        assert not (repo / "argops-temporal-secret.yaml").exists()

    def test_get_non_existent_secret(
        self, repo: Path, caplog: LogCaptureFixture
    ) -> None:
        """Test getting content of a non-existent file."""
        result = get_content("non_existent_secrets.yaml", repo_path=str(repo))

        assert result == ""
        assert (
            "The 'non_existent_secrets.yaml' at commit 'HEAD' doesn't exist: "
            in caplog.text
        )


class TestSetContent:

    def test_set_secrets(self, repo: Path) -> None:
        file_path = repo / "secrets.yaml"

        set_content(str(file_path), content="foo: bar")  # act

        assert "sops" in file_path.read_text(encoding="utf8")
        assert "foo: bar" in load_sops_file(str(file_path))


class TestSaveSops:
    def test_save_sops_when_file_doesnt_exist(self, repo: Path) -> None:
        file_path = repo / "new-secrets.yaml"

        save_sops_file(str(file_path), "foo: bar")  # act

        assert "foo: bar" in load_sops_file(str(file_path))


class TestCompareYamlContents:

    def test_new_property(self) -> None:
        yaml_content_1 = """
        key1: value1
        """
        yaml_content_2 = """
        key1: value1
        key2: value2
        """

        result = compare_yaml_contents(yaml_content_1, yaml_content_2)

        assert result.new == [("key2", "value2")]
        assert not result.changed
        assert not result.deleted
        assert result.unchanged == [("key1", "value1")]

    def test_new_property_from_empty(self) -> None:
        yaml_content_1 = ""
        yaml_content_2 = """
        key1: value1
        key2: value2
        """

        result = compare_yaml_contents(yaml_content_1, yaml_content_2)

        assert ("key1", "value1") in result.new
        assert ("key2", "value2") in result.new

    def test_changed_property(self) -> None:
        yaml_content_1 = """
        key1: value1
        key2: value2
        """
        yaml_content_2 = """
        key1: value1
        key2: new_value2
        """

        result = compare_yaml_contents(yaml_content_1, yaml_content_2)

        assert result.new == []
        assert result.changed == [("key2", "new_value2")]
        assert result.deleted == []
        assert result.unchanged == [("key1", "value1")]

    def test_deleted_property(self) -> None:
        yaml_content_1 = """
        key1: value1
        key2: value2
        """
        yaml_content_2 = """
        key1: value1
        """

        result = compare_yaml_contents(yaml_content_1, yaml_content_2)

        assert not result.new
        assert not result.changed
        assert result.deleted == ["key2"]
        assert result.unchanged == [("key1", "value1")]

    def test_deleted_all_properties(self) -> None:
        yaml_content_1 = """
        key1: value1
        key2: value2
        """
        yaml_content_2 = ""

        result = compare_yaml_contents(yaml_content_1, yaml_content_2)

        assert "key1" in result.deleted
        assert "key2" in result.deleted

    def test_multiple_changes(self) -> None:
        yaml_content_1 = """
        key1: value1
        key2: value2
        key3: value3
        """
        yaml_content_2 = """
        key1: new_value1
        key3: value3
        key4: value4
        """

        result = compare_yaml_contents(yaml_content_1, yaml_content_2)

        assert result.new == [("key4", "value4")]
        assert result.changed == [("key1", "new_value1")]
        assert result.deleted == ["key2"]
        assert result.unchanged == [("key3", "value3")]

    def test_no_changes(self) -> None:
        yaml_content_1 = """
        key1: value1
        key2: value2
        """
        yaml_content_2 = """
        key1: value1
        key2: value2
        """

        result = compare_yaml_contents(yaml_content_1, yaml_content_2)

        assert not result.new
        assert not result.changed
        assert not result.deleted
        # E1135: result.unchanged doesn't support membership test, but it does
        assert ("key1", "value1") in result.unchanged  # noqa: E1135
        assert ("key2", "value2") in result.unchanged  # noqa: E1135


class TestGetLastCommitId:

    def test_get_last_commit_id_valid_repo(self, repo: Path) -> None:
        result = get_last_commit_id(str(repo))

        assert isinstance(result, str)
        assert len(result) == 40  # A valid Git commit SHA-1 hash is 40 characters long

    def test_get_last_commit_id_invalid_repo(self) -> None:
        invalid_repo_path = "/invalid/path/to/repo"

        with pytest.raises(GitRepositoryError) as exc_info:
            get_last_commit_id(invalid_repo_path)

        assert str(exc_info.value) == f"Path does not exist: {invalid_repo_path}"

    def test_get_last_commit_id_not_a_repo(self, tmp_path: Path) -> None:
        non_repo_path = tmp_path / "not_a_repo"
        non_repo_path.mkdir()

        with pytest.raises(GitRepositoryError) as exc_info:
            get_last_commit_id(str(non_repo_path))

        assert str(exc_info.value) == f"Invalid Git repository at path: {non_repo_path}"


class TestUpdateValues:

    def test_update_values_with_empty_destination(self) -> None:
        last_promoted_source_content = dedent(
            """
        key1: value1
        key2: value2
        """
        )
        source_content = dedent(
            """
        key1: value1
        key2: updated_value2
        key3: value3
        """
        )
        destination_content = ""
        last_promoted_commit_id = "123abc"

        result = update_values(
            last_promoted_source_content,
            source_content,
            destination_content,
            last_promoted_commit_id,
        )

        expected_yaml = dedent(
            """\
        # Last promoted commit id: 123abc
        key1: value1  # New key in source
        key2: updated_value2 # New key in source
        key3: value3  # New key in source
        """
        )
        assert result.strip() == expected_yaml.strip()

    def test_update_values_with_empty_destination_and_unpromoted_source(self) -> None:
        last_promoted_source_content = ""
        source_content = dedent(
            """
        key1: value1
        key2: updated_value2
        key3: value3
        """
        )
        destination_content = ""
        last_promoted_commit_id = "123abc"

        result = update_values(
            last_promoted_source_content,
            source_content,
            destination_content,
            last_promoted_commit_id,
        )

        expected_yaml = dedent(
            """\
        # Last promoted commit id: 123abc
        key1: value1  # New key in source
        key2: updated_value2 # New key in source
        key3: value3 # New key in source
        """
        )
        assert result.strip() == expected_yaml.strip()

    def test_update_values_with_existing_destination(self) -> None:
        last_promoted_source_content = dedent(
            """
        key1: value1
        key2: value2
        """
        )
        source_content = dedent(
            """
        key1: value1
        key2: updated_value2
        key3: value3
        """
        )
        destination_content = dedent(
            """
        key1: value1
        key2: value2
        """
        )
        last_promoted_commit_id = "456def"

        result = update_values(
            last_promoted_source_content,
            source_content,
            destination_content,
            last_promoted_commit_id,
        )

        expected_yaml = dedent(
            """\
        # Last promoted commit id: 456def
        key1: value1
        key2: value2 # Key changed in source to updated_value2
        key3: value3  # New key in source
        """
        )
        assert result.strip() == expected_yaml.strip()

    def test_update_values_with_removed_content_in_source(self) -> None:
        last_promoted_source_content = dedent(
            """
        key1: value1
        key2: value2
        """
        )
        source_content = dedent(
            """
        key1: value1
        """
        )
        destination_content = dedent(
            """
        key1: value1
        key2: value2
        """
        )
        last_promoted_commit_id = "456def"

        result = update_values(
            last_promoted_source_content,
            source_content,
            destination_content,
            last_promoted_commit_id,
        )

        expected_yaml = dedent(
            """\
        # Last promoted commit id: 456def
        key1: value1
        key2: value2  # Key deleted in source
        """
        )
        assert result.strip() == expected_yaml.strip()

    def test_update_values_no_changes(self) -> None:
        last_promoted_source_content = dedent(
            """
        key1: value1
        key2: value2
        """
        )
        source_content = dedent(
            """
        key1: value1
        key2: value2
        """
        )
        destination_content = dedent(
            """
        # Last promoted commit id: 789ghi
        key1: value1
        key2: value2
        """
        )
        last_promoted_commit_id = "789ghi"

        result = update_values(
            last_promoted_source_content,
            source_content,
            destination_content,
            last_promoted_commit_id,
        )

        expected_yaml = dedent(
            """\
        # Last promoted commit id: 789ghi
        key1: value1
        key2: value2
        """
        )
        assert result.strip() == expected_yaml.strip()

    def test_update_values_no_changes_on_last_commit(self) -> None:
        """
        We don't want to change the last_promoted_commit_id if the file has not
        changed since then. Otherwise each time we do a promote all the values files
        of the repository will have a line change, which will twarten the pull request
        reviews.
        """
        last_promoted_source_content = dedent(
            """
        key1: value1
        key2: value2
        """
        )
        source_content = dedent(
            """
        key1: value1
        key2: value2
        """
        )
        destination_content = dedent(
            """
            # Last promoted commit id: a_previous_commit
        key1: value1
        key2: value2
        """
        )
        last_promoted_commit_id = "789ghi"

        result = update_values(
            last_promoted_source_content,
            source_content,
            destination_content,
            last_promoted_commit_id,
        )

        expected_yaml = dedent(
            """\
        # Last promoted commit id: a_previous_commit
        key1: value1
        key2: value2
        """
        )
        assert result.strip() == expected_yaml.strip()

    def test_update_values_with_nested_values(self) -> None:
        last_promoted_source_content = dedent(
            """
        parent:
          child1: value1
          child2: value2
        """
        )
        source_content = dedent(
            """
        parent:
          child1: value1
          child2: updated_value2
          child3: value3
        """
        )
        destination_content = dedent(
            """
        parent:
          child1: value1
          child2: value2
        """
        )
        last_promoted_commit_id = "789xyz"

        result = update_values(
            last_promoted_source_content,
            source_content,
            destination_content,
            last_promoted_commit_id,
        )

        assert re.search(
            r"child2: value2\s+# Key changed in source to updated_value2", result
        )
        assert re.search(r"child3: value3\s+# New key in source", result)

    def test_update_values_with_nested_deletions(self) -> None:
        last_promoted_source_content = dedent(
            """
        parent:
          child1: value1
          child2: value2
          child3: value3
        """
        )
        source_content = dedent(
            """
        parent:
          child1: value1
        """
        )
        destination_content = dedent(
            """
        parent:
          child1: value1
          child2: value2
          child3: value3
        """
        )
        last_promoted_commit_id = "abc456"

        result = update_values(
            last_promoted_source_content,
            source_content,
            destination_content,
            last_promoted_commit_id,
        )

        assert re.search(r"child2: value2\s+# Key deleted in source", result)
        assert re.search(r"child3: value3\s+# Key deleted in source", result)


class TestShowDiff:
    def test_no_difference(self, caplog: LogCaptureFixture) -> None:
        src = "Hello\nWorld\n"
        dest = "Hello\nWorld\n"

        show_diff(src, dest)  # act

        assert len(caplog.records) == 0

    def test_added_line(self, caplog: LogCaptureFixture) -> None:
        caplog.set_level(logging.DEBUG)
        src = "Hello\nWorld\nNew line"
        dest = "Hello\nWorld"

        show_diff(src, dest)  # act

        assert (
            "argops.services",
            logging.INFO,
            f"{GREEN}+New line{RESET}",
        ) in caplog.record_tuples

    def test_removed_line(self, caplog: LogCaptureFixture) -> None:
        caplog.set_level(logging.DEBUG)
        src = "Hello\nWorld"
        dest = "Hello\nWorld\nRemoved line"

        show_diff(src, dest)  # act

        assert (
            "argops.services",
            logging.INFO,
            f"{RED}-Removed line{RESET}",
        ) in caplog.record_tuples


@pytest.mark.usefixtures("set_current_dir")
class TestFindApplicationDirectories:
    def test_no_filters_returns_all_applications(self) -> None:
        result = find_application_directories(filters=[])

        assert len(result) == 3

    def test_single_filter_valid_result(self) -> None:
        result = find_application_directories(filters=["application-1"])

        assert len(result) == 1
        assert result[0] == Path("staging/application-set-1/application-1")

    def test_multiple_filters_valid_result(self) -> None:
        result = find_application_directories(
            filters=["application-1", "application-3"]
        )

        assert len(result) == 2
        assert Path("staging/application-set-1/application-1") in result
        assert Path("staging/application-3") in result

    def test_no_applications_found_raises_value_error(self) -> None:
        with pytest.raises(
            ValueError,
            match="No application was found with the selected filters: non-existent",
        ):
            find_application_directories(filters=["non-existent"])

    def test_application_set_filter(self) -> None:
        result = find_application_directories(filters=["application-set-1"])

        assert len(result) == 2
        assert Path("staging/application-set-1/application-1") in result
        assert Path("staging/application-set-1/application-2") in result

    def test_no_filters_returns_all_applications_under_application_set_cwd(
        self,
    ) -> None:
        result = find_application_directories(
            filters=[], start_dir=Path("staging/application-set-1")
        )

        assert len(result) == 2
        assert Path("staging/application-set-1/application-1") in result
        assert Path("staging/application-set-1/application-2") in result

    def test_no_filters_returns_all_applications_under_application_cwd(self) -> None:
        result = find_application_directories(
            filters=[], start_dir=Path("staging/application-3")
        )

        assert len(result) == 1
        assert Path("staging/application-3") in result


@pytest.mark.usefixtures("set_current_dir")
class TestPromoteChanges:
    def test_promote_changes_when_cwd_is_application_dir(self, work_dir: Path) -> None:
        production_path = Path("production/application-3")
        os.chdir("staging/application-3")
        assert not production_path.exists()

        promote_changes()  # act

        assert production_path.exists()
        assert not (work_dir / "production" / "application-set-1").exists()

    def test_promote_changes_when_cwd_is_application_set_dir(
        self, work_dir: Path
    ) -> None:
        production_paths = [
            Path("production/application-set-1/application-1"),
            Path("production/application-set-1/application-2"),
        ]
        os.chdir("staging/application-set-1")
        assert not production_paths[0].exists()
        assert not production_paths[1].exists()

        promote_changes()  # act

        assert production_paths[0].exists()
        assert production_paths[1].exists()
        assert not (work_dir / "production" / "application-3").exists()

    def test_promote_changes_when_cwd_is_application_set_dir_and_has_filter(
        self, work_dir: Path
    ) -> None:
        production_paths = [
            Path("production/application-set-1/application-1"),
            Path("production/application-set-1/application-2"),
        ]
        os.chdir("staging/application-set-1")
        assert not production_paths[0].exists()
        assert not production_paths[1].exists()

        promote_changes(filters=["application-1"])  # act

        assert production_paths[0].exists()
        assert not production_paths[1].exists()
        assert not (work_dir / "production" / "application-3").exists()

    def test_promote_changes_when_cwd_is_environment_dir(self) -> None:
        production_paths = [
            Path("production/application-set-1/application-1"),
            Path("production/application-set-1/application-2"),
            Path("production/application-3"),
        ]
        os.chdir("staging")
        assert not production_paths[0].exists()
        assert not production_paths[1].exists()
        assert not production_paths[2].exists()

        promote_changes()  # act

        assert production_paths[0].exists()
        assert production_paths[1].exists()
        assert production_paths[2].exists()

    def test_promote_changes_when_cwd_is_root_dir(self) -> None:
        production_paths = [
            Path("production/application-set-1/application-1"),
            Path("production/application-set-1/application-2"),
            Path("production/application-3"),
        ]
        assert not production_paths[0].exists()
        assert not production_paths[1].exists()
        assert not production_paths[2].exists()

        promote_changes()  # act

        assert production_paths[0].exists()
        assert production_paths[1].exists()
        assert production_paths[2].exists()
