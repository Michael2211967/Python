#! /usr/bin/python3

import secrets

pw = ""
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!§$%&/()=+#-*_"
length = int(input("Bitte gib die Passwortlänge ein: "))

for _ in range(length):
    pw = pw + secrets.choice(chars)

print(pw)
