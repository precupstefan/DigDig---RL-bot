from io import BytesIO

from PIL import Image
from pytesseract import pytesseract
from selenium import webdriver
import os
from config import config
import matplotlib.pyplot as plt

_driver_path = os.path.join(os.getcwd(), 'web_driver', 'chromedriver.exe')
browser = webdriver.Chrome(executable_path=_driver_path)
browser.set_window_size(config["window_size"]["width"], config["window_size"]["height"])
browser.get('https://digdig.io/')
browser.execute_script(f"localStorage.setItem('digdig_nickname', '{config['username']}');")
browser.execute_script("localStorage.setItem('digdig_keyboard_control', 'Y');")


def take_screenshot_and_text():
    text = ""
    st = browser.get_screenshot_as_png()
    file_jpgdata = BytesIO(st)
    dt = Image.open(file_jpgdata)
    text = pytesseract.image_to_string(dt)
    file_jpgdata = BytesIO(st)
    img = plt.imread(file_jpgdata)
    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
    return imgGray, text
