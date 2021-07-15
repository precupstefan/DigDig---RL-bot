import pytesseract
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

from custom_gym import DigDigEnv
from web_driver import browser, take_screenshot
import gym


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# try:
env = DigDigEnv()
# check_env(env,warn=True)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000, log_interval=4)
model.save("dqn-digdig")

browser.close()
# except Exception as e:
#     browser.close()
#     raise e
