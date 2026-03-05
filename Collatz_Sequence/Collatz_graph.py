import pygame as pg
import collatz
# pygame ab Version 2.0 wird benötigt
# Installation im Terminal mit
#   --> pip install pygame (windows)
#   --> pip3 install pygame (mac)
#   --> sudo apt-get install python3-pygame (Linux Debian/Ubuntu/Mint)

pg.init()
größe = breite, höhe = 1200, 1080
fenster = pg.display.set_mode(größe)

print(collatz.collatz_seq(3))

# Zeichenschleife mit FPS Bildern pro Sekunde
while True:
  fenster.fill('black')

  for ereignis in pg.event.get():
    if ereignis.type == pg.QUIT or ereignis.type == pg.KEYDOWN and ereignis.key == pg.K_ESCAPE: quit()

  pg.display.flip()
