import pyautogui  # type: ignore
from PIL import Image  # type: ignore
import pytesseract # type: ignore

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtCore import QSize

def check_for_roshan(width:int, height:int) -> bool:
    y = int(height/2)
    width = int(width/4)
    height = int(height/4)

    x1, y1, width, height = 0, y, width, height

    take_screenshot(x1, y1, width, height)

    # Use Tesseract OCR to extract text from the image
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Path to Tesseract OCR executable
    extracted_text = pytesseract.image_to_string(Image.open('screenshot.png'))

    # Define the word you want to detect
    word_to_detect = "Roshan"

    # Check if the word is present in the extracted text
    if word_to_detect.lower() in extracted_text.lower():
        return True
    else:
        return False
    
def take_screenshot(x:int,y:int,w:int,h:int) -> None:
    screenshot = pyautogui.screenshot(region=(x, y, w, h))
    screenshot.save("screenshot.png")   