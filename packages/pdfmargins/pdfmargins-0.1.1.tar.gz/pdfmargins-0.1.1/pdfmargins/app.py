"""
PDF Margin Adder Gradio Application

This script provides a web interface for adding margins to PDF files
using the `add_margins` function from the `pdfmargins` module. Users can specify margins
in points or as relative values, and the application can process both individual PDF files
and directories containing PDF files.

Dependencies:
- Gradio: A package for creating web applications.
- pdfmargins: The module to add margins to PDF files.
"""

import gradio as gr
from pathlib import Path
from pdfmargins.add_margins import add_margins
import tempfile
import shutil


def process_pdf(input_file, left, right, top, bottom, force_relative):
    """
    Process a single PDF file and add margins.

    Args:
        input_file (Path): The input PDF file.
        left (float): The left margin to add (absolute or relative).
        right (float): The right margin to add (absolute or relative).
        top (float): The top margin to add (absolute or relative).
        bottom (float): The bottom margin to add (absolute or relative).
        force_relative (bool): If True, interpret margins as relative values.

    Returns:
        str: The path to the output PDF file with added margins.
    """
    output_file = Path(input_file.name.replace('.pdf', '.margins.pdf'))
    add_margins(
        input_file,
        output_file,
        left=left,
        right=right,
        top=top,
        bottom=bottom,
        force_relative=force_relative,
    )
    return str(output_file)


def gradio_interface(input_files, left, right, top, bottom, force_relative):
    """
    Gradio interface function to process PDF files.

    Args:
        input_files (list): List of input PDF files.
        left (float): Left margin to add.
        right (float): Right margin to add.
        top (float): Top margin to add.
        bottom (float): Bottom margin to add.
        force_relative (bool): Interpret margins as relative.

    Returns:
        list: List of paths to the output PDF files with added margins.
    """
    output_files = []
    for input_file in input_files:
        output_file = process_pdf(input_file, left, right, top, bottom, force_relative)
        output_files.append(output_file)
    return output_files


# Define the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# PDF Margin Adder")
    gr.Markdown("Upload PDF files or a directory and specify the margins to be added.")

    with gr.Row():
        input_files = gr.File(label="Upload PDF files", file_count="multiple")
        left = gr.Number(label="Left Margin", value=150)
        right = gr.Number(label="Right Margin", value=150)
        top = gr.Number(label="Top Margin", value=0)
        bottom = gr.Number(label="Bottom Margin", value=0)
        force_relative = gr.Checkbox(label="Force Relative Margins", value=False)

    submit_btn = gr.Button("Add Margins")
    output_files = gr.File(label="Download Output Files", file_count="multiple")

    # Define what happens when the button is clicked
    submit_btn.click(
        gradio_interface,
        inputs=[input_files, left, right, top, bottom, force_relative],
        outputs=output_files,
    )

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch()
