#!/usr/bin/env python3
import tkinter as tk

root = tk.Tk()
root.title("Hallo Welt")
root.geometry("300x200")
label1 = tk.Label(root, text="hello world")
label1.pack()
root.mainloop()

print("Das Fenster ist geschlossen")
