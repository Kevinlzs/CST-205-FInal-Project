import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QFileDialog, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a button and set its text
        self.select_photo_button = QPushButton("Select Photo")
        self.select_photo_button.clicked.connect(self.select_photo)

        # Create a save button
        self.save_button = QPushButton("Save Photo")
        self.save_button.clicked.connect(self.save_photo)
        self.save_button.setEnabled(False)  # Disable the button until an image is loaded

        # Create a label to display the photo
        self.photo_label = QLabel()
        self.photo_label.setAlignment(Qt.AlignCenter)

        # Create a label to display the image sizes
        self.size_label = QLabel()
        self.size_label.setAlignment(Qt.AlignCenter)

        # Create a vertical layout to contain the buttons
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.select_photo_button)
        button_layout.addWidget(self.save_button)
        button_layout.addStretch(1)

        # Create a vertical layout to contain the image and size label
        image_layout = QVBoxLayout()
        image_layout.addWidget(self.photo_label)
        image_layout.addWidget(self.size_label)

        # Create a horizontal layout to contain the button layout and image layout
        layout = QHBoxLayout()
        layout.addLayout(button_layout)
        layout.addStretch(1)
        layout.addLayout(image_layout)
        layout.addStretch(1)

        # Create a central widget to hold the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.pixmap = None  # To hold the QPixmap object

    def select_photo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "Images (*.png *.xpm *.jpg *.bmp *.gif);;All Files (*)", options=options)
        if file_name:
            # Load the image and resize if necessary
            original_pixmap = QPixmap(file_name)
            self.pixmap = original_pixmap.copy()
            max_size = 500  # Maximum size for width or height
            if self.pixmap.width() > max_size or self.pixmap.height() > max_size:
                self.pixmap = self.pixmap.scaled(max_size, max_size, Qt.KeepAspectRatio)

            # Set the photo label's pixmap to the resized photo
            self.photo_label.setPixmap(self.pixmap)
            self.save_button.setEnabled(True)  # Enable the save button

            # Display the original and resized image sizes
            self.size_label.setText(f'Original size: {original_pixmap.width()} x {original_pixmap.height()}\n'
                                    f'Resized size: {self.pixmap.width()} x {self.pixmap.height()}')

    def save_photo(self):
        if self.pixmap:
            file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                       "Images (*.png *.jpg *.bmp *.gif);;All Files (*)")
            if file_name:
                self.pixmap.save(file_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
