import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a button and set its text
        self.select_photo_button = QPushButton("Select Photo")
        self.select_photo_button.clicked.connect(self.select_photo)

        # Create a label to display the photo
        self.photo_label = QLabel()

        # Create a vertical layout to contain the button and label
        layout = QVBoxLayout()
        layout.addWidget(self.select_photo_button)
        layout.addWidget(self.photo_label)

        # Create a central widget to hold the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def select_photo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "Images (*.png *.xpm *.jpg *.bmp *.gif);;All Files (*)", options=options)
        if file_name:
            # Set the photo label's pixmap to the selected photo
            pixmap = QPixmap(file_name)
            self.photo_label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
