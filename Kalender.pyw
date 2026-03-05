import tkinter as tk
import customtkinter
from tkcalendar import Calendar

root = customtkinter.CTk()
root.title("Kalender")
widget = Calendar(Master=root, font="Arial 25")
widget.pack()
root.mainloop()
