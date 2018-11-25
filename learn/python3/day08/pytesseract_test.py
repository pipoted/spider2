import pytesseract
from PIL import Image

image = Image.open('te.png')
text = pytesseract.image_to_string(image, 'chi_sim')
print(text)
