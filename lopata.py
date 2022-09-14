from ast import In
from codecs import charmap_encode
import pyautogui
import keyboard
import pydirectinput
import time
from random import randint

inClick = False
rand = randint(1880, 1900)

def set_clicker():
    global inClick
    if inClick:
        inClick - False
        print('off')
    else:
        inClick = True
        print('on')

keyboard.add_hotkey('Alt + Z', set_clicker)

while True:
    if inClick:
        pydirectinput.keyDown('1')
        time.sleep(rand)
