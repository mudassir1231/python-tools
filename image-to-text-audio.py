from PIL import Image
import pytesseract 
from pytesseract import image_to_string
from gtts import gTTS
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

image1 =  Image.open("C:\\python\\basic-projects\\converter\\image.jpg")

text1= image_to_string(image1)

print(text1)

sound = gTTS(text=text1, lang='en', slow=False) 

sound.save("sound.mp3")

# os.system("start sound.mp3")