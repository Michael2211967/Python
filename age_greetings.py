#!/usr/bin/python3

from age import age_calc
from datetime import date, datetime

name = input("Wie heissen Sie? ")
birthday = input("Wann sind Sie geboren? ")
age = age_calc(birthday)

time = datetime.now()
print("\nPython:~$", end=" ")
if 6 <= time.hour < 12:
    print(f"Guten Morgen, {name}")
elif 12 <= time.hour < 18:
    print(f"Guten Tag, {name}")
elif 18 <= time.hour < 23:
    print(f"Guten Abend, {name}")
else:
    print(f"Gute Nacht, {name}")

print(f"Python:~$ Sie sind aktuell {age} Jahre alt.")
