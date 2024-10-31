"""Define the command line interface."""

import logging
import traceback
from pathlib import Path
from typing import List, Optional

import typer

from .. import services
from . import utils

log = logging.getLogger(__name__)
cli = typer.Typer()


@cli.command()
def main(
    version: Optional[bool] = typer.Option(  # noqa: W0613, M511, B008
        None, "--version", callback=utils.version_callback, is_eager=True
    ),
    src_dir: Path = typer.Option(
        "staging", "--src-dir", "-s", help="Name of the source directory"
    ),
    dest_dir: Path = typer.Option(
        "production",
        "--dest-dir",
        "-d",
        help="Name of the destination directory",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help=(
            "Perform a dry run, showing the differences without changing the "
            "files or directories"
        ),
    ),
    filters: List[str] = typer.Argument(
        None, help="List of environment, application or application sets to promote"
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Promote argo applications between environments.

    If no filters are specified it will promote all applications under the current
    directory.
    """
    filters = filters or []
    utils.load_logger(verbose)
    try:
        services.promote_changes(src_dir, dest_dir, filters, dry_run)
    except Exception as error:
        if verbose:
            raise error
        log.error(traceback.format_exception(None, error, error.__traceback__)[-1])
        raise typer.Exit(code=1)


if __name__ == "__main__":
    cli()
