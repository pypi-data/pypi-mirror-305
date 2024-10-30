# SPDX-FileCopyrightText: 2024-present Paul Reinerfelt <Paul.Reinerfelt@gmail.com>
#
# SPDX-License-Identifier: MIT
import logging
import pathlib
from datetime import datetime

import click
import click_logging  # type: ignore
from zoneinfo import ZoneInfo

from abnf_to_plantuml.__about__ import __version__
from abnf_to_plantuml.processing import process

logger = logging.getLogger("abnf_to_plantuml")
click_logging.basic_config(logger)


@click.command(
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click_logging.simple_verbosity_option(logger)
@click.argument(
    "input_",
    type=click.Path(
        exists=True, dir_okay=False, allow_dash=True, path_type=pathlib.Path
    ),
)
@click.option(
    "-o",
    "--output",
    type=click.Path(
        exists=False,
        writable=True,
        dir_okay=False,
        allow_dash=True,
        path_type=pathlib.Path,
    ),
    default="-",
    help="path to the file where the produced EBNF is stored. If not specified, stdout is used.",
)
@click.option(
    "--include-core-rules",
    is_flag=True,
    help="Include the definitions of the RFC 5234 core rules that have been referenced",
)
@click.version_option(version=__version__, prog_name="abnf_to_plantuml")
def abnf_to_plantuml(
    input_: pathlib.Path, output: pathlib.Path, include_core_rules: bool
) -> int:
    """
    Read a file containing an ABNF-grammar and write to another file,
    or to `stdout`, the conversion of said grammar into a PlantUML
    `@startebnf`/`@endebnf` section.
    """
    myzone = ZoneInfo("Europe/Stockholm")
    now = datetime.now(myzone)
    today = now.date()
    current_time = now.time()
    click.echo(
        f"This is abnf-to-plantuml, Version {__version__} {today.isoformat()} {current_time.isoformat('seconds')}"
    )
    logger.debug(f"Include core rules: {include_core_rules}")
    return process(input_, output, include_core_rules)
