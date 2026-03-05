#! /usr/bin/python3
import pyautogui as pag
import random as rnd
import time
print("Drücken Sie Strg-C zum Beenden!")
try:
    while True:
        x = rnd.randint(100, 2400)
        y = rnd.randint(200,1300)
        pag.moveTo(x, y)
        time.sleep(2)
except KeyboardInterrupt:
    print("\n")
