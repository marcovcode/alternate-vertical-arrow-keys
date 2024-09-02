import keyboard
import time

# Initialize the state to track whether to press up or down
press_up = True

def on_space_press():
    global press_up
    if press_up:
        keyboard.press_and_release('up')
    else:
        keyboard.press_and_release('down')
    press_up = not press_up

# Hook the space key to the on_space_press function
keyboard.on_press_key('space', lambda _: on_space_press())

# Keep the script running
print("Press space to alternate between pressing arrow up and arrow down. Press ESC to exit.")
keyboard.wait("esc")
