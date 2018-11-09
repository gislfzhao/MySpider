# -*- coding: utf-8 -*-
import tesserocr
import pytesseract
from PIL import Image

image = Image.open('code1.jpg')
# image = image.convert('L')
# image = image.convert('1')
# image.show()
# threshold = 127
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# image = image.point(table, '1')
# image.show()
result = tesserocr.image_to_text(image)
print(result)
result2 = pytesseract.image_to_string(image)
print(result2)
