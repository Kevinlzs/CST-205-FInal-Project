import sys
from PySide6.QtWidgets import (QApplication, QPushButton,
                                QHBoxLayout, QVBoxLayout, QWidget)
from PySide6.QtCore import Slot 
class MyWidow(QWidget):
    def __init__(self):
        super().__init__()

        v_layout = QVBoxLayout()
        self.b1 = QPushButton("Negative")
        self.b2 = QPushButton("Grey")
        self.b3 = QPushButton("Sepia")
        self.b4 = QPushButton("Warm")
        self.b5 = QPushButton("Cool")
        self.b6 = QPushButton("Lark")

        v_layout.addWidgit(self.b1)
        v_layout.addWidgit(self.b2)
        v_layout.addWidgit(self.b3)
        v_layout.addWidgit(self.b4)
        v_layout.addWidgit(self.b5)
        v_layout.addWidgit(self.b6)

        h1_layout = QHBoxLayout()
        h1_layout.addWidget(self.b1)
        h1_layout.addWidget(self.b2)

        h2_layout = QHBoxLayout()
        h2_layout.addWidget(self.b3)
        h2_layout.addWidget(self.b4)

        h3_layout = QHBoxLayout()
        h3_layout.addWidget(self.b5)
        h3_layout.addWidget(self.b6)

        v_layout.addLayout(h1_layout)
        v_layout.addLayout(h2_layout)
        v_layout.addLayout(h3_layout)
        self.setLayout(v_layout)

app = QApplication([])
window = MyWidow()
window.show()
sys.exit(app.exec())
        
