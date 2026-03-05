#!/usr/bin/env python3

import sys
import os

def printhi():
    try:
        s = sys.winver
        user = os.environ["USERNAME"]
    except:
        user = os.environ["USER"].capitalize()

    print(f"Hi, {user}")

if __name__ == "__main__":
    printhi()
