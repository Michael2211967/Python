#!/usr/bin/python3
import sys
import tkinter as tk
from tkinter import filedialog

class Editor:
    def __init__(self, window):
        try:
            self.file = sys.argv[1]
        except:
            self.file = ""
        window.title(f"Texteditor: {self.file}")
        self.SCREEN_WIDTH = window.winfo_screenwidth()
        self.SCREEN_HEIGHT = window.winfo_screenheight()
        self.WIN_WIDTH = 1200
        self.WIN_HEIGHT = 600
        self.WIN_X = (self.SCREEN_WIDTH - self.WIN_WIDTH) // 2
        self.WIN_Y = (self.SCREEN_HEIGHT - self.WIN_HEIGHT) // 2
        window.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}+{self.WIN_X}+{self.WIN_Y}")
        window.resizable(False, False)

        menubar = tk.Menu(window)
        window.config(menu=menubar)

        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Datei", menu=filemenu)

        filemenu.add_command(label="Neu", command=self.neu)
        filemenu.add_command(label="Öffnen", command=self.oeffnen)
        filemenu.add_command(label="Speichern", command=self.speichern)
        filemenu.add_command(label="Speichern unter ...", command=self.speicher_unter)
        filemenu.add_command(label="Schließen", command=self.beenden)

        editmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Bearbeiten", menu=editmenu)

        editmenu.add_command(label="Rückgängig", command=self.rueckgaengig)

        self.text_widget = tk.Text(window, wrap=tk.WORD, width=148, height=37)
        self.text_widget.pack()

        self.text_widget.bind("<KeyRelease>", self.text_geaendert)
        self.undo_stack = [self.text_widget.get("1.0", "end-1c")]
        window.bind("<Control-z>", self.rueckgaengig)

        if self.file:
            self.oeffnen(self.file)
    
    def neu(self):
        self.text_widget.delete("1.0", tk.END)
        self.undo_stack.clear()
        self.file = ""
        root.title(f"Texteditor: {self.file}")

    def oeffnen(self, file=None):
        if file:
            dateipfad = file
        else:
            dateipfad = filedialog.askopenfilename(filetypes=[("Textdateien", "*.txt")])
        if dateipfad:
            with open(dateipfad, "r") as datei:
                inhalt = datei.read()
                self.text_widget.delete("1.0", tk.END)
                self.text_widget.insert(tk.END, inhalt)
                self.file = dateipfad
                root.title(f"Texteditor: {self.file}")
                self.undo_stack.clear()
                datei.close()
    
    def speicher_unter(self):
        dateipfad = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textdateien", "*.txt")])
        if dateipfad:
            inhalt = self.text_widget.get("1.0", tk.END)
            with open(dateipfad, "w") as datei:
                datei.write(inhalt)
                datei.close()
            self.file = dateipfad
            root.title(f"Texteditor: {self.file}")

    def speichern(self):
        if self.file:
            with open(self.file, "w") as datei:
                datei.write(self.text_widget.get("1.0", tk.END))
                datei.close()
        else:
            self.speicher_unter()

    def beenden(self):
        root.destroy()

    def rueckgaengig(self, event=None):
        if self.undo_stack:
            letzter_zustand = self.undo_stack.pop()
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert(tk.END, letzter_zustand)

    def text_geaendert(self, event=None):
        aktueller_zustand = self.text_widget.get("1.0", "end-1c")
        if not self.undo_stack or aktueller_zustand != self.undo_stack[-1]:
            self.undo_stack.append(aktueller_zustand)
            self.text_widget.edit_separator()

def rueckgaengig_machen(event):
    edit.rueckgaengig()

root = tk.Tk()
edit = Editor(root)
root.wm_protocol("WM_DELETE_WINDOW", edit.beenden)
root.bind_all("<Control-z>", rueckgaengig_machen)
root.mainloop()
