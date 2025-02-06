#! /usr/bin/python3

def p_input():
    print()
    length = float(input("Länge eingeben: "))
    width = float(input("Breite eingeben: "))
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
    kiloprice = float(input("Preis je Kilo Farbe eingeben: "))
    kiloquantity = float(input("Kilo je Quadratmeter eingeben: "))
    answer="ja"
    while answer == "ja" or answer == "j":
        length, width = p_input()
        area, quantity, price = processing(kiloprice, kiloquantity, length, width)
        output(area, quantity, price)
        answer=input("\nWollen Sie eine neue Fläche berechnen? ")
    print("\nAuf Wiedersehen!\n")
