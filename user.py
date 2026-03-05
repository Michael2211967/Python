#!/usr/bin/env python3
#
#  test.py
#  
#  Copyright 2025 Norbert Bielski <norbert@norbert-Asus>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import sys
import os
import time

try:
    user=os.environ["USERNAME"]
except:
    user=os.environ["USER"].capitalize()

def main(args):
    lt  =  time.localtime()
    hour  = lt.tm_hour
    minute = lt.tm_min
    second = lt.tm_sec
    if hour >= 0 and hour <= 7:
        greeting = f"So früh am Computer, {user}? Geh' lieber ins Bett"
    if hour > 7 and hour <= 12:
        greeting = f"Guten Morgen, {user}"
    if hour > 13 and hour <= 18:
        greeting = f"Guten Tag, {user}"
    if hour > 18 and hour <= 21:
        greeting = f"Guten Abend, {user}"
    if hour > 21 and  hour <= 23:
        greeting = f"Hi {user}, so spät noch aktiv ???"
    print(f"{greeting} um {hour:02d}:{minute:02d}:{second:02d}")
    time.sleep(10)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
