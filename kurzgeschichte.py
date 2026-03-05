#! /usr/bin/python3
import random

# Begrüßung des Benutzers
name = input("Wie ist dein Name? ")
print("Hallo, " + name + "! Ich werde dir eine Kurzgeschichte erzählen.\n")

# Auswahl eines zufälligen Handlungsstrangs
handlungsstrang = random.choice(["Abenteuer im Dschungel", "Geheimnisvolles Schloss", "Zeitreise ins Mittelalter"])

# Einleitung des Handlungsstrangs
if handlungsstrang == "Abenteuer im Dschungel":
    print("Eines Tages wachtest du im Dschungel auf und wusstest nicht,")
    print("wie du dorthin gekommen bist.")
elif handlungsstrang == "Geheimnisvolles Schloss":
    print("Eines Tages erhieltst du einen Brief, in dem stand, dass du")
    print("ein geheimnisvolles Schloss geerbt hast.")
else:
    print("Eines Tages stolpertest du über einen alten Stein und fielst")
    print("plötzlich durch die Zeit ins Mittelalter.")

# Fortsetzung des Handlungsstrangs
if handlungsstrang == "Abenteuer im Dschungel":
    print("Du machst dich auf den Weg, um den Dschungel zu erkunden.")
    print("Unterwegs triffst du auf eine Gruppe von Forschern, die")
    print("ebenfalls im Dschungel gestrandet sind. Zusammen versucht ihr,")
    print("einen Weg zurück in die Zivilisation zu finden.")
elif handlungsstrang == "Geheimnisvolles Schloss":
    print("Du reist zum Schloss und triffst dort auf einen mysteriösen")
    print("Mann, der behauptet, der Verwalter des Schlosses zu sein. Er")
    print("gibt dir eine Aufgabe, die du erfüllen musst, um das Schloss")
    print("zu erben.")
else:
    print("Du findest dich im Mittelalter wieder und triffst auf eine")
    print("Gruppe von Rittern, die in einen Kampf verwickelt sind. Du")
    print("entscheidest dich, ihnen zu helfen und schließt dich ihrer")
    print("Armee an.")

# Abschluss der Geschichte
print("Am Ende deines Abenteuers hast du viel über dich selbst gelernt")
print("und bist stärker und mutiger geworden. Du kehrst in die Zivilisation")
print("zurück und hast eine unglaubliche Geschichte zu erzählen.")

input()
