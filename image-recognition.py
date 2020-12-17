import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

print(pytesseract.image_to_string(r'C:\Users\Eduardo Ramos\Desktop\python\Optical\20201119_210826.jpg'))