import csv
import random

class Lotto:
    def __init__(self, filename="lotto.csv"):
        self.filename = filename
        self.draws = []

    def generate_numbers(self):
        """Generiert eine Zufallsziehung mit 6 Zahlen zwischen 1 und 49."""
        numbers = sorted(random.sample(range(1, 50), 6))
        self.draws.append(numbers)
        return numbers

    def save_to_csv(self):
        """Speichert alle Ziehungen in eine CSV-Datei."""
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Ziehung 1", "Ziehung 2", "Ziehung 3", "Ziehung 4", "Ziehung 5", "Ziehung 6"])
            writer.writerows(self.draws)

    def load_from_csv(self):
        """Lädt Ziehungen aus der CSV-Datei."""
        self.draws.clear()
        try:
            with open(self.filename, mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Überspringt die Header-Zeile
                for row in reader:
                    self.draws.append([int(num) for num in row])
            return self.draws
        except FileNotFoundError:
            print("Keine gespeicherten Ziehungen gefunden.")
            return []

    def show_draws(self):
        """Zeigt gespeicherte Ziehungen an."""
        if not self.draws:
            print("Keine Ziehungen vorhanden.")
        else:
            for i, draw in enumerate(self.draws, start=1):
                print(f"Ziehung {i}: {draw}")

# Einfaches Menü für die Anwendung
def main():
    lotto = Lotto()

    while True:
        print("\nLotto Menü:")
        print("1 - Neue Lottozahlen generieren")
        print("2 - Ziehungen speichern")
        print("3 - Ziehungen laden")
        print("4 - Ziehungen anzeigen")
        print("5 - Beenden")
        choice = input("Wähle eine Option: ")

        if choice == "1":
            print("Generierte Zahlen:", lotto.generate_numbers())
        elif choice == "2":
            lotto.save_to_csv()
            print("Ziehungen gespeichert.")
        elif choice == "3":
            lotto.load_from_csv()
            print("Ziehungen geladen.")
        elif choice == "4":
            lotto.show_draws()
        elif choice == "5":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe, bitte erneut versuchen.")

# Programm starten
if __name__ == "__main__":
    main()
