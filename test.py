from ast import In
from codecs import charmap_encode
import pyautogui
import keyboard
import pydirectinput
import time

inClick = False

def switch_tab():
    keyboard.press_and_release('alt + tab')

def lopata():
        pydirectinput.keyDown('1')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('1')
        time.sleep(3960)
        pydirectinput.keyDown('2')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('2')
        time.sleep(3960)
        pydirectinput.keyDown('3')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('3')
        time.sleep(3960)
        pydirectinput.keyDown('4')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('4')
        time.sleep(3960)
        pydirectinput.keyDown('5')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('5')
        time.sleep(3960)
        pydirectinput.keyDown('6')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('6')
        time.sleep(3960)
        pydirectinput.keyDown('7')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('7')
        time.sleep(3960)
        pydirectinput.keyDown('8')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('8')
        time.sleep(3960)
        pydirectinput.keyDown('9')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('9')
        time.sleep(3960)
        pydirectinput.keyDown('0')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('0')
        time.sleep(3960)
        pydirectinput.keyDown('f1')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('f1')
        time.sleep(3960)
        pydirectinput.keyDown('f2')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('f2')
        time.sleep(3960)
        pydirectinput.keyDown('f3')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('f3')
        time.sleep(3960)
        pydirectinput.keyDown('f4')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('f4')
        time.sleep(3960)
        pydirectinput.keyDown('f5')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('f5')
        time.sleep(3960)
        pydirectinput.keyDown('f6')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('f6')
        time.sleep(3960)
        pydirectinput.keyDown('f7')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('f7')
        time.sleep(3960)
        pydirectinput.keyDown('f8')
        time.sleep(1)
        switch_tab()
        time.sleep(1)
        pydirectinput.keyDown('f8')


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
        time.sleep(1)
        pydirectinput.keyUp('1')   
        time.sleep(1)     
        pydirectinput.keyDown('2')
        time.sleep(1)

