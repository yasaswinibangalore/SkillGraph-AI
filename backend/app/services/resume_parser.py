
import fitz
from pathlib import Path


def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF resume."""

    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError("Resume file not found.")

    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are supported.")

    text = ""

    with fitz.open(pdf_path) as document:
        for page in document:
            text += page.get_text() + "\n"

    if not text.strip():
        raise ValueError("No readable text found in this PDF.")

    return text