import sys
from PIL import Image
from PIL.ImageQt import ImageQt
import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, 
                                QPushButton, QLineEdit, QVBoxLayout, QComboBox, QHBoxLayout, QFileDialog)
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QDesktopServices

class NewWindow(QWidget):
    def __init__(self, filename):
        super().__init__()
        self.label = QLabel()
        img = Image.open(filename)
        grayscale_list = [ ( (a[0]+a[1]+a[2])//3, ) * 3 for a in img.getdata() ]
        img.putdata(grayscale_list)
        qim = ImageQt(img)
        pixmap = QPixmap.fromImage(qim)
        pixmap = pixmap.scaled(500,500, Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

class FileDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,400)
        self.btn = QPushButton("Browse...")
        self.negativeBtn = QPushButton("Negative")
        self.btn.setFixedSize(70,25)
        self.btn.setStyleSheet("border-radius : 5; border : 2px solid grey")
        self.btn.clicked.connect(self.getImageFile)
        self.btn.clicked.connect(self.openNewWindow)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout.addWidget(self.btn)
        layout2.addWidget(self.label)
        layout.addLayout(layout2)
        self.setLayout(layout)
    def getImageFile(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.jpg *.png)")
        # , _ allows us to get the file name not the path
        print(self.filename)
        image = QPixmap(self.filename)
        image = image.scaled(300, 300, Qt.KeepAspectRatio)
        self.label.setPixmap(image)
    def openNewWindow(self):
        self.newWindow = NewWindow(self.filename)
        self.newWindow.show()

app = QApplication([])
window = FileDialog()
window.show()
sys.exit(app.exec())