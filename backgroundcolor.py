import tkinter as tk

def hex_zu_rgb(hex_farbe):
    hex_farbe = hex_farbe.lstrip('#')
    return tuple(int(hex_farbe[i:i+2], 16) for i in (0, 2, 4))

def rgb_zu_hex(rgb_farbe):
    return '#{:02x}{:02x}{:02x}'.format(*rgb_farbe)

def linearer_farbverlauf_hintergrund(canvas, farbe1, farbe2, breite, hoehe, schritte):
    r1, g1, b1 = hex_zu_rgb(farbe1)
    r2, g2, b2 = hex_zu_rgb(farbe2)

    delta_r = (r2 - r1) / schritte
    delta_g = (g2 - g1) / schritte
    delta_b = (b2 - b1) / schritte

    streifen_breite = breite / schritte

    for i in range(schritte):
        r = int(r1 + i * delta_r)
        g = int(g1 + i * delta_g)
        b = int(b1 + i * delta_b)
        farbe = rgb_zu_hex((r, g, b))
        x_start = i * streifen_breite
        x_ende = (i + 1) * streifen_breite
        canvas.create_rectangle(x_start, 0, x_ende, hoehe, fill=farbe, outline="")

if __name__ == "__main__":
    fenster = tk.Tk()
    fenster.title("Farbverlauf als Hintergrund")

    breite = 400
    hoehe = 300
    anzahl_schritte = 100

    hintergrund_canvas = tk.Canvas(fenster, width=breite, height=hoehe, highlightthickness=0)
    hintergrund_canvas.pack(fill="both", expand=True)

    farbe_start = "#F0F8FF"  # Alice Blue
    farbe_ende = "#87CEEB"    # Sky Blue

    linearer_farbverlauf_hintergrund(hintergrund_canvas, farbe_start, farbe_ende, breite, hoehe, anzahl_schritte)

    # Hier könntest du weitere Widgets auf das Fenster packen
    label = tk.Label(fenster, text="Text auf dem Farbverlauf", bg="white") # Transparenter Hintergrund wäre komplexer
    label.pack(pady=20)

    eingabefeld = tk.Entry(fenster)
    eingabefeld.pack(pady=10)

    fenster.mainloop()
