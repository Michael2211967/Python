#!/usr/bin/env python3
country = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15", "G": "16", \
           "H": "17", "I": "18", "J": "19", "K": "20", "L": "21", "M": "22", "N": "23", \
           "O": "24", "P": "25", "Q": "26", "R": "27", "S": "28", "T": "29", "U": "30", \
           "V": "31", "W": "32", "X": "33", "Y": "34", "Z": "35"}

iban = input("Geben Sie bitte die IBAN ein: ")

countryCode=country[iban[0]] + country[iban[1]]
blz = iban[4:12]
kto = iban[-10:]

test = int(blz + kto + countryCode + "00") % 97
checksum = 98 - test

control = int(iban[2:4])
print()

if control == checksum:
    print("Die IBAN scheint korrekt zu sein.")
else:
    print("Die Prüfsumme in der IBAN stimmt nicht mit der errechneten überein (Zahlendreher?)")

