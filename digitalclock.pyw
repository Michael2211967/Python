#! /usr/bin/python3
# digitalclock.pyw

from time import *
from datetime import datetime, timezone
from tkinter import *
import _thread

class clock:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("200x100")
        self.root.title("Uhr")
        self.utcNow = datetime.now(timezone.utc)
        self.localNow = datetime.now()
        self.UTC = StringVar()
        self.time = StringVar()
        Label(self.root, textvariable=self.UTC,font=("Arial","30")).pack()
        Label(self.root, textvariable=self.time,font=("Arial","28")).pack()
        _thread.start_new_thread(self.timeshow, ())
        self.root.mainloop()

    def timeshow(self):
        while True:
            self.utcNow = datetime.now(timezone.utc)
            self.localNow = datetime.now()
            self.UTC.set(self.utcNow.strftime("%H:%M:%S"))
            self.time.set(self.localNow.strftime("%H:%M:%S"))
            sleep(1)

clock = clock()
        
