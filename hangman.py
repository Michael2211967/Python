#!/usr/bin/python3
import random as rnd

with open("Teil_058_Wörter.txt") as f:
    word = rnd.choice([w.strip().upper() for w in f])

trials, wanted, advised = 10, set(b for b in word), set()

while trials > 0:
    output = f"Noch {trials:>2} Versuche: "
    output += " ".join([f"{b if b in advised else '_'}" for b in word])
    trial = input(output + " Ihr Buchstabe? ").upper()
    advised.add(trial)
    if trial not in wanted:
        trials -= 1
    if wanted.issubset(advised):
        break

result = "GEWONNEN! " if trials > 0 else "VERLOREN! "
print(f"{result} Das gesuchte Wort war {word}")
