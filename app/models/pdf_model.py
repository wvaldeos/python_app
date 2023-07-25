import pytesseract
from pdf2image import convert_from_path
from app import app
import os

def extract_text(filename):
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # ajusta esto a la ruta de tu ejecutable de Tesseract
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    images = convert_from_path(pdf_path)

    text = ""
    for i in range(len(images)):
        text += pytesseract.image_to_string(images[i], lang='spa')

    return text
