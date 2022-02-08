from PyDesing.first_task_design import Ui_MainWindow
from constans import *

import os
import sys
import requests
from io import BytesIO

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class YandexMap(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.zoom = 0.1  # map zoom
        self.cords_long = 37.61
        self.cords_width = 55.75
        self.layer = "map"  # map layout
        self.setupUi(self)  # load design
        self.show_map()  # show map with start cords
        self.setFocusPolicy(Qt.StrongFocus)  # for working arrows
        self.btn_show.clicked.connect(self.change_conditions)
        self.rbtn_map.clicked.connect(self.change_conditions)
        self.rbtn_sat.clicked.connect(self.change_conditions)
        self.rbtn_skl.clicked.connect(self.change_conditions)

    def change_conditions(self):
        if self.sender() == self.rbtn_map:
            self.layer = "map"
        if self.sender() == self.rbtn_sat:
            self.layer = "sat"
        if self.sender() == self.rbtn_skl:
            self.layer = "sat,skl"
        if self.sender() == self.btn_show:
            self.cords_long, self.cords_width = self.dsp_long.value(), self.dsp_width.value()  # update cords
        self.show_map()

    def show_map(self):
        map_params = {
            "ll": f"{self.cords_long},{self.cords_width}",
            "l": self.layer,
            "size": f"{WIDTH},{HEIGHT}",
            "spn": f"{self.zoom},{self.zoom}"}
        response = requests.get(MAP_API_SERVER, params=map_params)
        pixmap = QPixmap()  # container for map
        expansion = "JPEG"  # image expansion
        if self.layer == "map":
            expansion = "PNG"  # if we have map image will be PNG
        pixmap.loadFromData(BytesIO(response.content).read(), expansion)  # save image to pixmap from RAM
        self.lbl_map.setPixmap(pixmap)  # load map to label

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in {Qt.Key_PageUp, Qt.Key_PageDown}:
            # we will change value to 50%;  max value is (90 - |width| + 10)
            # because this is the edge of the map and 10 for zooming another part of the map
            if event.key() == Qt.Key_PageUp:
                self.zoom = min(90 - abs(self.dsp_width.value()) + 10, self.zoom + self.zoom * 0.5)
            if event.key() == Qt.Key_PageDown:
                self.zoom = max(self.zoom - self.zoom * 0.5, 0.0001)
        if event.key() in {Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right}:
            # moving map using arrows
            if event.key() == Qt.Key_Up:
                self.cords_width = min(85, self.cords_width + self.zoom)
                self.dsp_width.setValue(self.cords_width)
            if event.key() == Qt.Key_Down:
                self.cords_width = max(-85, self.cords_width - self.zoom)
                self.dsp_width.setValue(self.cords_width)
            if event.key() == Qt.Key_Left:
                self.cords_long -= self.zoom
                if self.cords_long < -180:
                    self.cords_long = 180 + (self.cords_long + 180)
                self.dsp_long.setValue(self.cords_long)
            if event.key() == Qt.Key_Right:
                self.cords_long += self.zoom
                if self.cords_long > 180:
                    self.cords_long = -180 + (self.cords_long - 180)
                self.dsp_long.setValue(self.cords_long)
        self.show_map()  # change and repaint map


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YandexMap()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
