"""
PDF Margin Adder Command Line Interface

This script provides a command-line interface (CLI) for adding margins to PDF files
using the `add_margins` function from the `pdfmargins` module. Users can specify margins
in points or as relative values, and the script can process both individual PDF files
and directories containing PDF files.

Dependencies:
- Click: A package for creating command-line interfaces.
- TQDM: A library for creating progress bars.
- pathlib: A module to handle filesystem paths.

Usage:
    To use this CLI, run the script with the desired options. For example:
    python cli.py input.pdf --left 10 --right 10
"""

import click
from pathlib import Path
from tqdm import tqdm
from pdfmargins.add_margins import add_margins


@click.command()
@click.argument(
    "input_file_or_dir",
    type=click.Path(exists=True, dir_okay=True, file_okay=True, path_type=Path),
)
@click.option(
    "--left",
    type=float,
    default=0,
    help="Left margin in points or relative (default: 150)",
)
@click.option(
    "--right",
    type=float,
    default=0.2,
    help="Right margin in points or relative (default: 150)",
)
@click.option(
    "--top", type=float, default=0, help="Top margin in points or relative (default: 0)"
)
@click.option(
    "--bottom",
    type=float,
    default=0.3,
    help="Bottom margin in points or relative (default: 0)",
)
@click.option("--force", is_flag=True, help="overwrite existing files, else skip.")
@click.option(
    "--force-relative",
    is_flag=True,
    help="Force to interpret margins as relative margins",
)
def cli(
    input_file_or_dir: Path,
    left: float,
    right: float,
    top: float,
    bottom: float,
    force: bool = False,
    force_relative: bool = False,
):
    """
    Command-line interface function to add margins to PDF files.

    Args:
        input_file_or_dir (Path): The input PDF file or directory containing PDF files.
        left (float): The left margin to add (absolute or relative).
        right (float): The right margin to add (absolute or relative).
        top (float): The top margin to add (absolute or relative).
        bottom (float): The bottom margin to add (absolute or relative).
        force (bool, optional): If true, overwrite existing files, else skip
        force_relative (bool, optional): If True, interpret all margins as relative values.
    """

    # Check if the input is a file or a directory
    file = input_file_or_dir

    # If it's a file, apply margins and create a new PDF with added margins
    if input_file_or_dir.is_file():
        target = file.with_name(f"{file.stem}.margins{file.suffix}")
        if not (target.exists() and not force):
            add_margins(
                file,
                target,
                left=left,
                right=right,
                top=top,
                bottom=bottom,
                force_relative=force_relative,
            )

    # If it's a directory, process all PDF files within it
    else:
        # Collect all PDF files in the directory, excluding already processed files
        files = [
            f
            for f in input_file_or_dir.rglob("*.pdf")
            if not f.name.endswith(".margins.pdf")
        ]

        # Progress bar to track processing of multiple files
        for file in tqdm(files):
            target = file.with_name(f"{file.stem}.margins{file.suffix}")
            if target.exists() and not force:
                continue  # skip
            add_margins(
                file,
                target,
                left=left,
                right=right,
                top=top,
                bottom=bottom,
                force_relative=force_relative,
            )


# Entry point to the script
if __name__ == "__main__":
    cli()  # Invoke the CLI command
