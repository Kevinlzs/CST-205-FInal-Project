import sys
from PySide6.QtWidgets import (QApplication, QPushButton,
                                QHBoxLayout, QVBoxLayout, QWidget, QLabel)
from PySide6.QtCore import Slot 
class MyWidow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,200)

        layout = QHBoxLayout()
        v2_layout = QVBoxLayout()
        v_layout = QVBoxLayout()

        self.label = QLabel()
        self.blank_label = QLabel()
        self.browse_btn = QPushButton("Browse...")
        self.browse_btn.setFixedSize(70,25)
        self.browse_btn.setStyleSheet("border-radius : 5; border : 2px solid grey")
        self.b1 = QPushButton("Negative")
        self.b1.setFixedSize(70,25)
        self.b2 = QPushButton("Grey")
        self.b2.setFixedSize(70,25)
        self.b3 = QPushButton("Sepia")
        self.b3.setFixedSize(70,25)
        self.b4 = QPushButton("Warm")
        self.b4.setFixedSize(70,25)
        self.b5 = QPushButton("Cool")
        self.b5.setFixedSize(70,25)
        self.b6 = QPushButton("Lark")
        self.b6.setFixedSize(70,25)

        h1_layout = QHBoxLayout()
        h1_layout.addWidget(self.b1)
        h1_layout.addWidget(self.b2)

        h2_layout = QHBoxLayout()
        h2_layout.addWidget(self.b3)
        h2_layout.addWidget(self.b4)

        h3_layout = QHBoxLayout()
        h3_layout.addWidget(self.b5)
        h3_layout.addWidget(self.b6)

        v2_layout.addWidget(self.label)
        v2_layout.addWidget(self.blank_label)
        v2_layout.addWidget(self.browse_btn)
        
        v_layout.addLayout(h1_layout)
        v_layout.addLayout(h2_layout)
        v_layout.addLayout(h3_layout)
        layout.addLayout(v_layout)
        layout.addLayout(v2_layout)
        self.setLayout(layout)
        # self.resize(500,500)

app = QApplication([])
window = MyWidow()
window.show()
sys.exit(app.exec())
        
