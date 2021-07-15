import time
import numpy as np
import gym
from PIL import Image
from gym import spaces
from pytesseract import pytesseract

from input import actions, send_enter, move
from web_driver import take_screenshot
import matplotlib.pyplot as plt


class DigDigEnv(gym.Env):
    """
    Custom Environment that follows custom_gym interface.
    This is a simple env where the agent must learn to go always left.
    """
    # Because of google colab, we cannot implement the GUI ('human' render mode)
    metadata = {'render.modes': ['console']}
    # Define constants for clearer code
    LEFT = 0
    RIGHT = 1

    def __init__(self, grid_size=10):
        super(DigDigEnv, self).__init__()

        # Size of the 1D-grid
        # self.grid_size = grid_size
        # # Initialize the agent at the right of the grid
        # self.agent_pos = grid_size - 1

        # Define action and observation space
        # They must be custom_gym.spaces objects
        # Example when using discrete actions, we have two: left and right
        self.action_space = spaces.Discrete(actions.DIRECTION.__len__())
        # The observation will be the coordinate of the agent
        # this can be described both by Discrete and Box space
        # TODO Calculate actual image size
        self.observation_space = spaces.Box(low=0, high=1, shape=(588*1264,), dtype="float32")

    def reset(self):
        """
        Important: the observation must be a numpy array
        :return: (np.array)
        """
        send_enter()
        send_enter()
        self.obs = take_screenshot()
        self.start_time = time.time()
        return self.obs.flatten()

    def step(self, action):
        # if action == self.LEFT:
        #     self.agent_pos -= 1
        # elif action == self.RIGHT:
        #     self.agent_pos += 1
        # else:
        #     raise ValueError("Received invalid action={} which is not part of the action space".format(action))

        move(action)

        self.obs = take_screenshot()

        # Account for the boundaries of the grid
        # self.agent_pos = np.clip(self.agent_pos, 0, self.grid_size)

        # Are we at the left of the grid?
        img = Image.fromarray(self.obs).convert("L")
        done = pytesseract.image_to_string(img)
        print(done)
        # Null reward everywhere except when reaching the goal (left of the grid)
        reward = time.time() - self.start_time

        # Optionally we can pass additional info, we are not using that for now
        info = {}

        return self.obs.flatten(), reward, done, info

    def render(self, ):
        plt.imshow(self.obs, cmap="gray")
        plt.show()
        plt.pause(0.001)

    def close(self):
        pass
