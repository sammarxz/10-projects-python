import os
import time
import pyautogui


def screenshot():
    name = int(round(time.time() * 1000))
    name = "screenshots/{}.png".format(name)
    time.sleep(3)
    img = pyautogui.screenshot(name)
    img.show()
    

screenshot()