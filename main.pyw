import sys
import datum
import tkinter as tk
from tkinter import ttk

class greeting():
    def __init__(self):
        self.root = tk.Tk()
        self.date = datum.datetime("Michael")
        self.title = f"Heute ist {self.date[1]}, der {self.date[2]}. {self.date[3]} {self.date[4]}. Es ist {self.date[5]:02d}:{self.date[6]:02d}:{self.date[7]:02d}"
        self.root.title(self.title)
        self.root.geometry("640x100")
        self.greeting = ttk.Label(self.root, text=self.date[0], font="Arial 15")
        self.greeting["anchor"] = "w"
        self.greeting["justify"] = "left"
        self.greeting.pack()
        self.datetimelabel = ttk.Label(self.root, text=self.title, font="Arial 15")
        self.datetimelabel["anchor"] ="w"
        self.datetimelabel["justify"] = "left"
        self.datetimelabel.pack()
        self.root.mainloop()

g = greeting()
