# Macro-Pad-Raspberry-Pi-Pico
This is a custom, 16-key, macro pad made using the raspberry pi pico and the pico rgb keypad by pimoroni. I have also utilized another github project called rgbkeypad which is very helpful!



**KEY FEATURES:**

  * on keypress a keyboard shortcut is run and the key lights up white as long as it is pressed.
  
  * LEDs timeout and turn off after 5 minutes of no keypresses. All the keys still work, just the LEDs turn off so the board doesn't get too hot.
  
  * all written in CircuitPython
  
  * plug and play. code.py will run right when the board is plugged into a PC.



**LIMITATIONS:**
 
  * I wanted to set this up with the Python os library, but all MicroPython and CircuitPython implimentations do not have the methods to monitor programs opened on the pc.
  
  * I also wanted to use MicroPython but there is no USB_HID support for this board at least. Hopefully this changes in the future.
  
  * Discord does not allow you to keybind the end call button (disconnect)



**TOOLS I USED:**

  * [AutoControl Chrome Extension](https://chrome.google.com/webstore/detail/autocontrol-custom-shortc/lkaihdpfpifdlgoapbfocpmekbokmcfd/related) for shortcuts to websites and   bookmarks in chrome.
  * [Audio Switcher](https://audioswit.ch/er#download) to switch between headphones and speakers
  * [pico-rgbkeypad](https://github.com/martinohanlon/pico-rgbkeypad) is a great github project that got me started
  * A useful windows keyboard shortcut is Markup : <kbd>WIN</kbd> + <kbd>1</kbd> to open first program in taskbar, <kbd>WIN</kbd> + <kbd>2</kbd> to open second, etc.



**FUTURE IDEAS:**
 
  * paint on the keycaps so it looks a little nicer.
  * if usb_hid is added to MicroPython, rewrite code.py
 
![PXL_20220109_213418757](https://user-images.githubusercontent.com/65916505/148702096-f43b39e2-853b-4fdf-8876-185e69089982.jpg)
![PXL_20220109_213232932](https://user-images.githubusercontent.com/65916505/148702098-172b3502-cf49-4fca-931b-7a1f85e40a20.jpg)
