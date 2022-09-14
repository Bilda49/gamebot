from ast import In
from codecs import charmap_encode
import pyautogui
import keyboard
import pydirectinput
import time
from random import randint

inClick = False
rand = randint(1, 2)
randm = randint(1900, 1910)

def switch_tab():
    keyboard.press_and_release('alt + tab')

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
        inClick
        pydirectinput.keyDown('1')
        time.sleep(rand)
        switch_tab()
        time.sleep(rand)
        pydirectinput.keyDown('1')
        time.sleep(randm)