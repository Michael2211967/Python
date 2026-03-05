#!/usr/bin/env python3
import locale
locale.setlocale(locale.LC_ALL, "de_DE.utf8")

def zinsrechner():
    kapital = float(input("Bitte geben Sie Ihr Kapital ein: "))
    zins = float(input("Bitte Geben Sie den Zins an: "))
    n = float(input("Bitte geben Sie die Anlagedauer an: "))
    endkapital = kapital * (1 + (zins / 100)) ** n
    print(endkapital)
    antwort = f"Ihre {kapital:n} € wachsen in {n:n} Jahren bei {zins:n}% jährlicher Verzinsung auf {round(endkapital,2):n} €."
    return antwort

print(zinsrechner())
