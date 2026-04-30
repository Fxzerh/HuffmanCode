# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'estadisticasPanel.ui'
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
    QWidget)

class Ui_estadisticas(object):
    def setupUi(self, estadisticas):
        if not estadisticas.objectName():
            estadisticas.setObjectName(u"estadisticas")
        estadisticas.resize(1280, 720)
        self.back_btn = QPushButton(estadisticas)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(10, 10, 81, 26))
        self.label_2 = QLabel(estadisticas)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 30, 451, 51))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)

        self.retranslateUi(estadisticas)

        QMetaObject.connectSlotsByName(estadisticas)
    # setupUi

    def retranslateUi(self, estadisticas):
        estadisticas.setWindowTitle(QCoreApplication.translate("estadisticas", u"Form", None))
        self.back_btn.setText(QCoreApplication.translate("estadisticas", u"Volver", None))
        self.label_2.setText(QCoreApplication.translate("estadisticas", u"Estaditicas del Archivo", None))
    # retranslateUi

