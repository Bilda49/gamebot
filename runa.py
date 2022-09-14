from ast import In
from codecs import charmap_encode
import pyautogui
import keyboard
import pydirectinput
import time
from random import randint, random

inClick = False
random_digit = random()

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
        time.sleep(random_digit)
#        pydirectinput.keyDown('tab')
#        time.sleep(2)
#        pydirectinput.keyDown('3')
#        time.sleep(1)
#        pydirectinput.keyDown('2')
#111        time.sleep(1)