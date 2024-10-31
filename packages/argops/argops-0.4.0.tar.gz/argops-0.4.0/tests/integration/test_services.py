"""Integration tests of the services."""

from pathlib import Path

import git
import pytest

from argops.services import (
    load_sops_file,
    promote_environment_specific_files,
    save_sops_file,
)


@pytest.mark.usefixtures("set_current_dir")
class TestPromoteEnvironmentSpecificFiles:
    def test_promote_staging_values_when_production_doesnt_exist(self) -> None:
        file_name = "values-staging.yaml"
        staging_file = Path("staging") / file_name
        staging_file.write_text("foo: bar-staging", encoding="utf8")
        production_file = Path("production") / file_name.replace(
            "staging", "production"
        )
        assert not production_file.exists()
        repo = git.Repo.init()
        repo.index.add(["staging"])
        repo.index.commit("Add staging's values file")

        promote_environment_specific_files(
            "values-staging.yaml", "staging", "production", dry_run=False
        )  # act

        result_content = production_file.read_text(encoding="utf8")
        assert "\nfoo: bar-production  # New key in source\n" in result_content

    def test_promote_staging_secret_when_production_doesnt_exist(self) -> None:
        file_name = "secrets.yaml"
        staging_file = Path("staging") / file_name
        save_sops_file(str(staging_file), "foo: bar")
        production_file = Path("production") / file_name
        assert not production_file.exists()
        repo = git.Repo.init()
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
