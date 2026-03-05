# browser.pyw

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtWebEngineWidgets import *

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welt-Browser")

        # Widgets
        self.setWindowIcon(QIcon("welt.png"))
        self.webView = QWebEngineView(self)
        self.addressBar = QLineEdit(self)
        self.searchButton = QPushButton("Suchen", self)

        #Layout
        hbl = QHBoxLayout()
        hbl.addWidget(self.addressBar)
        hbl.addWidget(self.searchButton)
        vbl = QVBoxLayout()
        vbl.addLayout(hbl)
        vbl.addWidget(self.webView)
        self.setLayout(vbl)

        # Connections
        self.addressBar.returnPressed.connect(self.search)
        self.searchButton.clicked.connect(self.search)

        self.show()

    def search(self):
        # Zeige Webseite mit angegebener Adresse
        address = str(self.addressBar.text())
        if address:
            if "://" not in address:
                address = "http://" + address
            url = QUrl(address)
            self.webView.load(url)

app = QApplication(sys.argv)
browser = Browser()
sys.exit(app.exec_())
