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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

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
        self.refresh_btn = QPushButton(estadisticas)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.setGeometry(QRect(1170, 20, 90, 30))
        self.label_info = QLabel(estadisticas)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(30, 100, 1220, 30))
        self.label_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.statsTable = QTableWidget(estadisticas)
        self.statsTable.setObjectName(u"statsTable")
        self.statsTable.setGeometry(QRect(30, 140, 1220, 520))

        self.retranslateUi(estadisticas)

        QMetaObject.connectSlotsByName(estadisticas)
    # setupUi

    def retranslateUi(self, estadisticas):
        estadisticas.setWindowTitle(QCoreApplication.translate("estadisticas", u"Form", None))
        self.back_btn.setText(QCoreApplication.translate("estadisticas", u"Volver", None))
        self.label_2.setText(QCoreApplication.translate("estadisticas", u"Estad\u00edsticas del Archivo", None))
        self.refresh_btn.setText(QCoreApplication.translate("estadisticas", u"Actualizar", None))
        self.label_info.setText(QCoreApplication.translate("estadisticas", u"Seleccione un archivo para ver la comparaci\u00f3n de tama\u00f1os.", None))
    # retranslateUi

