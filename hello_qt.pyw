# hello_qt.pyw

import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
w = QWidget()
w.resize(250, 100)
w.setWindowTitle("Hallo Qt")
w.show()
sys.exit(app.exec())
