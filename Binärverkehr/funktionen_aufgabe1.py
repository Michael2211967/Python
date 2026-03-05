aufgabe = """
1.) Schreibe eine Funktion 'begrüßen' mit einem
    String-Parameter 'name'. Wenn die Funktion
    mit dem Argument 'Max' aufgerufen wird, soll
    sie den Text "Hallo, Max!" in der Konsole ausgeben.
"""
# Hinweis: es wird print() benötigt
# Schreibe hier deinen Code für Aufgabe 1 👇

def begrüßen(name):
    print(f"Halo, {name}!")

if __name__ == "__main__":
    print(aufgabe)
    name = input("Gib Deinen vornamen ein: ")
    begrüßen(name)
