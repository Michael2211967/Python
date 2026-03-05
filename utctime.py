#! /usr/bin/python3

from datetime import datetime, timezone
from time import sleep
from funktionen import clear

minutes = int(input("Wieviel Minuten soll die Uhr laufen? "))
seconds = minutes * 60
for i in range(seconds):
    clear()
    utc_now = datetime.now(timezone.utc)
    time_now = datetime.now()
    print(f"{int(i/60)}\tUTC: {utc_now.hour:02d}:{utc_now.minute:02d}:{utc_now.second:02d}\tLokalzeit: {time_now.hour:02d}:{time_now.minute:02d}:{time_now.second:02d}")
    sleep(1)
