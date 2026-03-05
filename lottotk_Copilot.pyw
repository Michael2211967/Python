import tkinter as tk
from tkinter import messagebox
import csv
import random

class LottoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lotto-Programm")
        self.root.geometry("400x300")

        self.lotto = Lotto()

        self.label = tk.Label(root, text="Lotto Zahlen Generator", font=("Arial", 14))
        self.label.pack(pady=10)

        self.spin_label = tk.Label(root, text="Anzahl der Ziehungen:")
        self.spin_label.pack()
        self.spinbox = tk.Spinbox(root, from_=1, to=10, width=5)  # Auswahl von 1 bis 10 Ziehungen
        self.spinbox.pack()
        
        self.generate_button = tk.Button(root, text="Ziehung generieren", command=self.generate_numbers)
        self.generate_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Ziehungen speichern", command=self.save_to_csv)
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(root, text="Ziehungen laden", command=self.load_from_csv)
        self.load_button.pack(pady=5)

        self.show_button = tk.Button(root, text="Ziehungen anzeigen", command=self.show_draws)
        self.show_button.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def generate_numbers(self):
        numbers = self.lotto.generate_numbers()
        count = int(self.spinbox.get())  # Anzahl der Ziehungen abrufen
        results = [self.lotto.generate_numbers() for _ in range(count)]
        self.result_label.config(text="Generierte Zahlen: " + str(numbers))

    def save_to_csv(self):
        self.lotto.save_to_csv()
        messagebox.showinfo("Erfolg", "Ziehungen gespeichert!")

    def load_from_csv(self):
        self.lotto.load_from_csv()
        messagebox.showinfo("Erfolg", "Ziehungen geladen!")

    def show_draws(self):
        draws = self.lotto.draws
        if not draws:
            messagebox.showinfo("Info", "Keine Ziehungen vorhanden.")
        else:
            messagebox.showinfo("Ziehungen", "\n".join([f"Ziehung {i+1}: {draw}" for i, draw in enumerate(draws)]))

class Lotto:
    def __init__(self, filename="lotto.csv"):
        self.filename = filename
        self.draws = []

    def generate_numbers(self):
        numbers = sorted(random.sample(range(1, 50), 6))
        self.draws.append(numbers)
        return numbers

    def save_to_csv(self):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Ziehung 1", "Ziehung 2", "Ziehung 3", "Ziehung 4", "Ziehung 5", "Ziehung 6"])
            writer.writerows(self.draws)

    def load_from_csv(self):
        self.draws.clear()
        try:
            with open(self.filename, mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Header überspringen
                for row in reader:
                    self.draws.append([int(num) for num in row])
        except FileNotFoundError:
            messagebox.showwarning("Warnung", "Keine gespeicherten Ziehungen gefunden.")

# Tkinter-App starten
if __name__ == "__main__":
    root = tk.Tk()
    app = LottoApp(root)
    root.mainloop()
