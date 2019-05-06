from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import sys
from rate import *


class ABVARA(QWidget):
    def __init__(self):
        super().__init__()

        self.xp = "No selection"
        self.pub = "No selection"

        self.y_layout = QVBoxLayout()                            # Parent (vertical) layout
        # self.y_layout.setAlignment(Qt.AlignCenter)
        self.y_layout.setSizeConstraint(QLayout.SetFixedSize)    # Layout will resize as widgets are added/removed

        self.intro_label = QLabel("Welcome to the AudioBook Voice Actor Rate Assistant!")

        self.about_you = QLabel("First, let's find out about you.")
        
        self.exp_prompt = QLabel("How experienced are you?")
        self.exp_box = QComboBox(self)
        self.exp_box.addItem("I'm just getting started")
        self.exp_box.addItem("Experienced voice actor")
        self.exp_box.activated[str].connect(self.xp_choice)
        
        self.publisher_label = QLabel("Is your client a small or large publisher?")
        self.pub_box = QComboBox(self)
        self.pub_box.addItem("Small publisher")
        self.pub_box.addItem("Medium/Large publisher")
        self.pub_box.activated[str].connect(self.pub_choice)

        self.submit_btn = QPushButton("Submit")
        self.submit_btn.setMaximumWidth(100)

        # Instantiate the UI
        self.create_ui()
        self.setWindowTitle("ABVARA")

    def create_ui(self):
        self.submit_btn.clicked.connect(lambda: self.submit())

        # Add widgets to layout
        self.y_layout.addWidget(self.intro_label)
        self.y_layout.addWidget(self.about_you)
        self.y_layout.addWidget(self.exp_prompt)
        self.y_layout.addWidget(self.exp_box)
        self.y_layout.addWidget(self.publisher_label)
        self.y_layout.addWidget(self.pub_box)
        self.y_layout.addWidget(self.submit_btn)

        # Add layout to UI
        self.setLayout(self.y_layout)

        # Make the UI visible
        self.show()

    def xp_choice(self, exp):
        # This callback function takes the input from exp_box and makes it the value for "xp"
        self.xp = exp

    def pub_choice(self, size):
        # This callback function takes the input from exp_box and makes it the value for "pub"
        self.pub = size

    def submit(self):
        calculator = Rate()
        calculator.rate_calculator(self.xp, self.pub)


# Start UI
if __name__ == '__main__':
    window = QApplication(sys.argv)
    ui = ABVARA()
    sys.exit(window.exec_())
