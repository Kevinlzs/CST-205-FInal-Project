import sys
from PIL import Image
from PIL.ImageQt import ImageQt
import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, 
                                QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QFileDialog)

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QDesktopServices, QImageReader

from io import BytesIO
import requests, json
from pprint import pprint

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800,800)  
        self.setWindowTitle("Photoshop for Dummies")  
        self.is_dark_mode = False
        # Main layout
        main_layout = QHBoxLayout()

        # Layout for buttons
        button_layout = QVBoxLayout()
        button_layout.setAlignment(Qt.AlignTop)
        
        # Widgets and buttons 
        self.pixmap = QPixmap()
        self.scaled = ""
        self.size_label = QLabel()
        self.label = QLabel()
        self.blank_label = QLabel()
        self.browse_btn = QPushButton("Select Photo")
        self.save_btn = QPushButton("Save Photo")
        self.dark_mode_btn = QPushButton("Dark Mode")  
        self.label.setAlignment(Qt.AlignCenter)
        self.browse_btn.setFixedSize(90,25)
        self.browse_btn.setStyleSheet("border-radius : 5; border : 2px solid grey")
        self.save_btn.setFixedSize(90,25)
        self.save_btn.setStyleSheet("border-radius : 5; border : 2px solid grey")
        self.dark_mode_btn.setFixedSize(90,25)
        self.dark_mode_btn.setStyleSheet("border-radius : 5; border : 2px solid grey")
        self.save_btn.setEnabled(False)
        button_layout.addWidget(self.browse_btn)
        button_layout.addWidget(self.save_btn)
        button_layout.addStretch()  
        button_layout.addWidget(self.dark_mode_btn)  

        self.buttons = []
        for i, name in enumerate(["Negative", "Grey", "Sepia", "Warm", "Cool", "Lark", "Random Img", "Small", "Medium", "Large", "Undo"]):
            button = QPushButton(name)
            button.setFixedSize(90,25)
            button.setStyleSheet("border-radius : 5; border : 2px solid grey")
            self.buttons.append(button)
            button_layout.addWidget(button)

        # Image layout
        image_layout = QVBoxLayout()
        image_layout.setAlignment(Qt.AlignCenter)

        # Spacers for image layout
        image_top_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        image_bot_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Add spacers and label to image layout
        image_layout.addItem(image_top_spacer)
        image_layout.addWidget(self.label)
        image_layout.addWidget(self.size_label)
        image_layout.addItem(image_bot_spacer)

        # Adding button layout and image layout to the main layout
        main_layout.addLayout(button_layout)
        main_layout.addLayout(image_layout)
        self.setLayout(main_layout)

        # Connecting the functions to their corresponding buttons when clicked
        self.browse_btn.clicked.connect(self.getImageFile)
        self.save_btn.clicked.connect(self.saveImage)
        self.dark_mode_btn.clicked.connect(self.toggleDarkMode)  
        self.buttons[0].clicked.connect(self.openNegative)
        self.buttons[1].clicked.connect(self.openGrayscale)
        self.buttons[2].clicked.connect(self.openSepia)
        self.buttons[3].clicked.connect(self.openWarm)
        self.buttons[4].clicked.connect(self.openCool)
        self.buttons[5].clicked.connect(self.openLark)
        self.buttons[6].clicked.connect(self.openRandomImage)
        self.buttons[7].clicked.connect(self.scaleSmall)
        self.buttons[8].clicked.connect(self.scaleMedium)
        self.buttons[9].clicked.connect(self.scaleLarge)
        self.buttons[10].clicked.connect(self.undo)


    def getImageFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "Images (*.png *.xpm *.jpg *.bmp *.gif);;All Files (*)", options=options)
        if self.filename:
            # Load the image and resize if necessary
            self.original_pixmap = QPixmap(self.filename)
            self.pixmap = QPixmap(self.filename)
            max_size = 300  # Maximum size for width or height
            if self.pixmap.width() > max_size or self.pixmap.height() > max_size:
                self.pixmap = self.pixmap.scaled(max_size, max_size, Qt.KeepAspectRatio)

            # Set the photo label's pixmap to the resized photo
            self.label.setPixmap(self.pixmap)
            self.save_btn.setEnabled(True)  

            # Display the original and resized image sizes
            self.size_label.setText(f'Original size: {self.original_pixmap.width()} x {self.original_pixmap.height()}\n'
                                    f'Resized size: {self.pixmap.width()} x {self.pixmap.height()}')
            self.label.setPixmap(self.pixmap)
            self.img = Image.open(self.filename)
            self.saved_img = self.filename
            self.saved_qim = ImageQt(self.img)
            self.image_type = "directory"

        # self.filename, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.jpg *.png)")
        # , _ allows us to get the file name not the path
        # print(self.filename)
        # image = QPixmap(self.filename)
        # image = image.scaled(300, 300, Qt.KeepAspectRatio)
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
        if self.pixmap:
            self.filename, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                        "Images (*.png *.jpg *.bmp *.gif);;All Files (*)")
            if self.filename:
                self.pixmap.save(self.filename)

    def openRandomImage(self):
        self.image_type = "random"
        img = requests.get("https://picsum.photos/200/300")
        self.img = Image.open(BytesIO(img.content))

        if self.img:
            self.save_btn.setEnabled(True)
            self.saved_img = BytesIO(img.content)
            self.saved_qim = ImageQt(self.img)
            self.pixmap.loadFromData(img.content)
            self.original_pixmap = self.pixmap
            if self.scaled == "small":
                self.pixmap = self.pixmap.scaled(200,200, Qt.KeepAspectRatio)
            elif self.scaled == "large":
                self.pixmap = self.pixmap.scaled(400,400, Qt.KeepAspectRatio)
            else:
                self.pixmap = self.pixmap.scaled(300,300, Qt.KeepAspectRatio)
            self.label.setPixmap(self.pixmap)
            self.size_label.setText(f'Original size: {self.original_pixmap.width()} x {self.original_pixmap.height()}\n'
                                    f'Resized size: {self.pixmap.width()} x {self.pixmap.height()}')
    def scaleSmall(self):
        self.scaled = "small"
        self.pixmap = self.pixmap.scaled(200,200, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
        self.size_label.setText(f'Original size: {self.original_pixmap.width()} x {self.original_pixmap.height()}\n'
                                    f'Resized size: {self.pixmap.width()} x {self.pixmap.height()}')
    def scaleMedium(self):
        self.scaled = "medium"
        self.pixmap = self.pixmap.scaled(300,300, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
        self.size_label.setText(f'Original size: {self.original_pixmap.width()} x {self.original_pixmap.height()}\n'
                                    f'Resized size: {self.pixmap.width()} x {self.pixmap.height()}')
    def scaleLarge(self):
        self.scaled = "large"
        self.pixmap = self.pixmap.scaled(400,400, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
        self.size_label.setText(f'Original size: {self.original_pixmap.width()} x {self.original_pixmap.height()}\n'
                                    f'Resized size: {self.pixmap.width()} x {self.pixmap.height()}')
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

    def toggleDarkMode(self):
        if self.is_dark_mode:
            # Switch to light mode
            self.setStyleSheet("")  # Remove any custom styles to revert to default
        else:
            # Switch to dark mode
            dark_stylesheet = """
                QWidget {
                    background-color: #222222;
                    color: #FFFFFF;
                }

                QPushButton {
                    background-color: #444444;
                    color: #FFFFFF;
                }

                /* Add more style rules for other widgets as needed */
            """
            self.setStyleSheet(dark_stylesheet)

        self.is_dark_mode = not self.is_dark_mode





app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Create a button and set its text
#         self.select_photo_button = QPushButton("Select Photo")
#         self.select_photo_button.clicked.connect(self.select_photo)

#         # Create a save button
#         self.save_button = QPushButton("Save Photo")
#         self.save_button.clicked.connect(self.save_photo)
#         self.save_button.setEnabled(False)  # Disable the button until an image is loaded

#         # Create a label to display the photo
#         self.photo_label = QLabel()
#         self.photo_label.setAlignment(Qt.AlignCenter)

#         # Create a label to display the image sizes
#         self.size_label = QLabel()
#         self.size_label.setAlignment(Qt.AlignCenter)

#         # Create a vertical layout to contain the buttons
#         button_layout = QVBoxLayout()
#         button_layout.addWidget(self.select_photo_button)
#         button_layout.addWidget(self.save_button)
#         button_layout.addStretch(1)

#         # Create a vertical layout to contain the image and size label
#         image_layout = QVBoxLayout()
#         image_layout.addWidget(self.photo_label)
#         image_layout.addWidget(self.size_label)

#         # Create a horizontal layout to contain the button layout and image layout
#         layout = QHBoxLayout()
#         layout.addLayout(button_layout)
#         layout.addStretch(1)
#         layout.addLayout(image_layout)
#         layout.addStretch(1)

#         # Create a central widget to hold the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         self.pixmap = None  # To hold the QPixmap object

#     def select_photo(self):
#         options = QFileDialog.Options()
#         options |= QFileDialog.ReadOnly
#         file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
#                                                    "Images (*.png *.xpm *.jpg *.bmp *.gif);;All Files (*)", options=options)
#         if file_name:
#             # Load the image and resize if necessary
#             original_pixmap = QPixmap(file_name)
#             self.pixmap = original_pixmap.copy()
#             max_size = 500  # Maximum size for width or height
#             if self.pixmap.width() > max_size or self.pixmap.height() > max_size:
#                 self.pixmap = self.pixmap.scaled(max_size, max_size, Qt.KeepAspectRatio)

#             # Set the photo label's pixmap to the resized photo
#             self.photo_label.setPixmap(self.pixmap)
#             self.save_button.setEnabled(True)  # Enable the save button

#             # Display the original and resized image sizes
#             self.size_label.setText(f'Original size: {original_pixmap.width()} x {original_pixmap.height()}\n'
#                                     f'Resized size: {self.pixmap.width()} x {self.pixmap.height()}')

#     def save_photo(self):
#         if self.pixmap:
#             file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
#                                                        "Images (*.png *.jpg *.bmp *.gif);;All Files (*)")
#             if file_name:
#                 self.pixmap.save(file_name)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())