from selenium import webdriver
import os
from config import config

_driver_path = os.path.join(os.getcwd(), 'web_driver', 'geckodriver.exe')
browser = webdriver.Firefox(executable_path=_driver_path)
browser.set_window_size(config["window_size"]["width"], config["window_size"]["height"])
browser.get('https://digdig.io/')
browser.execute_script(f"localStorage.setItem('digdig_nickname', '{config['username']}');")
browser.execute_script("localStorage.setItem('digdig_keyboard_control', 'Y');")
