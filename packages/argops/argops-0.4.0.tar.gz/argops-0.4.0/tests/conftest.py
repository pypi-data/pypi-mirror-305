"""Store the classes and fixtures used throughout the tests."""

import os
import shutil
from pathlib import Path
from typing import Generator

import pytest


@pytest.fixture(name="work_dir")
def work_dir_(tmp_path: Path) -> Path:
    """Create the work directory for the tests."""
    shutil.copytree("tests/assets/gpg", tmp_path / "gpg")
    shutil.copytree("tests/assets/repo", tmp_path / "repo")
    os.environ["GNUPGHOME"] = str(tmp_path / "gpg")

    return tmp_path


@pytest.fixture
def set_current_dir(work_dir: Path) -> Generator[Path, None, None]:
    """Change the working directory for the test."""
    old_cwd = os.getcwd()
    os.chdir(work_dir / "repo")

    yield work_dir

    # Reset the current working directory after the test is done
    os.chdir(old_cwd)
