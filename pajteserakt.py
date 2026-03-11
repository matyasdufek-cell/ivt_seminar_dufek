import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\dufek\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread("L19-ocr.png")
img = img[320:550, :, :]
text = pytesseract.image_to_string(img, "eng")

print(text)