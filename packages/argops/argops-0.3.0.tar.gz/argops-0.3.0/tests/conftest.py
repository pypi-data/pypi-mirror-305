"""Store the classes and fixtures used throughout the tests."""

import os
import shutil
from pathlib import Path

import pytest


@pytest.fixture(name="work_dir")
def work_dir_(tmp_path: Path) -> Path:
    """Create the work directory for the tests."""
    shutil.copytree("tests/assets/gpg", tmp_path / "gpg")
    shutil.copytree("tests/assets/repo", tmp_path / "repo")
    os.environ["GNUPGHOME"] = str(tmp_path / "gpg")

    return tmp_path
