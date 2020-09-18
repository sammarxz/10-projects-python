import time
import pyautogui
import tkinter as tk

from io import BytesIO
from PIL import Image


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

def screenshot():
    name = int(round(time.time() * 1000))
    name = "screenshots/{}.png".format(name)
    root.iconify()
    time.sleep(3)
    img = pyautogui.screenshot(name)


button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot
)

button.pack(side = tk.LEFT)

quit_button = tk.Button(
    frame,
    text="QUIT",
    command=quit
)

quit_button.pack(side = tk.LEFT)

root.title('Simple Screenshot Tool')
root.mainloop()
root.resizable(0,0)

screenshot()