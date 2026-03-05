#!/usr/bin/python3
import os
import sys

# Den absoluten Pfad des Skripts ermitteln
current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
from tkinter import *
from tkinter import font, messagebox
from PIL import Image, ImageTk
sys.path.append(current_dir)
import functions

class PowerConverter:
    def __init__(self):
        self.root = Tk()
        self.title = "Leistungsumrechner"
        self.root.title(self.title)
        self.image = PhotoImage(file=os.path.join(current_dir, 'power.png'))
        self.root.iconphoto(True, self.image)

        self.car1 = Image.open(os.path.join(current_dir, "images/car1.jpg"))
        self.car1_size=(functions.resize_picture(self.car1.width, self.car1.height))
        
        self.car2 = Image.open(os.path.join(current_dir, "images/car2.jpg"))
        self.car2_size=(functions.resize_picture(self.car2.width, self.car2.height))
        
        self.car3 = Image.open(os.path.join(current_dir, "images/car3.jpg"))
        self.car3_size=(functions.resize_picture(self.car3.width, self.car3.height, 600))
        
        self.car1 = ImageTk.PhotoImage(self.car1.resize(self.car1_size))
        self.car2 = ImageTk.PhotoImage(self.car2.resize(self.car2_size))
        self.car3 = ImageTk.PhotoImage(self.car3.resize(self.car3_size))
        self.font = font.Font(family="Arial", size=14)
        self.geometry = functions.center_window(800, 450, self.root)
        self.root.geometry(self.geometry)
        self.kw = StringVar()
        self.ps = StringVar()
        self.kw_label = Label(self.root, text="Kilowatt (kW): ", font=self.font)
        self.kw_input = Entry(self.root, textvariable=self.kw, justify="right", font=self.font)
        self.kw_input.bind('<Return>', self.calculate_PS)
        self.kw_label.grid(row=0, column=0, padx=5, pady=5)
        self.kw_input.grid(row=0, column=1, padx=5, pady=5)
        self.ps_label = Label(self.root, text="PS: ", font=self.font)
        self.ps_input = Entry(self.root, textvariable=self.ps, justify="right", font=self.font)
        self.ps_input.bind('<Return>', self.calculate_kW)
        self.ps_label.grid(row=0, column=3, padx=5, pady=5)
        self.ps_input.grid(row=0, column=4, padx=5, pady=5)
        self.ps_rb = Radiobutton(self.root, text="PS", font=self.font, value="PS", command=lambda: self.change_output("PS"))
        self.kw_rb = Radiobutton(self.root, text="kW", font=self.font, value="kW", command=lambda: self.change_output("kW"))
        self.calc = Button(self.root, text="Umrechnen", font=self.font, command=self.calculate_PS)
        self.ps_rb.grid(row=1, column=1, padx=5, pady=5)
        self.calc.grid(row=1, column=2, padx=5, pady=5)
        self.kw_rb.grid(row=1, column=4, padx=5, pady=5)
        self.ps_rb.select()
        self.your_car_label = Label(self.root, text="", font=self.font)
        self.your_car_image = Label(self.root)
        self.your_car_label.grid(row=2, column=1, columnspan=4, padx=5, pady=5)
        self.your_car_image.grid(row=3, column=1, columnspan=4, padx=5, pady=5)
        self.root.mainloop()

    def change_output(self, unity):
        if unity == "PS":
            self.ps_rb.select()
            self.calc.config(command=self.calculate_PS)
        else:
            self.kw_rb.select()
            self.calc.config(command=self.calculate_kW)

    def calculate_PS(self, event=None):
        try:
            kw = float(self.kw.get())
            ps = kw * 1.36
            self.ps.set(f"{ps: .2f}")
            self.show_car(ps)
        except:
            messagebox.showerror("Fehler", "Bitte nur Zahlenwerte eingeben!")

    def calculate_kW(self, event=None):
        try:
            ps = float(self.ps.get())
            kw = ps / 1.36
            self.kw.set(f"{kw: .2f}")
            self.show_car(ps)
        except:
            messagebox.showerror("Fehler", "Bitte nur Zahlenwerte eingeben!")

    def show_car(self, ps):
        self.your_car_label.configure(text="Ist das Ihr Auto?")
        if ps < 100:
            self.your_car_image.configure(image=self.car1)
        elif 100 <= ps < 200:
            self.your_car_image.configure(image=self.car2)
        else:
            self.your_car_image.configure(image=self.car3)


pc = PowerConverter()