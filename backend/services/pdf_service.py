import io

import fitz
import pytesseract
from PIL import Image

# Add this line
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)

    text = ""

    for page in doc:

        # Try extracting embedded text first
        page_text = page.get_text()

        if page_text.strip():
            text += page_text
        else:
            # OCR for scanned pages
            pix = page.get_pixmap(dpi=300)

            img = Image.open(io.BytesIO(pix.tobytes("png")))

            ocr_text = pytesseract.image_to_string(img)

            text += ocr_text

    doc.close()

    return text