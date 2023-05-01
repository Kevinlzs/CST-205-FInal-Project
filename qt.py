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

        self.browse_btn.clicked.connect(self.getImageFile)
        self.b1.clicked.connect(self.openNegative)
        self.b2.clicked.connect(self.openGrayscale)
        self.b3.clicked.connect(self.openSepia)
        self.b4.clicked.connect(self.openWarm)
        self.b5.clicked.connect(self.openCool)
        self.b6.clicked.connect(self.openLark)
        # self.resize(500,500)

        def getImageFile(self):
            self.filename, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.jpg *.png)")
            # , _ allows us to get the file name not the path
            print(self.filename)
            image = QPixmap(self.filename)
            image = image.scaled(300, 300, Qt.KeepAspectRatio)
            self.label.setPixmap(image)
        def openGrayscale(self):
            self.newWindow = NewWindow(self.filename, "grayscale")
            self.newWindow.show()
        def openNegative(self):
            self.newWindow = NewWindow(self.filename, "negative")
            self.newWindow.show()
        def openSepia(self):
            self.newWindow = NewWindow(self.filename, "sepia")
            self.newWindow.show()
        def openWarm(self):
            self.newWindow = NewWindow(self.filename, "warm")
            self.newWindow.show()
        def openCool(self):
            self.newWindow = NewWindow(self.filename, "cool")
            self.newWindow.show()
        def openLark(self):
            self.newWindow = NewWindow(self.filename, "lark")
            self.newWindow.show()

app = QApplication([])
window = MyWidow()
window.show()
sys.exit(app.exec())
        
