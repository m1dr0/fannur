# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sumit-ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(571, 231)
        MainWindow.setStyleSheet(u"background-color: rgb(33, 33, 33)")
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.select_path_menu = QAction(MainWindow)
        self.select_path_menu.setObjectName(u"select_path_menu")
        self.action_SumIt = QAction(MainWindow)
        self.action_SumIt.setObjectName(u"action_SumIt")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 571, 191))
        self.label_filename_field = QLabel(self.groupBox)
        self.label_filename_field.setObjectName(u"label_filename_field")
        self.label_filename_field.setEnabled(False)
        self.label_filename_field.setGeometry(QRect(270, 30, 291, 21))
        self.label_filename_field.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: white;")
        self.pushButton_upload = QPushButton(self.groupBox)
        self.pushButton_upload.setObjectName(u"pushButton_upload")
        self.pushButton_upload.setGeometry(QRect(30, 30, 121, 24))
        self.checkBox_transcript = QCheckBox(self.groupBox)
        self.checkBox_transcript.setObjectName(u"checkBox_transcript")
        self.checkBox_transcript.setGeometry(QRect(30, 100, 111, 20))
        self.label_filename = QLabel(self.groupBox)
        self.label_filename.setObjectName(u"label_filename")
        self.label_filename.setGeometry(QRect(160, 32, 101, 16))
        self.checkBox_bulletpoint = QCheckBox(self.groupBox)
        self.checkBox_bulletpoint.setObjectName(u"checkBox_bulletpoint")
        self.checkBox_bulletpoint.setGeometry(QRect(30, 130, 111, 20))
        self.pushButton_start = QPushButton(self.groupBox)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setGeometry(QRect(450, 120, 110, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 571, 33))
        self.menu_settings = QMenu(self.menubar)
        self.menu_settings.setObjectName(u"menu_settings")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu_settings.addAction(self.select_path_menu)
        self.menu_2.addAction(self.action_SumIt)
        self.menu_2.addAction(self.action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SumIt", None))
        self.select_path_menu.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0443\u0442\u044c \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))       
        self.action_SumIt.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430 \u043f\u043e SumIt", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label_filename_field.setText("")
        self.pushButton_upload.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
#if QT_CONFIG(statustip)
        self.checkBox_transcript.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.checkBox_transcript.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u043d\u0441\u043a\u0440\u0438\u043f\u0446\u0438\u044f", None))
        self.label_filename.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430:", None))
        self.checkBox_bulletpoint.setText(QCoreApplication.translate("MainWindow", u"Bullet point", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.menu_settings.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi