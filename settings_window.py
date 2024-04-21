# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings-window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(632, 92)
        self.centralwidget = QWidget(SettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_pathselection = QPushButton(self.centralwidget)
        self.pushButton_pathselection.setObjectName(u"pushButton_pathselection")
        self.pushButton_pathselection.setGeometry(QRect(10, 30, 121, 24))
        self.label_path = QLabel(self.centralwidget)
        self.label_path.setObjectName(u"label_path")
        self.label_path.setGeometry(QRect(140, 32, 131, 20))
        self.label_path_field = QLabel(self.centralwidget)
        self.label_path_field.setObjectName(u"label_path_field")
        self.label_path_field.setEnabled(False)
        self.label_path_field.setGeometry(QRect(270, 30, 351, 21))
        self.label_path_field.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: white;")
        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0443\u0442\u044c \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0438", None))
        self.pushButton_pathselection.setText(QCoreApplication.translate("SettingsWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0443\u0442\u044c", None))
        self.label_path.setText(QCoreApplication.translate("SettingsWindow", u"\u041f\u0443\u0442\u044c \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f:", None))
        self.label_path_field.setText("")
    # retranslateUi