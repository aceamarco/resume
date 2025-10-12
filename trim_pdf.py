#!/usr/bin/env python3
"""
Script to trim a PDF file to only the first page.
Usage: python trim_pdf.py <input_pdf> <output_pdf>
"""
import sys
from pypdf import PdfReader, PdfWriter


def trim_to_first_page(input_pdf, output_pdf):
    """Trim PDF to only the first page."""
    # Read the PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Add only the first page
    if len(reader.pages) > 0:
        writer.add_page(reader.pages[0])
        print(f"Original PDF had {len(reader.pages)} page(s)")

        # Write to output file
        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
        print(f"Successfully trimmed to 1 page: {output_pdf}")
    else:
        print("Error: PDF has no pages")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python trim_pdf.py <input_pdf> <output_pdf>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    trim_to_first_page(input_file, output_file)
