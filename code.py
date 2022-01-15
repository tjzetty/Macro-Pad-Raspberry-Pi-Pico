from rgbkeypad import RGBKeypad
import time
import board
from digitalio import DigitalInOut, Direction, Pull

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

keypad = RGBKeypad() # initialize keypad

kb = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)


# default color values
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
OFF = (0, 0, 0)

# define color of keypress based on row
def colorPress(x, y):
    # row 0
    if y == 0:
        if x == 0:
            return BLUE
        if x == 1:
            return RED
        if x == 2:
            return YELLOW
        if x == 3:
            return YELLOW
    
    # row 1
    if y == 1:
        return PURPLE
            
    # row 2
    if y == 2:
        return GREEN
    
    # row 3
    if y == 3:
        if x == 0:
            return BLUE
        if x == 1:
            return RED
        if x == 2:
            return BLUE
        if x == 3:
            return BLUE

# define funciton of keypress
def functionPress(x, y):
    # column 0
    if x == 0:
        # chrome
        if y == 0:
            kb.press(Keycode.GUI, Keycode.ONE)
            kb.release(Keycode.GUI, Keycode.ONE)
        # discord
        if y == 1:
            kb.press(Keycode.GUI, Keycode.FOUR)
            kb.release(Keycode.GUI, Keycode.FOUR)
        # spotify
        if y == 2:
            kb.press(Keycode.GUI, Keycode.FIVE)
            kb.release(Keycode.GUI, Keycode.FIVE)
        # alt + tab
        if y == 3:
            kb.press(Keycode.ALT, Keycode.TAB)
            kb.release(Keycode.TAB)
            time.sleep(1)
            kb.release(Keycode.ALT)
    
    # column 1
    if x == 1:
        # youtube
        if y == 0:
            kb.press(Keycode.ALT, Keycode.KEYPAD_ONE)
            kb.release(Keycode.ALT, Keycode.KEYPAD_ONE)
        # discord mute
        if y == 1:
            kb.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.M)
            kb.release(Keycode.CONTROL, Keycode.SHIFT, Keycode.M)
        # play/pause
        if y == 2:
            cc.send(ConsumerControlCode.PLAY_PAUSE)
        # close current program
        if y == 3:
            kb.press(Keycode.ALT, Keycode.F4)
            kb.release(Keycode.ALT, Keycode.F4)
            
    # column 2
    if x == 2:
        # one piece
        if y == 0:
            kb.press(Keycode.ALT, Keycode.KEYPAD_TWO)
            kb.release(Keycode.ALT, Keycode.KEYPAD_TWO)
        # discord deafen
        if y == 1:
            kb.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.D)
            kb.release(Keycode.CONTROL, Keycode.SHIFT, Keycode.D)
        # previous track
        if y == 2:
            cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
        # switch to speakers
        if y == 3:
            kb.press(Keycode.ALT, Keycode.Q)
            kb.release(Keycode.ALT, Keycode.Q)
    
    # column 3
    if x == 3:
        # canvas
        if y == 0:
            kb.press(Keycode.ALT, Keycode.KEYPAD_THREE)
            kb.release(Keycode.ALT, Keycode.KEYPAD_THREE)
        # if y == 1:
            # currently no keybind option to disconnect from a discord call
        # next track
        if y == 2:
            cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        # switch to headphones
        if y == 3:
            kb.press(Keycode.ALT, Keycode.W)
            kb.release(Keycode.ALT, Keycode.W)
            

def main():
    # timeout variables
    lastPress = time.time()
    timeout = False
    fiveMins = 5 * 60 # timeout duration
    
    # running loop
    while True:
        # timeout functionality
        current = time.time()
        if current > lastPress + fiveMins:
            keypad.color = OFF
            timeout = True
        keypad.brightness = 0.2
        
        # update keys
        for key in keypad.keys:
            # timeout visibility
            if timeout:
                key.color = OFF
            else:
                if key.color == OFF or key.color == WHITE:
                    key.color = colorPress(key.x, key.y)
                    
            # on keypress
            if key.is_pressed():
                lastPress = current
                timeout = False
                key.color = WHITE
                functionPress(key.x, key.y)
                
                # keep color on if button is held
                while key.is_pressed():
                    time.sleep(0.05) 
                
        time.sleep(0.05)

# if there is an error turn keypad red and stop the program
# great for debugging new code!
try:
    main()
except Exception as e:
    keypad.color = RED
    time.sleep(10)
    exit()

