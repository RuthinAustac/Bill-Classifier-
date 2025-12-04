import pytesseract
import cv2
import os
from pdf2image import convert_from_path
from PIL import Image
import numpy as np

# If Tesseract is not automatically detected, set its path manually:
# Example for Windows:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return ""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.strip()

def extract_text_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    text_content = []
    for page in pages:
        text = pytesseract.image_to_string(page)
        text_content.append(text)
    return "\n".join(text_content).strip()

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png']:
        return extract_text_from_image(file_path)
    elif ext == '.pdf':
        return extract_text_from_pdf(file_path)
    else:
        return ""
