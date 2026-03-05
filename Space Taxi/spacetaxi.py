import pygame
import random
import math

# Initialisierung von Pygame
pygame.init()

# Bildschirmgröße
BREITE = 800
HOEHE = 600
BILDSCHIRM = pygame.display.set_mode((BREITE, HOEHE))
pygame.display.set_caption("Spacetaxi")

# Farben
SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)
GELB = (255, 255, 0)
BLAU = (0, 0, 255)
GRUEN = (0, 255, 0)

# Bilder laden (du musst diese Bilder im selben Ordner haben oder die Pfade anpassen)
raumschiff_bild = pygame.image.load("raumschiff.png").convert_alpha() # Erstelle ein einfaches Raumschiff-Bild
planet_bilder = [
    pygame.image.load("erde.png").convert_alpha(),   # Einfache Planeten-Bilder
    pygame.image.load("mars.png").convert_alpha(),
    pygame.image.load("jupiter.png").convert_alpha()
]
raumschiff_skaliert = pygame.transform.scale(raumschiff_bild, (50, 50))

# Raumschiff-Klasse
class Raumschiff(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = raumschiff_skaliert
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.geschwindigkeit = 5
        self.treibstoff = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.geschwindigkeit
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.geschwindigkeit
        if keys[pygame.K_UP]:
            self.rect.y -= self.geschwindigkeit
        if keys[pygame.K_DOWN]:
            self.rect.y += self.geschwindigkeit

        # Begrenzung des Raumschiffs
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > BREITE:
            self.rect.right = BREITE
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HOEHE:
            self.rect.bottom = HOEHE

    def fliegen(self, ziel_x, ziel_y, distanz):
        if self.treibstoff >= distanz:
            winkel = math.atan2(ziel_y - self.rect.centery, ziel_x - self.rect.centerx)
            geschwindigkeit_x = self.geschwindigkeit * math.cos(winkel)
            geschwindigkeit_y = self.geschwindigkeit * math.sin(winkel)

            while self.rect.collidepoint(ziel_x, ziel_y) == False and self.treibstoff > 0:
                self.rect.x += geschwindigkeit_x
                self.rect.y += geschwindigkeit_y
                self.treibstoff -= 0.1 # Treibstoffverbrauch pro Frame (anpassen!)
                BILDSCHIRM.fill(SCHWARZ)
                alle_sprites.draw(BILDSCHIRM)
                pygame.display.flip()
                pygame.time.delay(20) # Langsamere Bewegung

            self.treibstoff = max(0, self.treibstoff)
            return True
        else:
            print("Nicht genügend Treibstoff!")
            return False

# Planeten-Klasse
class Planet(pygame.sprite.Sprite):
    def __init__(self, x, y, bild):
        super().__init__()
        self.image = bild
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.name = random.choice(["Erde", "Mars", "Jupiter"]) # Nur zur Demo

# Passagier-Klasse (könnte später für Interaktion wichtig sein)
class Passagier:
    def __init__(self, start_planet, ziel_planet):
        self.start_planet = start_planet
        self.ziel_planet = ziel_planet

# Spiel-Klasse
class SpacetaxiSpiel:
    def __init__(self):
        self.raumschiff = Raumschiff(BREITE // 2, HOEHE // 2)
        self.planeten_liste = [
            Planet(100, 150, random.choice(planet_bilder)),
            Planet(700, 450, random.choice(planet_bilder)),
            Planet(400, 100, random.choice(planet_bilder))
        ]
        self.alle_sprites = pygame.sprite.Group()
        self.alle_sprites.add(self.raumschiff)
        for planet in self.planeten_liste:
            self.alle_sprites.add(planet)
        self.ausgewaehlter_planet = None
        self.laufend = True
        self.schriftart = pygame.font.Font(None, 30)

    def text_anzeigen(self, text, farbe, x, y):
        textflaeche = self.schriftart.render(text, True, farbe)
        textrechteck = textflaeche.get_rect()
        textrechteck.topleft = (x, y)
        BILDSCHIRM.blit(textflaeche, textrechteck)

    def ereignisse_verarbeiten(self):
        for ereignis in pygame.event.get():
            if ereignis.type == pygame.QUIT:
                self.laufend = False
            if ereignis.type == pygame.MOUSEBUTTONDOWN:
                maus_pos = pygame.mouse.get_pos()
                for planet in self.planeten_liste:
                    if planet.rect.collidepoint(maus_pos):
                        self.ausgewaehlter_planet = planet
                        print(f"Planet ausgewählt: {planet.name}")
            if ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_SPACE and self.ausgewaehlter_planet:
                    distanz = math.sqrt((self.ausgewaehlter_planet.rect.centerx - self.raumschiff.rect.centerx)**2 +
                                       (self.ausgewaehlter_planet.rect.centery - self.raumschiff.rect.centery)**2)
                    if self.raumschiff.fliegen(self.ausgewaehlter_planet.rect.centerx, self.ausgewaehlter_planet.rect.centery, distanz / 10): # Skalierte Distanz für Treibstoff
                        print(f"Angekommen auf {self.ausgewaehlter_planet.name}")
                        self.ausgewaehlter_planet = None # Auswahl aufheben

    def laufen(self):
        uhr = pygame.time.Clock()
        while self.laufend:
            uhr.tick(60)
            self.ereignisse_verarbeiten()
            self.raumschiff.update()

            BILDSCHIRM.fill(SCHWARZ)
            self.alle_sprites.draw(BILDSCHIRM)
            self.text_anzeigen(f"Treibstoff: {self.raumschiff.treibstoff:.1f}", WEISS, 10, 10)
            if self.ausgewaehlter_planet:
                self.text_anzeigen(f"Ziel: {self.ausgewaehlter_planet.name}", GELB, 10, 40)

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    spiel = SpacetaxiSpiel()
    spiel.laufen()
