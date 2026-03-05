aufgabe = """
4.) Schreibe eine Funktion namens 'konto_aktion', die ein Dictionary mit
den Schlüsseln 'kontostand' (Guthaben), 'betrag' (Betrag) und 'aktion'
(Aktion) als Parameter erhält. Die Funktion soll das aktualisierte
Dictionary zurückgeben, das zusätzlich den Schlüssel 'status' mit
einem entsprechenden Wert enthält.

Die Regeln für die Funktion sind:

a.) Wenn die Aktion "einzahlen" ist, wird der Betrag dem Kontostand
    hinzugefügt und die Nachricht lautet "erfolgreich".

b.) Wenn die Aktion "auszahlen" ist, wird der Betrag vom Kontostand
    abgezogen, vorausgesetzt das Konto ist ausreichend gedeckt.
    Falls nicht, lautet die Nachricht "fehlgeschlagen".

c.) Wenn die Aktion weder "einzahlen" noch "auszahlen" ist, passiert
    nichts und die Nachricht lautet "ungültig".

Beispiele:

Argument:   {
            "kontostand": 300,
            "betrag": 200,
            "aktion": "einzahlen"
            }
Rückgabe:
            {
            "kontostand": 500,
            "betrag": 200,
            "aktion": "einzahlen",
            "status": "erfolgreich"
            }
"""
# Schreibe hier deinen Code für Aufgabe 4 👇
 
def konto_aktion(data):
    kontostand, betrag, aktion = data["kontostand"], data["betrag"], data["aktion"]
    if aktion == "einzahlen":
        kontostand += betrag
        data["kontostand"] = kontostand
        data["status"] = "erfolgreich"
        return data
    elif aktion == "auszahlen":
        if kontostand >= betrag:
            kontostand -= betrag
            data["kontostand"] = kontostand
            data["status"] = "erfolgreich"
            return data
        else:
            data["status"] = "fehlgeschlagen"
            return data
    else:
        data["status"] = "ungültig"
        return data
        

if __name__ == "__main__":
    print(aufgabe)
    try:
        kontostand = int(input("Geben Sie den Kontostand ein: "))
        betrag = int(input("Geben Sie den Betrag ein: "))
        aktion = input("Geben Sie die Aktion ein: ")
        ergebnis = konto_aktion({"kontostand": kontostand, "betrag": betrag, "aktion": aktion})
        print(ergebnis)
    except:
        print("Nur Zahlen eingeben")
    






























































 


###################################################################
#
#---------- NACHFOLGENDEN TESTCODE (NICHT VERÄNDERN!) -------------
#
# Imports
import unittest
import io
import sys


class TestCode(unittest.TestCase):

    def test_konto_aktion(self):
        test_dict1 = {"kontostand": 300, "betrag": 200, "aktion": "einzahlen"}
        expected1 = {"kontostand": 500, "betrag": 200, "aktion": "einzahlen", "status": "erfolgreich"}
        test_dict2 = {"kontostand": 300, "betrag": 200, "aktion": "auszahlen"}
        expected2 = {"kontostand": 100, "betrag": 200, "aktion": "auszahlen", "status": "erfolgreich"}
        test_dict3 = {"kontostand": 300, "betrag": 500, "aktion": "auszahlen"}
        expected3 = {"kontostand": 300, "betrag": 500, "aktion": "auszahlen", "status": "fehlgeschlagen"}
        test_dict4 = {"kontostand": 300, "betrag": 200, "aktion": "sasfasr"}
        expected4 = {"kontostand": 300, "betrag": 200, "aktion": "sasfasr", "status": "ungültig"}
        self.assertEqual(konto_aktion(test_dict1),expected1)
        self.assertEqual(konto_aktion(test_dict2),expected2)
        self.assertEqual(konto_aktion(test_dict3),expected3)
        self.assertEqual(konto_aktion(test_dict4),expected4)


if __name__ == "__main__":
    unittest.main()
