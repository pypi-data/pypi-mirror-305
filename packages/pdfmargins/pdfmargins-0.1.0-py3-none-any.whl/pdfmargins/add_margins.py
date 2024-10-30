"""
PDF Margin Adder Tool

This script provides a function to add margins to PDF pages. Users can specify
absolute or relative margin values for each side of the page. The tool reads an
input PDF file, applies the specified margins, and writes the output to a new PDF file.

Dependencies:
- PyPDF2: A library for manipulating PDF files.
- tqdm: A library for creating progress bars.

Usage:
    To use this tool, call the `add_margins` function with the desired parameters.
"""

from pypdf import PdfReader, PdfWriter, Transformation, PageObject
from tqdm import tqdm
from pathlib import Path
import math


def add_margins(
    input_path: str | Path,
    output_path: str | Path = None,
    left=0,
    right=0,
    top=0,
    bottom=0,
    force_relative=False,
):
    """
    Adds margins to each page of a PDF file.

    Args:
        input_path (str | Path): The path to the input PDF file.
        output_path (str | Path, optional): The path for the output PDF file. If None, overwrites the input file.
        left (int | float, optional): The left margin to add (absolute or relative).
        right (int | float, optional): The right margin to add (absolute or relative).
        top (int | float, optional): The top margin to add (absolute or relative).
        bottom (int | float, optional): The bottom margin to add (absolute or relative).
        force_relative (bool, optional): If True, all margin values are treated as relative to the page size.

    Raises:
        AssertionError: If any margin value is negative.

    Example:
        add_margins("input.pdf", "output.pdf", left=10, right=10, top=5, bottom=5)
    """
    
    # Set the output path to the input path if not provided
    if not output_path:
        output_path = input_path

    input_path = Path(input_path)
    output_path = Path(output_path)

    # Ensure margin values are non-negative
    assert right >= 0, "Right margin cannot be negative"
    assert left >= 0, "Left margin cannot be negative"
    assert top >= 0, "Top margin cannot be negative"
    assert bottom >= 0, "Bottom margin cannot be negative"

    with input_path.open("rb") as f:
        # Read the PDF file
        pdf = PdfReader(f)
        writer = PdfWriter()

        # Process each page in the PDF
        for page in tqdm(pdf.pages):
            # Get the original dimensions of the page
            original_width = float(page.mediabox.width)
            original_height = float(page.mediabox.height)

            # Calculate margins based on whether they are relative or absolute
            if force_relative:
                right = math.ceil(original_width * right)
                left = math.ceil(original_width * left)
                top = math.ceil(original_height * top)
                bottom = math.ceil(original_height * bottom)
            else:
                if right < 1:
                    right = math.ceil(original_width * right)
                if left < 1:
                    left = math.ceil(original_width * left)
                if top < 1:
                    top = math.ceil(original_height * top)
                if bottom < 1:
                    bottom = math.ceil(original_height * bottom)

            # Convert margins to integers
            top = int(top)
            bottom = int(bottom)
            left = int(left)
            right = int(right)

            # Calculate new dimensions for the page with margins
            width = original_width + left + right
            height = original_height + top + bottom

            # Create a new blank page with the desired dimensions
            bg = PageObject.create_blank_page(width=width, height=height)
            # Merge the original page onto the new page
            bg.merge_page(page)
            # Apply the transformation to position the original page
            bg.add_transformation(Transformation().translate(tx=left, ty=bottom))

            # Add the modified page to the writer
            writer.add_page(bg)

        # Write the modified pages to a new PDF file
        with output_path.open("wb") as output_file:
            writer.write(output_file)


