aufgabe = """
3.) a. Schreibe eine Funktion 'note_eintragen', welche eine
    Listen-Parameter 'notenliste' und einen Integer-Parameter
    'note' hat. Die Funktion soll die Note der Notenliste hinzufügen
    und anschließend die neue Notenliste als Rückgabewert zurückgeben.
 
    b. Es dürfen nur gültige Noten hinzugefügt werden (1-6).
    Wenn die Note ungültig ist, soll die Funktion die Notenliste
    unverändert zurückgeben.
"""
# Hinweis: Erstelle keine Variablen außerhalb der Funktion!
# Schreibe hier deinen Code für Aufgabe 3 👇

def note_eintragen(notenliste, note):
    if note >= 1 and note <= 6:
        notenliste.append(note)
        return notenliste
    else:
        return notenliste


if __name__ == "__main__":
    print(aufgabe)
    notenliste = []
    try:
        note = int(input("Bitte Note eingeben: "))
        notenliste = note_eintragen(notenliste, note)
        print(notenliste)
    except:
        print("Bitte nur Zahlen eingeben!")








 
























 


###################################################################
#
#---------- NACHFOLGENDEN TESTCODE (NICHT VERÄNDERN!) -------------
#
# Imports
import unittest
import io
import sys


class TestCode(unittest.TestCase):

    def test_note_eintragen(self):
        self.assertEqual(note_eintragen([], 2), [2])
        self.assertEqual(note_eintragen([3, 4], 1), [3, 4, 1])
        self.assertEqual(note_eintragen([], 0), [], msg="Note 0 ist ungültig, wurde aber eingetragen!")
        self.assertEqual(note_eintragen([], 7), [], msg="Note 7 ist ungültig, wurde aber eingetragen!")



if __name__ == "__main__":
    unittest.main()
