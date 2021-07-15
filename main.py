import pytesseract
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

from config import config
from custom_gym import DigDigEnv
from web_driver import browser, take_screenshot_and_text
import gym
import os.path

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# try:
env = DigDigEnv()

if not os.path.isfile(config["model"]):
    model = PPO("MlpPolicy", env, verbose=1)
else:
    model=PPO.load(config["model"])

while True:
    model.learn(total_timesteps=10)
    model.save(config["model"])

browser.close()
# except Exception as e:
#     browser.close()
#     raise e
