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
    keypad.brightness = 1
    
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
            kb.press(Keycode.CONTROL, Keycode.ALT, Keycode.LEFT_BRACKET)
            kb.release(Keycode.CONTROL, Keycode.ALT, Keycode.LEFT_BRACKET)
        # discord
        if y == 1:
            kb.press(Keycode.CONTROL, Keycode.ALT, Keycode.RIGHT_BRACKET)
            kb.release(Keycode.CONTROL, Keycode.ALT, Keycode.RIGHT_BRACKET)
        # spotify
        if y == 2:
            kb.press(Keycode.CONTROL, Keycode.ALT, Keycode.BACKSLASH)
            kb.release(Keycode.CONTROL, Keycode.ALT, Keycode.BACKSLASH)
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
            kb.press(Keycode.CONTROL, Keycode.ALT, Keycode.P)
            kb.release(Keycode.CONTROL, Keycode.ALT, Keycode.P)
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
            kb.press(Keycode.CONTROL, Keycode.ALT, Keycode.ZERO)
            kb.release(Keycode.CONTROL, Keycode.ALT, Keycode.ZERO)
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
            kb.press(Keycode.CONTROL, Keycode.ALT, Keycode.NINE)
            kb.release(Keycode.CONTROL, Keycode.ALT, Keycode.NINE)
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
    lastPress = time.time()
    tcolor = WHITE
    
    while True:
        current = time.time()
        if current > lastPress + 60:
            tcolor = OFF
        keypad.brightness = 0.5
        keypad.color = tcolor # initialize keypad lights
        
        for key in keypad.keys:
            if key.is_pressed():
                lastPress = current
                tcolor = WHITE
                keypad.color = tcolor
                
                key.color = colorPress(key.x, key.y)
                functionPress(key.x, key.y)
                
                while key.is_pressed():
                    time.sleep(0.05) # keep color on if button is held
                
        time.sleep(0.05)

main()
