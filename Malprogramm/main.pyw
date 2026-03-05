import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, master):
        self.master = master
        master.title("Einfaches Malprogramm")

        self.color = "black"
        self.brush_size = 2

        self.canvas = tk.Canvas(master, width=600, height=400, bg="white")
        self.canvas.grid(row=1, columnspan=5, padx=5, pady=5)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        self.pen_button = tk.Button(master, text="Stift", command=self.use_pen)
        self.pen_button.grid(row=0, column=0, padx=2, pady=2)

        self.color_button = tk.Button(master, text="Farbe", command=self.choose_color)
        self.color_button.grid(row=0, column=1, padx=2, pady=2)

        self.eraser_button = tk.Button(master, text="Radierer", command=self.use_eraser)
        self.eraser_button.grid(row=0, column=2, padx=2, pady=2)

        self.clear_button = tk.Button(master, text="Löschen", command=self.clear_canvas)
        self.clear_button.grid(row=0, column=3, padx=2, pady=2)

        self.size_scale = tk.Scale(master, from_=1, to=10, orient=tk.HORIZONTAL, label="Größe", command=self.set_brush_size)
        self.size_scale.set(self.brush_size)
        self.size_scale.grid(row=0, column=4, padx=2, pady=2)

        self.old_x = None
        self.old_y = None
        self.eraser_on = False

    def use_pen(self):
        self.activate_button(self.pen_button)
        self.eraser_on = False

    def choose_color(self):
        self.color = colorchooser.askcolor(title="Farbe wählen")[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)
        self.eraser_on = True
        self.color = self.canvas["bg"] # Setze die Farbe auf die Hintergrundfarbe des Canvas

    def clear_canvas(self):
        self.canvas.delete("all")

    def set_brush_size(self, size):
        self.brush_size = int(size)

    def activate_button(self, some_button, eraser_mode=False):
        self.pen_button.config(relief=tk.RAISED)
        self.color_button.config(relief=tk.RAISED)
        self.eraser_button.config(relief=tk.RAISED)
        some_button.config(relief=tk.SUNKEN)
        self.eraser_on = eraser_mode

    def paint(self, event):
        if self.old_x and self.old_y:
            paint_color = self.color if not self.eraser_on else self.canvas["bg"]
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.brush_size, fill=paint_color,
                               capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

root = tk.Tk()
app = PaintApp(root)
root.mainloop()