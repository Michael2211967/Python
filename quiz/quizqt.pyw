#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMenuBar, QAction, QTextEdit, QDialog, QVBoxLayout as DialogVBoxLayout, QInputDialog, QMessageBox
from fragen_loader import lade_fragen # Angenommen, fragen_loader.py existiert
from highscores_anzeige import HighscoreFenster
import random  # Importiere das random-Modul

class QuizFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt Quiz')
        self.fragen = lade_fragen('quizfragen.txt')
        self.fragen_liste = list(self.fragen.items()) # Um einfach auf Fragen zuzugreifen
        random.shuffle(self.fragen_liste)  # Mische die Fragenliste zufällig
        self.aktuelle_frage_index = 0
        self.punkte = 0
        self.highscores = self.laden_highscores() # Highscores laden

        self.frage_label = QLabel()
        self.antwort_eingabe = QLineEdit()
        self.antwort_button = QPushButton('Antworten')
        self.feedback_label = QLabel()
        self.punkte_label = QLabel(f'Punkte: {self.punkte}')
        self.highscores_fenster = None # Referenz für das Highscore-Fenster

        self.init_ui()
        self.naechste_frage_anzeigen()

    def init_ui(self):
        self.zentrales_widget = QWidget() # Neues zentrales Widget
        self.setCentralWidget(self.zentrales_widget) # Zentrales Widget setzen
        self.layout = QVBoxLayout(self.zentrales_widget) # Layout für das zentrale Widget
        self.layout.addWidget(self.frage_label)
        self.layout.addWidget(self.antwort_eingabe)
        self.layout.addWidget(self.antwort_button)
        self.layout.addWidget(self.feedback_label)
        self.layout.addWidget(self.punkte_label)

        # Menüleiste erstellen
        menueleiste = self.menuBar()
        datei_menue = menueleiste.addMenu('Datei') # Oder 'Optionen'

        # "Highscores anzeigen"-Aktion erstellen
        highscores_anzeigen_aktion = QAction('Highscores anzeigen', self)
        highscores_anzeigen_aktion.triggered.connect(self.zeige_highscores)
        datei_menue.addAction(highscores_anzeigen_aktion)

        # Signal des Buttons mit einer Methode verbinden (Slot)
        self.antwort_button.clicked.connect(self.antwort_pruefen)

    def laden_highscores(self):
        highscores = []
        try:
            with open('highscores.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    name, punkte = line.strip().split(',')
                    highscores.append((name, int(punkte)))
        except FileNotFoundError:
            pass # Datei existiert noch nicht, also leere Liste zurückgeben
        return highscores

    def speichern_highscores(self):
        with open('highscores.txt', 'w', encoding='utf-8') as f:
            for name, punkte in self.highscores:
                f.write(f"{name},{punkte}\n")

    def naechste_frage_anzeigen(self):
        if self.aktuelle_frage_index < len(self.fragen_liste):
            frage, _ = self.fragen_liste[self.aktuelle_frage_index]
            self.frage_label.setText(frage)
            self.antwort_eingabe.clear()
            self.feedback_label.setText('')
        else:
            self.quiz_beendet()

    def antwort_pruefen(self):
        if self.aktuelle_frage_index < len(self.fragen_liste):
            _, richtige_antwort = self.fragen_liste[self.aktuelle_frage_index]
            benutzer_antwort = self.antwort_eingabe.text().lower().strip()
            richtige_antwort = richtige_antwort.lower().strip()

            if benutzer_antwort == richtige_antwort:
                self.feedback_label.setText('Richtig!')
                self.punkte += 1
            else:
                self.feedback_label.setText(f'Falsch. Die richtige Antwort war: {richtige_antwort}')

            self.punkte_label.setText(f'Punkte: {self.punkte}')
            self.aktuelle_frage_index += 1
            self.naechste_frage_anzeigen()
            
    def quiz_beendet(self):
        self.frage_label.setText(f'Quiz beendet! Endergebnis: {self.punkte} von {len(self.fragen)}')
        self.antwort_eingabe.setEnabled(False)
        self.antwort_button.setEnabled(False)
        self.frage_nach_namen()

    def frage_nach_namen(self):
        name, ok = QInputDialog.getText(self, 'Highscore', 'Gib deinen Namen ein:')
        if ok and name:
            self.highscores.append((name, self.punkte))
            self.highscores.sort(key=lambda item: item[1], reverse=True) # Nach Punkten absteigend sortieren
            # Nur die Top-N Highscores behalten (z.B. Top 10)
            self.highscores = self.highscores[:10]
            self.speichern_highscores()
            QMessageBox.information(self, 'Highscore', f'Dein Ergebnis von {self.punkte} wurde gespeichert!')

    def zeige_highscores(self):
        if self.highscores_fenster is None:
            self.highscores_fenster = HighscoreFenster(self.highscores)
        self.highscores_fenster.aktualisiere_liste(self.highscores) # Sicherstellen, dass es aktuell ist
        self.highscores_fenster.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    quiz_app = QuizFenster()
    quiz_app.show()
    sys.exit(app.exec_())
