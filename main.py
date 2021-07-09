import time

from selenium.webdriver.support.wait import WebDriverWait

from input import move, send_enter, DIRECTION
from web_driver import browser
try:
    time.sleep(2)
    send_enter()
    move(DIRECTION.NW)

except Exception as e:
    browser.close()
    raise e
