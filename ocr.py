import cv2
import numpy as np
import pytesseract
from PIL import Image


def ocr_image(img: Image.Image, lang: str = "eng") -> str:
    """Run OCR on a chat screenshot and return text."""
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(binary, lang=lang)
    return text.strip()