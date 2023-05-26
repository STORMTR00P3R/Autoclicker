for pynput.mouse import Button, Controller
from time import sleep
import keyboard

mouse = Controller()

def start_clicking():
    print("Click")
    mouse.press(Button.Left)
    mouse.release(Button.left)

print("Listening...")

autoclicker_enabled = False

