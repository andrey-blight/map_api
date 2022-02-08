from PyDesing.first_task_design import Ui_MainWindow
from constans import *

import os
import sys
import requests
from io import BytesIO

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


class YandexMap(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.zoom = 12  # map zoom
        self.setupUi(self)  # load design
        self.show_map()  # show map with start cords
        self.btn_show.clicked.connect(self.show_map)

    def show_map(self):
        map_params = {
            "ll": ",".join(str(s) for s in [self.dsp_long.value(), self.dsp_width.value()]),
            "z": str(self.zoom),
            "size": f"{WIDTH},{HEIGHT}",
            "l": "map"}
        response = requests.get(MAP_API_SERVER, params=map_params)
        pixmap = QPixmap()  # container for map
        pixmap.loadFromData(BytesIO(response.content).read(), "PNG")  # save image to pixmap from RAM
        self.lbl_map.setPixmap(pixmap)  # load map to label

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_PageUp:
            self.zoom = min(17, self.zoom + 1)
            self.show_map()  # change zoom and repaint map
        if event.key() == Qt.Key_PageDown:
            self.zoom = max(self.zoom - 1, 0)
            self.show_map()  # change zoom and repaint map


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YandexMap()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
