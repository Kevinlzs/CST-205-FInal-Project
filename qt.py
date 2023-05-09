import sys
from PIL import Image
from PIL.ImageQt import ImageQt
import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, 
                                QPushButton, QLineEdit, QVBoxLayout, QComboBox, QHBoxLayout, QFileDialog)
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QDesktopServices, QImageReader

from io import BytesIO
import requests, json
from pprint import pprint

# class NewWindow(QWidget):
#     def __init__(self, filename, type):
#         super().__init__()
#         self.label = QLabel()
#         img = Image.open(filename)
#         if type == "grayscale":
#             grayscale_list = [ ((a[0]+a[1]+a[2])//3, ) * 3 for a in img.getdata() ]
#             img.putdata(grayscale_list)
#             qim = ImageQt(img)
#             pixmap = QPixmap.fromImage(qim)
#             pixmap = pixmap.scaled(500,500, Qt.KeepAspectRatio)
#         elif type == "negative":
#             negative_list = [ (255-p[0], 255-p[1], 255-p[2]) for p in img.getdata() ]
#             img.putdata(negative_list)
#             qim = ImageQt(img)
#             pixmap = QPixmap.fromImage(qim)
#             pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio)
#         elif type == "sepia":
#             sepia_list = [ (int(p[0]*1.1), p[1], int(p[2]*.9)) if p[0] < 63 else (int(p[0]*1.15), p[1], int(p[2]*.85)) if p[0] > 62 and p[0] < 192 else (int(p[0]*1.08), p[1], int(p[2]*.5)) for p in img.getdata()]
#             img.putdata(sepia_list)
#             qim = ImageQt(img)
#             pixmap = QPixmap.fromImage(qim)
#             pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio)
#         elif type == "warm":
#             warm_list = [ (int(p[0] * 1.2), p[1], int(p[2] * .8)) for p in img.getdata() ]
#             img.putdata(warm_list)
#             qim = ImageQt(img)
#             pixmap = QPixmap.fromImage(qim)
#             pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio)
#         elif type == "cool":
#             cool_list = [ (int(p[0] * .8), p[1], int(p[2] * 1.2)) for p in img.getdata() ]
#             img.putdata(cool_list)
#             qim = ImageQt(img)
#             pixmap = QPixmap.fromImage(qim)
#             pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio)
#         elif type == "lark":
#             lark_list = [ (int(p[0] * 1.2), int(p[1]*.9), int(p[2] * .8)) for p in img.getdata() ]
#             # infarred_list = [ (int(p[0] * .5), int(p[1]*.2), int(p[2] * .5)) for p in img.getdata() ]
#             # thermal_list = [ (int(p[0] * .5), int(p[1]*.5), int(p[2] * 1.5)) for p in img.getdata() ]
#             img.putdata(lark_list)
#             qim = ImageQt(img)
#             pixmap = QPixmap.fromImage(qim)
#             pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio)
#         self.label.setPixmap(pixmap)
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.label)
#         self.setLayout(self.layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.resize(600,400)
        # self.btn = QPushButton("Browse...")
        # self.negativeBtn = QPushButton("Negative")
        # self.btn.setFixedSize(70,25)
        # self.btn.setStyleSheet("border-radius : 5; border : 2px solid grey")
        # self.label = QLabel()

        # layout = QVBoxLayout()
        # layout2 = QHBoxLayout()
        # layout.addWidget(self.btn)
        # layout2.addWidget(self.label)
        # layout2.addWidget(self.negativeBtn)
        # layout.addLayout(layout2)
        # self.setLayout(layout)
        self.resize(400,200)

        layout = QHBoxLayout()
        v2_layout = QVBoxLayout()
        v_layout = QVBoxLayout()
        self.pixmap = QPixmap()
        self.scaled = ""

        self.image_name = QLineEdit("Image name with .jpg at end")
        self.label = QLabel()
        self.blank_label = QLabel()
        self.browse_btn = QPushButton("Browse...", self)
        self.browse_btn.setFixedSize(70,25)
        # self.browse_btn.setStyleSheet("QPushButton:pressed {background-color : red;}")
        self.browse_btn.setStyleSheet("border-radius : 5; border : 2px solid grey")
        self.save_btn = QPushButton("Save")
        self.save_btn.setFixedSize(70,25)
        self.save_btn.setStyleSheet("border-radius : 5; border : 2px solid grey")
        # self.save_btn.setStyleSheet("QPushButton:pressed {background-color : red;}")
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
        self.b7 = QPushButton("Random Img")
        self.b7.setFixedSize(90,25)
        self.b8 = QPushButton("Small")
        self.b8.setFixedSize(70,25)
        self.b9 = QPushButton("Medium")
        self.b9.setFixedSize(70,25)
        self.b10 = QPushButton("Large")
        self.b10.setFixedSize(70,25)
        self.b11 = QPushButton("Undo")
        self.b11.setFixedSize(70,25)

        h1_layout = QHBoxLayout()
        h1_layout.addWidget(self.b1)
        h1_layout.addWidget(self.b2)

        h2_layout = QHBoxLayout()
        h2_layout.addWidget(self.b3)
        h2_layout.addWidget(self.b4)

        h3_layout = QHBoxLayout()
        h3_layout.addWidget(self.b5)
        h3_layout.addWidget(self.b6)

        h4_layout = QHBoxLayout()
        h4_layout.addWidget(self.b7)
        h4_layout.addWidget(self.b8)

        h5_layout = QHBoxLayout()
        h5_layout.addWidget(self.b9)
        h5_layout.addWidget(self.b10)

        h6_layout = QHBoxLayout()
        h6_layout.addWidget(self.b11)

        v2_layout.addWidget(self.label)
        v2_layout.addWidget(self.blank_label)
        v2_layout.addWidget(self.browse_btn)
        v2_layout.addWidget(self.image_name)
        v2_layout.addWidget(self.save_btn)
        
        v_layout.addLayout(h1_layout)
        v_layout.addLayout(h2_layout)
        v_layout.addLayout(h3_layout)
        v_layout.addLayout(h4_layout)
        v_layout.addLayout(h5_layout)
        v_layout.addLayout(h6_layout)
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
        self.b7.clicked.connect(self.openRandomImage)
        self.b8.clicked.connect(self.scaleSmall)
        self.b9.clicked.connect(self.scaleMedium)
        self.b10.clicked.connect(self.scaleLarge)
        self.save_btn.clicked.connect(self.saveImage)
        self.b11.clicked.connect(self.undo)

    def getImageFile(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.jpg *.png)")
        # , _ allows us to get the file name not the path
        print(self.filename)
        image = QPixmap(self.filename)
        image = image.scaled(300, 300, Qt.KeepAspectRatio)
        self.label.setPixmap(image)
        self.img = Image.open(self.filename)
        self.saved_img = self.filename
        self.saved_qim = ImageQt(self.img)
        self.image_type = "directory"
    def openGrayscale(self):
        grayscale_list = [ ((a[0]+a[1]+a[2])//3, ) * 3 for a in self.img.getdata() ]
        self.img.putdata(grayscale_list)
        qim = ImageQt(self.img)
        self.pixmap = QPixmap.fromImage(qim)
        if self.scaled == "small":
            self.pixmap = self.pixmap.scaled(200,200, Qt.KeepAspectRatio)
        elif self.scaled == "large":
            self.pixmap = self.pixmap.scaled(400,400, Qt.KeepAspectRatio)
        else:
            self.pixmap = self.pixmap.scaled(300,300, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def openNegative(self):
        negative_list = [ (255-p[0], 255-p[1], 255-p[2]) for p in self.img.getdata() ]
        self.img.putdata(negative_list)
        qim = ImageQt(self.img)
        self.pixmap = QPixmap.fromImage(qim)
        if self.scaled == "small":
            self.pixmap = self.pixmap.scaled(200,200, Qt.KeepAspectRatio)
        elif self.scaled == "large":
            self.pixmap = self.pixmap.scaled(400,400, Qt.KeepAspectRatio)
        else:
            self.pixmap = self.pixmap.scaled(300,300, Qt.KeepAspectRatio)
        # self.pixmap = self.pixmap.scaled(300, 300, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def openSepia(self):
        sepia_list = [ (int(p[0]*1.1), p[1], int(p[2]*.9)) if p[0] < 63 else (int(p[0]*1.15), p[1], int(p[2]*.85)) if p[0] > 62 and p[0] < 192 else (int(p[0]*1.08), p[1], int(p[2]*.5)) for p in self.img.getdata()]
        self.img.putdata(sepia_list)
        qim = ImageQt(self.img)
        self.pixmap = QPixmap.fromImage(qim)
        if self.scaled == "small":
            self.pixmap = self.pixmap.scaled(200,200, Qt.KeepAspectRatio)
        elif self.scaled == "large":
            self.pixmap = self.pixmap.scaled(400,400, Qt.KeepAspectRatio)
        else:
            self.pixmap = self.pixmap.scaled(300,300, Qt.KeepAspectRatio)
        # self.pixmap = self.pixmap.scaled(300, 300, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def openWarm(self):
        warm_list = [ (int(p[0] * 1.2), p[1], int(p[2] * .8)) for p in self.img.getdata() ]
        self.img.putdata(warm_list)
        qim = ImageQt(self.img)
        self.pixmap = QPixmap.fromImage(qim)
        if self.scaled == "small":
            self.pixmap = self.pixmap.scaled(200,200, Qt.KeepAspectRatio)
        elif self.scaled == "large":
            self.pixmap = self.pixmap.scaled(400,400, Qt.KeepAspectRatio)
        else:
            self.pixmap = self.pixmap.scaled(300,300, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def openCool(self):
        cool_list = [ (int(p[0] * .8), p[1], int(p[2] * 1.2)) for p in self.img.getdata() ]
        self.img.putdata(cool_list)
        qim = ImageQt(self.img)
        self.pixmap = QPixmap.fromImage(qim)

        if self.scaled == "small":
            self.pixmap = self.pixmap.scaled(200,200, Qt.KeepAspectRatio)
        elif self.scaled == "large":
            self.pixmap = self.pixmap.scaled(400,400, Qt.KeepAspectRatio)
        else:
            self.pixmap = self.pixmap.scaled(300,300, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def openLark(self):
        lark_list = [ (int(p[0] * 1.2), int(p[1]*.9), int(p[2] * .8)) for p in self.img.getdata() ]
        # infarred_list = [ (int(p[0] * .5), int(p[1]*.2), int(p[2] * .5)) for p in img.getdata() ]
        # thermal_list = [ (int(p[0] * .5), int(p[1]*.5), int(p[2] * 1.5)) for p in img.getdata() ]
        self.img.putdata(lark_list)
        qim = ImageQt(self.img)
        self.pixmap = QPixmap.fromImage(qim)
        if self.scaled == "small":
            self.pixmap = self.pixmap.scaled(200,200, Qt.KeepAspectRatio)
        elif self.scaled == "large":
            self.pixmap = self.pixmap.scaled(400,400, Qt.KeepAspectRatio)
        else:
            self.pixmap = self.pixmap.scaled(300,300, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def saveImage(self):
        self.img.save(self.image_name.text())
    def openRandomImage(self):
        self.image_type = "random"
        img = requests.get("https://picsum.photos/200/300")
        self.img = Image.open(BytesIO(img.content))
        self.saved_img = BytesIO(img.content)
        self.saved_qim = ImageQt(self.img)
        self.pixmap.loadFromData(img.content)
        if self.scaled == "small":
            self.pixmap = self.pixmap.scaled(200,200, Qt.KeepAspectRatio)
        elif self.scaled == "large":
            self.pixmap = self.pixmap.scaled(400,400, Qt.KeepAspectRatio)
        else:
            self.pixmap = self.pixmap.scaled(300,300, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def scaleSmall(self):
        self.scaled = "small"
        self.pixmap = self.pixmap.scaled(200,200, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def scaleMedium(self):
        self.scaled = "medium"
        self.pixmap = self.pixmap.scaled(300,300, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def scaleLarge(self):
        self.scaled = "large"
        self.pixmap = self.pixmap.scaled(400,400, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def undo(self):
        self.pixmap = QPixmap.fromImage(self.saved_qim)
        self.img = Image.open(self.saved_img)
        if self.scaled == "small":
            self.pixmap = self.pixmap.scaled(200,200, Qt.KeepAspectRatio)
        elif self.scaled == "large":
            self.pixmap = self.pixmap.scaled(400,400, Qt.KeepAspectRatio)
        else:
            self.pixmap = self.pixmap.scaled(300,300, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())