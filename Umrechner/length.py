#! /usr/bin/python3

def zoll(i):
    zoll = i / 2.54
    return zoll

if __name__ == "__main__":
    centimeter = float(input("Bitte Geben Sie den Wert in cm ein: "))
    converted = zoll(centimeter)
    print(f"{centimeter} cm sind {converted}\"")