from ast import In
from codecs import charmap_encode
import pyautogui
import keyboard
import pydirectinput
import time
from random import *

inClick = False
count = 0
random_digit = triangular(0, 1)

def switch_tab():
    keyboard.press_and_release('alt + tab')

def set_clicker():
    global inClick
    if inClick:
        inClick = False
        print('off')
    else:
        inClick = True
        print('on')

keyboard.add_hotkey('Alt + Z', set_clicker)

while True:
    if inClick:
        pydirectinput.keyDown('1')
        count +=1
        time.sleep(random_digit)
        random_digit = triangular(0, 2)
#       pydirectinput.keyDown('tab')
#       time.sleep(1)
        if count == 2000:
            switch_tab()
            time.sleep(random_digit)
            pydirectinput.keyDown('1')
            time.sleep(random_digit)
            switch_tab()
            count = 0