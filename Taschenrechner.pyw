import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Taschenrechner")
        self.master.configure(bg="#000000")

        # Label zur Anzeige der Eingabe
        self.display = tk.Entry(master, width=30, justify="right", bg="#AAAAAA", fg="#222222", font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Buttons
        buttons = [
            '(', ')', 'C', 'off',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        # Erstellen der Buttons mit einer Schleife
        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.handle_button_click(x)
            tk.Button(master, text=button, width=5, height=2, bg="#444444", fg="#FFFFFF", font=("Arial", 14), command=command).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1        

    def handle_button_click(self, button):
        # Wenn "="-Button gedrückt wird, führe Berechnung aus
        if button == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        # Wenn "C"-Button gedrückt wird, lösche den Inhalt des Anzeigelabels
        elif button == "C":
            self.display.delete(0, tk.END)
        elif button == "off":
            self.master.destroy()
        # Andernfalls füge den gedrückten Button zur Eingabe hinzu
        else:
            self.display.insert(tk.END, button)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
