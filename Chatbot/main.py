from PyQt6.QtWidgets import QApplication, QPushButton, QLineEdit, QMainWindow, QTextEdit
import sys

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 600)

        #Adding chatarea
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        #Adding input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        #Adding Send Button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)

        self.show()


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())