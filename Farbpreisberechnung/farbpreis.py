#! /usr/bin/python3
import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir)
import c64demo
farbpreis_bas = os.path.join(current_dir, "farbpreis.bas")
def input_float(prompt: str):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("?REDO FROM START")
            
def p_input():
    print()
    length = input_float("Länge eingeben: ")
    width = input_float("Breite eingeben: ")
    return length, width

def processing(kiloprice, kiloquantity, length, width):
    area = length * width
    quantity = area * kiloquantity
    price = quantity * kiloprice
    return area, quantity, price

def output(area, quantity, price):
    print()
    print(f"Für die Fläche von {area:.2f} qm")
    print(f"werden {quantity:.2f} Kilo Farbe benötigt.")
    print(f"Der Preis für diese {quantity:.2f} kg Farbe beträgt {price:.2f} EUR.")
    
if __name__ == "__main__" :
    Retro_Look = int(input("Möchten Sie einen Retrolook vom C64 (0 = nein)? "))
    if Retro_Look != 0:
        print("\033[94m\033[44m/033[2 q", flush=True, end="")
        c64demo.Power_onMessage()
        c64demo.Load_Basic("farbpreis")
        c64demo.List_Basic(farbpreis_bas)
        c64demo.Type_Command("RUN")
    kiloprice = input_float("Preis je Kilo Farbe eingeben: ")
    kiloquantity = input_float("Kilo je Quadratmeter eingeben: ")
    answer="ja"
    while answer == "ja" or answer == "j":
        length, width = p_input()
        area, quantity, price = processing(kiloprice, kiloquantity, length, width)
        output(area, quantity, price)
        answer=input("\nWollen Sie eine neue Fläche berechnen? ").lower()
    print("\nAuf Wiedersehen!\n")
    if Retro_Look != 0:
        print("READY.\033[0m")
