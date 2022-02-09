from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 470)
        MainWindow.setMinimumSize(QSize(800, 470))
        MainWindow.setMaximumSize(QSize(800, 470))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_map = QLabel(self.centralwidget)
        self.lbl_map.setObjectName(u"lbl_map")
        self.lbl_map.setGeometry(QRect(180, 0, 600, 450))
        self.lbl_map.setMinimumSize(QSize(600, 450))
        self.lbl_map.setMaximumSize(QSize(600, 450))
        self.lbl_map.setFont(font)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(9, 9, 112, 368))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl1 = QLabel(self.layoutWidget)
        self.lbl1.setObjectName(u"lbl1")

        self.verticalLayout.addWidget(self.lbl1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl2 = QLabel(self.layoutWidget)
        self.lbl2.setObjectName(u"lbl2")

        self.horizontalLayout.addWidget(self.lbl2)

        self.dsp_width = QDoubleSpinBox(self.layoutWidget)
        self.dsp_width.setObjectName(u"dsp_width")
        self.dsp_width.setFocusPolicy(Qt.ClickFocus)
        self.dsp_width.setMinimum(-90.000000000000000)
        self.dsp_width.setMaximum(90.000000000000000)
        self.dsp_width.setValue(55.750000000000000)

        self.horizontalLayout.addWidget(self.dsp_width)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl3 = QLabel(self.layoutWidget)
        self.lbl3.setObjectName(u"lbl3")
        self.lbl3.setMaximumSize(QSize(50, 120))

        self.horizontalLayout_2.addWidget(self.lbl3)

        self.dsp_long = QDoubleSpinBox(self.layoutWidget)
        self.dsp_long.setObjectName(u"dsp_long")
        self.dsp_long.setFocusPolicy(Qt.ClickFocus)
        self.dsp_long.setMinimum(-180.000000000000000)
        self.dsp_long.setMaximum(180.000000000000000)
        self.dsp_long.setValue(37.609999999999999)

        self.horizontalLayout_2.addWidget(self.dsp_long)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lbl4 = QLabel(self.layoutWidget)
        self.lbl4.setObjectName(u"lbl4")

        self.verticalLayout.addWidget(self.lbl4)

        self.rbtn_map = QRadioButton(self.layoutWidget)
        self.rbtn_map.setObjectName(u"rbtn_map")
        self.rbtn_map.setFocusPolicy(Qt.NoFocus)
        self.rbtn_map.setChecked(True)

        self.verticalLayout.addWidget(self.rbtn_map)

        self.rbtn_sat = QRadioButton(self.layoutWidget)
        self.rbtn_sat.setObjectName(u"rbtn_sat")
        self.rbtn_sat.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.rbtn_sat)

        self.rbtn_skl = QRadioButton(self.layoutWidget)
        self.rbtn_skl.setObjectName(u"rbtn_skl")
        self.rbtn_skl.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.rbtn_skl)

        self.btn_show = QPushButton(self.layoutWidget)
        self.btn_show.setObjectName(u"btn_show")
        self.btn_show.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout.addWidget(self.btn_show)

        self.le_obj = QLineEdit(self.layoutWidget)
        self.le_obj.setObjectName(u"le_obj")
        font1 = QFont()
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.le_obj.setFont(font1)
        self.le_obj.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout.addWidget(self.le_obj)

        self.lbl5 = QLabel(self.layoutWidget)
        self.lbl5.setObjectName(u"lbl5")

        self.verticalLayout.addWidget(self.lbl5)

        self.le_obj_address = QTextEdit(self.layoutWidget)
        self.le_obj_address.setObjectName(u"le_obj_address")
        self.le_obj_address.setFocusPolicy(Qt.NoFocus)
        self.le_obj_address.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_obj_address)

        self.btn_find_obj = QPushButton(self.layoutWidget)
        self.btn_find_obj.setObjectName(u"btn_find_obj")
        self.btn_find_obj.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout.addWidget(self.btn_find_obj)

        self.btn_clear = QPushButton(self.layoutWidget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout.addWidget(self.btn_clear)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u042f\u043d\u0434\u0435\u043a\u0441 \u043a\u0430\u0440\u0442\u044b",
                                                             None))
        self.lbl_map.setText("")
        self.lbl1.setText(QCoreApplication.translate("MainWindow",
                                                     u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b",
                                                     None))
        self.lbl2.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u043e\u0442\u0430", None))
        self.lbl3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430", None))
        self.lbl4.setText(QCoreApplication.translate("MainWindow",
                                                     u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0441\u043b\u043e\u0439",
                                                     None))
        self.rbtn_map.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0445\u0435\u043c\u0430", None))
        self.rbtn_sat.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0443\u0442\u043d\u0438\u043a", None))
        self.rbtn_skl.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0438\u0431\u0440\u0438\u0434", None))
        self.btn_show.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u041e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c \u043a\u0430\u0440\u0442\u0443",
                                                         None))
        self.le_obj.setText("")
        self.le_obj.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                  u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u0431\u044a\u0435\u043a\u0442",
                                                                  None))
        self.lbl5.setText(QCoreApplication.translate("MainWindow",
                                                     u"\u0410\u0434\u0440\u0435\u0441 \u043e\u0431\u044a\u0435\u043a\u0442\u0430:",
                                                     None))
        self.btn_find_obj.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u041f\u043e\u0438\u0441\u043a \u043e\u0431\u044a\u0435\u043a\u0442\u0430",
                                                             None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow",
                                                          u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043f\u043e\u0438\u0441\u043a",
                                                          None))
    # retranslateUi
