#!/usr/bin/python3
import os
import sys

# Den absoluten Pfad des Skripts ermitteln
current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
from tkinter import *
from tkinter import messagebox
sys.path.append(current_dir)
import functions

class EuroConverter:
    def __init__(self):
        self.root = Tk()
        self.title = "Euro-Umrechner"
        self.root.title(self.title)
        self.image = PhotoImage(file=os.path.join(current_dir, 'euro.png'))
        self.root.iconphoto(True, self.image)
        self.font = ("Arial", 14)
        self.geometry = functions.center_window(750, 200, self.root)
        self.root.geometry(self.geometry)
        self.euro_active = False
        self.dm_active = True
        self.currency = StringVar()
        self.converted = StringVar()
        self.netto_euro = StringVar()
        self.mwst_euro = StringVar()
        self.netto_dm = StringVar()
        self.mwst_dm = StringVar()
        self.mwst = StringVar()
        self.netto_label = Label(self.root, text="Netto: ", font=self.font)
        self.netto_euro_label = Label(self.root, textvariable=self.netto_euro, font=self.font)
        self.mwst_euro_label = Label(self.root, textvariable=self.mwst_euro, font=self.font)
        self.netto_dm_label = Label(self.root, textvariable=self.netto_dm, font=self.font)
        self.mwst_dm_label = Label(self.root, textvariable=self.mwst_dm, font=self.font)
        self.mwst_label = Label(self.root, text="MwSt (%): ", font=self.font)
        self.mwst_entry = Entry(self.root, textvariable=self.mwst, justify="right", font=self.font, width=5)
        self.mwst.set("19.0")
        self.mwst_entry.bind('<Return>', self.calculate_mwst)
        self.netto_label.grid(row=0, column=0,sticky="w", padx=5, pady=5)
        self.netto_euro_label.grid(row=0, column=2, sticky="e", padx=5, pady=5)
        self.netto_dm_label.grid(row=0, column=5, sticky="e", padx=5, pady=5)
        self.mwst_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.mwst_entry.grid(row=1, column=1, padx=5, pady=5)
        self.mwst_euro_label.grid(row=1, column=2, sticky="e", padx=5,pady=5)
        self.mwst_dm_label.grid(row=1, column=5, sticky="e", padx=5, pady=5)
        self.euro_prompt = Label(self.root, text="Euro: ", font=self.font)
        self.euro_input = Entry(self.root, textvariable=self.currency, justify="right", font=self.font, width=15)
        self.euro_input.bind('<Return>', self.calculate_dm)
        self.euro_prompt.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.euro_input.grid(row=2, column=2, padx=5, pady=5)
        self.DM_prompt = Label(self.root, text="DM: ", font=self.font)
        self.DM_input = Entry(self.root, textvariable=self.converted, justify="right", font=self.font, width=15)
        self.DM_input.bind('<Return>', self.calculate_euro)
        self.DM_prompt.grid(row=2, column=4, sticky="w", padx=5, pady=5)
        self.DM_input.grid(row=2, column=5, padx=5, pady=5)
        self.DM_rb = Radiobutton(self.root, text="DM", value="DM", font=self.font, command=lambda: self.change_output("DM"))
        self.euro_rb = Radiobutton(self.root, text="Euro", value="Euro", font=self.font, command=lambda: self.change_output("Euro"))
        self.DM_rb.grid(row=3, column=2, padx=5, pady=5)
        self.euro_rb.grid(row=3, column=5, padx=5, pady=5)
        self.DM_rb.select()
        self.calc = Button(self.root, text="Umrechnen", font=self.font, command=self.calculate_dm)
        self.calc.grid(row=3, column=3, padx=5, pady=5)
        self.currency.set("1.00")
        self.calculate_dm()
        self.root.mainloop()

    def change_output(self, currency):
        if currency == "DM":
            self.DM_rb.select()
            self.calc.config(command=self.calculate_dm)
            self.euro_active = False
            self.dm_active = True
        else:
            self.euro_rb.select()
            self.calc.config(command=self.calculate_euro)
            self.euro_active = True
            self.dm_active = False

    def calculate_dm(self, event=None):
        try:
            euro = float(self.currency.get())
            converted = euro * 1.95583
            self.converted.set(f"{converted: .2f}")
        except:
            messagebox.showerror("Fehler", "Bitte nur Zahlenwerte eingeben!")
        self.calculate_mwst()         

    def calculate_euro(self, event=None):
        try:
            dm_value = float(self.converted.get())
            converted = dm_value / 1.95583
            self.currency.set(f"{converted: .2f}")
        except:
            messagebox.showerror("Fehler", "Bitte nur Zahlenwerte eingeben!")
        self.calculate_mwst()

    def calculate_mwst(self, event=None):
        try:
            mwst_value = float(self.mwst.get())
            euro_value = float(self.currency.get())
            dm_value = float(self.converted.get())
            mw_euro = euro_value * mwst_value / (100 + mwst_value)
            nett_euro = euro_value - mw_euro
            mw_dm = dm_value * mwst_value / (100 + mwst_value)
            nett_dm = dm_value - mw_dm
            self.netto_euro.set(f"{nett_euro: .2f}")
            self.mwst_euro.set(f"{mw_euro: .2f}")
            self.netto_dm.set(f"{nett_dm: .2f}")
            self.mwst_dm.set(f"{mw_dm: .2f}")
        except:
          messagebox.showerror("Fehler", "Bitte nur Zahlenwerte eingeben!")
        
ew = EuroConverter()