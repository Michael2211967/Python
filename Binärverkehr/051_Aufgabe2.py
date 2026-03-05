aufgabe = """
2.) Schreibe eine Funktion 'addieren', welche zwei Integer-Parameter 'a'
    und 'b' hat und die Summe der beiden Zahlen zurückgibt.
    Wenn die Funktion mit den Argumenten '2' und '4' aufgerufen wird soll
    sie als Ergebnis die Summe aus 2 + 4, also 6 zurückgeben.
"""
# Hinweis: es wird kein print() oder input() benötigt!
# Schreibe hier deinen Code für Aufgabe 2 👇

def addieren(a, b):
    return a + b

if __name__ == "__main__":
    print(aufgabe)
    try:
        a = int(input("Gib bitte Zahl 1 ein: "))
        b = int(input("Gib bitte Zahl 2 ein: "))
    except:
        print("Bitte nur Zahlen eingeben!")

    try:
        ergebnis = addieren(a, b)
        print(f"\n\n{a} + {b} = {ergebnis}")
    except:
        pass
                










































 

###################################################################
#
#---------- NACHFOLGENDEN TESTCODE (NICHT VERÄNDERN!) -------------
#
# Imports
import unittest
import io
import sys
#
#
#
# 1.) Funktion 'begrüßen'
#
class TestCode(unittest.TestCase):
    # 2.) Funktion 'addieren'
    def test_addieren(self):
        self.assertEqual(addieren(2, 4), 6)
        self.assertEqual(addieren(2, -4), -2)
        self.assertEqual(addieren(-2, 4), 2)
        self.assertEqual(addieren(-2, -4), -6)



if __name__ == "__main__":
    unittest.main()
