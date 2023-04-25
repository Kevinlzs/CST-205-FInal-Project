import sys
from PIL import Image
from PIL.ImageQt import ImageQt
import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, 
                                QPushButton, QLineEdit, QVBoxLayout, QComboBox, QHBoxLayout, QFileDialog)
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QDesktopServices

class FileDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,400)
        self.btn = QPushButton("Upload an Image")
        self.btn.clicked.connect(self.getImageFile)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.label)
        self.setLayout(layout)
    def getImageFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.jpg *.png)")
        # , _ allows us to get the file name not the path
        print(filename)
        image = QPixmap(filename)
        image = image.scaled(300, 300, Qt.KeepAspectRatio)
        self.label.setPixmap(image)

app = QApplication([])
window = FileDialog()
window.show()
sys.exit(app.exec())