from selenium.webdriver.common.keys import Keys
from web_driver import browser
from selenium.webdriver import ActionChains

from .actions import ABILITY, DIRECTION


def reset_keys():
    action = ActionChains(browser)
    action.key_up(Keys.SPACE)
    action.key_up(Keys.SHIFT)
    action.key_up("w")
    action.key_up("s")
    action.key_up("a")
    action.key_up("d")
    action.perform()


def send_enter():
    action = ActionChains(browser)
    action.send_keys(Keys.ENTER)
    action.perform()


def move(direction: DIRECTION, action: ABILITY = ABILITY.NONE):
    action = ActionChains(browser)
    if direction is DIRECTION.N:
        action.key_down("w")
    if direction is DIRECTION.NE:
        action.key_down("w")
        action.key_down("d")
    if direction is DIRECTION.E:
        action.key_down("d")
    if direction is DIRECTION.SE:
        action.key_down("s")
        action.key_down("d")
    if direction is DIRECTION.S:
        action.key_down("s")
    if direction is DIRECTION.SW:
        action.key_down("s")
        action.key_down("a")
    if direction is DIRECTION.W:
        action.key_down("a")
    if direction is DIRECTION.NW:
        action.key_down("a")
        action.key_down("w")

    if action is ABILITY.HEAL:
        action.key_down(Keys.LEFT_SHIFT)
    if action is ABILITY.RUN:
        action.key_down(Keys.SPACE)

    action.perform()
