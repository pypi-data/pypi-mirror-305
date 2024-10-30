"""Integration tests of the services."""

import os
from pathlib import Path
from typing import Generator

import git
import pytest

from argops.services import (
    load_sops_file,
    promote_environment_specific_files,
    save_sops_file,
)


@pytest.fixture(autouse=True)
def set_current_dir(work_dir: Path) -> Generator[Path, None, None]:
    """Change the working directory for the test."""
    old_cwd = os.getcwd()
    os.chdir(work_dir)

    yield work_dir

    # Reset the current working directory after the test is done
    os.chdir(old_cwd)


class TestPromoteEnvironmentSpecificFiles:
    def test_promote_staging_values_when_production_doesnt_exist(
        self, work_dir: Path
    ) -> None:
        file_name = "values-staging.yaml"
        repo_path = work_dir / "repo"
        os.chdir(repo_path)
        staging_file = repo_path / "staging" / file_name
        staging_file.write_text("foo: bar", encoding="utf8")
        production_file = (
            repo_path / "production" / file_name.replace("staging", "production")
        )
        assert not production_file.exists()
        repo = git.Repo.init(repo_path)
        repo.index.add(["staging"])
        repo.index.commit("Add staging's values file")

        promote_environment_specific_files(
            "values-staging.yaml", "staging", "production", dry_run=False
        )  # act

        result_content = production_file.read_text(encoding="utf8")
        assert "\nfoo: bar  # New key in source\n" in result_content

    def test_promote_staging_secret_when_production_doesnt_exist(
        self, work_dir: Path
    ) -> None:
        file_name = "secrets.yaml"
        repo_path = work_dir / "repo"
        os.chdir(repo_path)
        staging_file = repo_path / "staging" / file_name
        save_sops_file(str(staging_file), "foo: bar")
        production_file = repo_path / "production" / file_name
        assert not production_file.exists()
        repo = git.Repo.init(repo_path)
        repo.index.add(["staging"])
        repo.index.commit("Add staging's secret file")

        promote_environment_specific_files(
            "secrets.yaml", "staging", "production", dry_run=False
        )  # act

        assert production_file.exists(), "the file was not created"
        result_content = load_sops_file(str(production_file))
        # Note: sops doesn't support yaml inline comments well. It adds
        # the comment before the key.
        assert "# New key in source\nfoo: bar" in result_content
