#!/usr/bin/env python3
from age import age_calc
from datetime import date, datetime

print("---Willkommen zum Geburtstagskarten-Generator---")

name = input("Name der zu grüßenden Person eingeben: ")
birth = input("Geburtsdatum der zu grüßenden Person eingeben: ")
birthday = datetime.strptime(birth, "%d.%m.%Y")
age = age_calc(birth)
today = date.today()
if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
    age += 1
birthdate = date(today.year, birthday.month, birthday.day).strftime("%d.%m.%Y")
sender = input("Eigenen Namen eingeben: ")

print()
print(f"Hallo {name},")
print()
print(f"ich wünsche Dir alles Gute zum {age}. Geburtstag am {birthdate}.")
print("Ich hoffe, dass Du einen schönen Tag hast und mit Deinen Liebsten feierst.")
print("Zudem wünsche ich Dir alles nur erdenklich Gute für das neue Lebensjahr")
print("und viel Gesundheit.")
print()
print("Liebe Grüße")
print(sender)
