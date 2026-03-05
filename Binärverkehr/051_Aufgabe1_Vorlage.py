aufgabe = """
1.) Schreibe eine Funktion 'begrüßen' mit einem
    String-Parameter 'name'. Wenn die Funktion
    mit dem Argument 'Max' aufgerufen wird, soll
    sie den Text "Hallo, Max!" in der Konsole ausgeben.
"""
# Hinweis: es wird print() benötigt
# Schreibe hier deinen Code für Aufgabe 1 👇

def begrüßen(name):
    print(f"Hallo, {name}!")

if __name__ == "__main__":
    print(aufgabe)
    name = input("Gib Deinen vornamen ein: ")
    begrüßen(name)







































 

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
class TestConsoleOutput(unittest.TestCase):
    def test_output(self):
        # Erstelle ein StringIO-Objekt zum Abfangen der Ausgabe
        captured_output = io.StringIO()
        # Leite sys.stdout auf das StringIO-Objekt um
        sys.stdout = captured_output
        
        # Rufe die Funktion auf, die etwas ausgeben soll
        begrüßen("Max")
        begrüßen("Moritz")
        
        # Rückgabe auf die Standardausgabe zurücksetzen
        sys.stdout = sys.__stdout__
        
        # Teste den abgefangenen Inhalt
        self.assertEqual(
            captured_output.getvalue().strip(),
            "Hallo, Max!\nHallo, Moritz!",
            msg="Ausgabe falsch"
            )



if __name__ == "__main__":
    unittest.main()
