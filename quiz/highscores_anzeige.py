from PyQt5.QtWidgets import QDialog, QTextEdit, QVBoxLayout

class HighscoreFenster(QDialog):
    def __init__(self, highscores):
        super().__init__()
        self.setWindowTitle('Highscores')
        self.highscores = highscores
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.highscores_anzeige = QTextEdit()
        self.highscores_anzeige.setReadOnly(True)
        layout.addWidget(self.highscores_anzeige)
        self.setLayout(layout)
        self.zeige_liste()

    def zeige_liste(self):
        text = ""
        for name, punkte in self.highscores:
            text += f"{name}: {punkte}\n"
        self.highscores_anzeige.setText(text)

    def aktualisiere_liste(self, neue_highscores):
        self.highscores = neue_highscores
        self.zeige_liste()

if __name__ == '__main__':
    # Testcode (optional)
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    test_highscores = [("Alice", 10), ("Bob", 8), ("Charlie", 8), ("David", 5)]
    fenster = HighscoreFenster(test_highscores)
    fenster.show()
    sys.exit(app.exec_())
