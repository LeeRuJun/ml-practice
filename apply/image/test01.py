# encoding = utf-8
from PIL import Image
import pytesseract

Image = Image.open('')
text = pytesseract.image_to_string(Image, lang='chi_sim') # 使用简体中文解析图片
print(text)