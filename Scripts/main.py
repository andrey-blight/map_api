from PyDesing.first_task_design import Ui_MainWindow
from constans import *

import os
import sys
import requests

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_show.clicked.connect(self.show_map)

    def show_map(self):
        # Собираем параметры для запроса к StaticMapsAPI:
        map_params = {
            "ll": ",".join(str(s) for s in [self.dsp_long.value(), self.dsp_width.value()]),
            "spn": ",".join(str(s) for s in SPN),
            "l": "map"}

        map_api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_api_server, params=map_params)

        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.lbl_map.setPixmap(QPixmap(self.map_file))

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
