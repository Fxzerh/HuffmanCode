# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadFilePanel.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_loadFile(object):
    def setupUi(self, loadFile):
        if not loadFile.objectName():
            loadFile.setObjectName(u"loadFile")
        loadFile.resize(1280, 720)
        self.back_btn = QPushButton(loadFile)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(10, 10, 81, 26))
        self.label_2 = QLabel(loadFile)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(480, 30, 311, 51))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)
        self.buscarFile_btn = QPushButton(loadFile)
        self.buscarFile_btn.setObjectName(u"buscarFile_btn")
        self.buscarFile_btn.setGeometry(QRect(520, 120, 231, 51))
        font1 = QFont()
        font1.setBold(True)
        self.buscarFile_btn.setFont(font1)
        self.showFile = QTextEdit(loadFile)
        self.showFile.setObjectName(u"showFile")
        self.showFile.setGeometry(QRect(90, 250, 1091, 421))
        self.label = QLabel(loadFile)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 210, 241, 41))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label.setFont(font2)

        self.retranslateUi(loadFile)

        QMetaObject.connectSlotsByName(loadFile)
    # setupUi

    def retranslateUi(self, loadFile):
        loadFile.setWindowTitle(QCoreApplication.translate("loadFile", u"Form", None))
        self.back_btn.setText(QCoreApplication.translate("loadFile", u"Volver", None))
        self.label_2.setText(QCoreApplication.translate("loadFile", u"Cargar Archivo", None))
        self.buscarFile_btn.setText(QCoreApplication.translate("loadFile", u"Buscar Archivo", None))
        self.label.setText(QCoreApplication.translate("loadFile", u"Contenido del archivo:", None))
    # retranslateUi

