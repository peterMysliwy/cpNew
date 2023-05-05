from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from UIs.ui_measurement import Ui_measurement


class Loader(QWidget, Ui_measurement):
    def __init__(self, parent, name):
        super().__init__()
        # print(f'loader name -> {name}')
        self.setupUi(self)
        self.description.setText(name)
        self.description.setAlignment(Qt.AlignmentFlag.AlignCenter)

