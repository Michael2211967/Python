#!/usr/bin/python3
import time
import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir)
datum = os.path.join(current_dir, "datum.py")

file = open(datum, "r")
file_list = file.readlines()
file.close()
for i, line in enumerate(file_list):
    print(f"{(i+1)*10} {line.upper()}", end="")
    time.sleep(0.1)

