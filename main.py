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

while True:
    if keyboard.is_pressed(",") and autoclicker_enabled == False:
        autoclicker_enabled = True
        print("ON")
        while autoclicker_enabled:
            sleep(0.01)
            start_clicking()

            if keyboard.is_pressed(",") and  autoclicker_enabled:
                autoclicker_enabled = False
                print("OFF")
                sleep(0.1)