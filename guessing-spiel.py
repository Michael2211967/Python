#! /bin/python3
import random

def main():
    # Zufällige Zahl zwischen 1 und 100 generieren
    number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Willkommen beim Zahlenratespiel!")
    print("Ich denke mir eine Zahl zwischen 1 und 100 aus. Kannst du sie erraten?")

    while not guessed:
        guess = int(input("Dein Tipp: "))
        attempts += 1

        if guess == number:
            print("Gut geraten! Du hast die Zahl in", attempts, "Versuchen gefunden.")
            guessed = True
        elif guess < number:
            print("Zu niedrig! Versuch es nochmal.")
        else:
            print("Zu hoch! Versuch es nochmal.")

if __name__ == '__main__':
    main()
