"""
PDF Margin Adder FastAPI Application

This script provides an API endpoint for adding margins to a PDF file
using the `add_margins` function from the `pdfmargins` module. Users can
upload a single PDF file, specify margins in points or as relative values,
and receive the processed PDF file with added margins.
"""
from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Depends
from fastapi.responses import Response
from pathlib import Path
from pdfmargins.add_margins import add_margins
import logging
import tempfile

app = FastAPI()
logging.basicConfig(level=logging.INFO)

async def get_temp_dir():
    """
    Dependency that creates and manages the lifetime of a temporary directory.

    This function uses the `tempfile.TemporaryDirectory()` context manager to
    create a secure temporary directory. The directory and its contents are
    automatically cleaned up when the context is exited, either at the end of
    the request or if an exception is raised.

    Yielding the directory path instead of returning it allows FastAPI to inject
    the temporary directory path as a parameter to the endpoint function.
    """
    temp_dir = tempfile.TemporaryDirectory()
    try:
        yield temp_dir.name
    finally:
        temp_dir.cleanup()

@app.post("/add_margins/")
async def add_margins_to_pdf(
    file: UploadFile = File(...),
    left: float = Form(150),
    right: float = Form(150),
    top: float = Form(0),
    bottom: float = Form(0),
    force_relative: bool = Form(False),
    temp_dir: str = Depends(get_temp_dir),
):
    """
    Endpoint to add margins to an uploaded PDF file.

    Args:
        file (UploadFile): The PDF file to which margins will be added.
        left (float): Left margin in points or relative (default: 150).
        right (float): Right margin in points or relative (default: 150).
        top (float): Top margin in points or relative (default: 0).
        bottom (float): Bottom margin in points or relative (default: 0).
        force_relative (bool): Interpret all margins as relative values if True.
        temp_dir (str): Temporary directory path provided by the `get_temp_dir` dependency.

    Returns:
        Response: The modified PDF file with added margins as bytes.
    """
    # Verify that the uploaded file is a PDF
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF")

    try:
        # Construct input and output file paths within the temporary directory
        input_path = Path(temp_dir) / file.filename
        output_path = Path(temp_dir) / f"{Path(file.filename).stem}.margins.pdf"

        # Write the uploaded file to the temporary input file
        with open(input_path, "wb") as f:
            f.write(await file.read())
            logging.info(f"Uploaded file saved to: {input_path}")

        # Process the PDF with the specified margins
        add_margins(
            input_path,
            output_path,
            left=left,
            right=right,
            top=top,
            bottom=bottom,
            force_relative=force_relative,
        )
        logging.info(f"PDF with margins saved to: {output_path}")

        # Read the contents of the output file as bytes and return them
        # TODO: this is bad as it requires the file to be read into memory and takes a lot of RAM
        #       but if I don't do this, the file gets deleted. This is because fastapi reads it lazy
        #       after this fuctioned returned. But then the context manager already deleted the dir 
        #       and with this the file. Good enough for now...
        with open(output_path, "rb") as f: 
            output_bytes = f.read()

        return Response(
            content=output_bytes,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f"attachment; filename={Path(file.filename).stem}.margins.pdf"
            },
        )
    except Exception as e:
        logging.error(f"Error processing PDF: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")