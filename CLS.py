#!/usr/bin/env python3

import os, sys
import datum
  
def clear():
    try:
        s = sys.winver
        os.system('cls') 
    except: 
        os.system('clear')
if __name__ == "__main__":   
    clear()
    date = datum.datetime()
    print(date[0])
    print(f"\nHeute ist {date[1]}, der {date[2]}. {date[3]} {date[4]}. Es ist {date[5]:02d}:{date[6]:02d}:{date[7]:02d}")
