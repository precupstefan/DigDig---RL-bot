import pytesseract
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

from config import config
from custom_gym import DigDigEnv
from custom_gym.callback import CustomCallback
from web_driver import browser, take_screenshot_and_text, reload
import gym
import os.path

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# try:
env = DigDigEnv()
file = os.path.join(os.getcwd(),config["model"])
if not os.path.isfile(file+".zip"):
    model = PPO("MlpPolicy", env, verbose=1, n_steps=512, seed=0, device="auto")
    print("new model created")
else:
    model=PPO.load(file)
    model.set_env(env)
    print(" model loaded")

while True:
    callback = CustomCallback()
    model.learn(total_timesteps=3*512, callback=callback)
    model.save(file)
    print("model saved")
    reload()

browser.close()
# except Exception as e:
#     browser.close()
#     raise e
