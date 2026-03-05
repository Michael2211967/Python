#!/usr/bin/python3
import os
import sys

# Den absoluten Pfad des Skripts ermitteln
current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
sys.path.append(current_dir)
from length import zoll
import functions

class Converter:
    def __init__(self):
        self.root = Tk()
        self.image = PhotoImage(file=os.path.join(current_dir, 'length.png'))
        self.root.iconphoto(True, self.image)
        self.title = "Längen-Umrechner"
        self.root.title(self.title)

        self.tv1 = Image.open(os.path.join(current_dir, "images/tv1.jpg"))
        self.tv1_size=(functions.resize_picture(self.tv1.width, self.tv1.height, 230))
        self.tv1 = ImageTk.PhotoImage(self.tv1.resize(self.tv1_size))

        self.tv2 = Image.open(os.path.join(current_dir, "images/tv2.jpg"))
        self.tv2_size=(functions.resize_picture(self.tv2.width, self.tv2.height))
        self.tv2 = ImageTk.PhotoImage(self.tv2.resize(self.tv2_size))

        self.tv3 = Image.open(os.path.join(current_dir, "images/tv3.jpg"))
        self.tv3_size=(functions.resize_picture(self.tv3.width, self.tv3.height))
        self.tv3 = ImageTk.PhotoImage(self.tv3.resize(self.tv3_size))

        self.tv4 = Image.open(os.path.join(current_dir, "images/tv4.jpg"))
        self.tv4_size=(functions.resize_picture(self.tv4.width, self.tv4.height))
        self.tv4 = ImageTk.PhotoImage(self.tv4.resize(self.tv4_size))

        self.geometry = functions.center_window(750, 450, self.root)
        self.font = ("Arial", 14)
        self.root.geometry(self.geometry)
        self.centimeter_active = False
        self.zoll_active = True
        self.centimeter = StringVar()
        self.zoll = StringVar()
        self.converted = StringVar()
        self.cm_prompt = Label(self.root, text="cm: ", font=self.font)
        self.cm_input = Entry(self.root, textvariable=self.centimeter, justify="right", font=self.font)
        self.zoll_prompt = Label(self.root, text="zoll: ", font=self.font)
        self.zoll_input = Entry(self.root, textvariable=self.zoll, justify="right", font=self.font)
        self.cm_prompt.grid(row=0, column=0, padx=5, pady=5)
        self.cm_input.grid(row=0, column=1, padx=5, pady=5)
        self.cm_input.bind("<Return>", self.calculate_zoll)
        self.zoll_prompt.grid(row=0, column=3, padx=5, pady=5)
        self.zoll_input.grid(row=0, column=4, padx=5, pady=5)
        self.zoll_input.bind("<Return>", self.calculate_cm)
        self.calc = Button(self.root, text="Umrechnen", font=self.font, command=self.calculate_zoll)
        self.calc.grid(row=1, column=2, padx=5, pady=5)
        self.centimeter_rb = Radiobutton(self.root, text="cm", value="cm", font=self.font, command=lambda: self.change_output("cm"))
        self.centimeter_rb.grid(row=1, column=4, padx=4, pady=4)
        self.zoll_rb = Radiobutton(self.root, text="zoll", value="zoll", font=self.font, command=lambda: self.change_output("zoll"))
        self.zoll_rb.grid(row=1, column=1, padx=5, pady=5)
        self.zoll_rb.select()
        self.your_tv_label = Label(self.root, text="", font=self.font)
        self.your_tv_image = Label(self.root)
        self.your_tv_label.grid(row=2, column=1, columnspan=4, padx=5, pady=5)
        self.your_tv_image.grid(row=3, column=1, columnspan=4, padx=5, pady=5)
        self.root.mainloop()

    def calculate_zoll(self, event=None):
        if self.converted.get() != "":
            self.converted.set("")
        try:
            centimeter = float(self.centimeter.get())
            converted = zoll(centimeter)
            self.zoll.set(f"{converted: .2f}")
            self.show_tv(converted)
        except:
            messagebox.showerror("Fehler", "Bitte nur Zahlenwerte eingeben!")

    def calculate_cm(self, event=None):
        if self.converted.get() != "":
            self.converted.set("")
        try:
            zoll_value = float(self.zoll.get())
            converted = zoll_value * 2.54
            self.centimeter.set(f"{converted: .2f}")
            self.show_tv(zoll_value)
        except:
            messagebox.showerror("Fehler", "Bitte nur Zahlenwerte eingeben!")

    def change_output(self, length_unit):
        if length_unit == "zoll":
            self.calc.config(command=self.calculate_zoll)
            self.zoll_rb.select()
            self.centimeter_active = False
            self.zoll_active = True
        else:
            self.calc.config(command=self.calculate_cm)
            self.centimeter_rb.select()
            self.centimeter_active = True
            self.zoll_active = False

    def show_tv(self, zoll):
        self.your_tv_label.configure(text="Ist das Ihr Fernsehen? ")
        if zoll < 10:
            self.your_tv_image.configure(image=self.tv1)
        elif 10 <= zoll < 40:
            self.your_tv_image.configure(image=self.tv2)
        elif 40 <= zoll  < 80:
            self.your_tv_image.configure(image=self.tv3)
        else:
            self.your_tv_image.configure(image=self.tv4)

c = Converter()