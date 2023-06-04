from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
print(pytesseract.image_to_string(r'C:\Users\DELL\Desktop\Data Analysis\day 9\Image_proccesing\download (3).png'))
