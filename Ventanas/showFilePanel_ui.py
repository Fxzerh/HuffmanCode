# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'showFilePanel.ui'
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
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_showFile(object):
    def setupUi(self, showFile):
        if not showFile.objectName():
            showFile.setObjectName(u"showFile")
        showFile.resize(1280, 720)
        self.back_btn = QPushButton(showFile)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(10, 10, 81, 26))
        self.label_2 = QLabel(showFile)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 30, 451, 51))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)
        self.tableFile = QTableWidget(showFile)
        if (self.tableFile.columnCount() < 2):
            self.tableFile.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableFile.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableFile.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableFile.setObjectName(u"tableFile")
        self.tableFile.setGeometry(QRect(30, 140, 461, 521))
        self.textFileO = QTextEdit(showFile)
        self.textFileO.setObjectName(u"textFileO")
        self.textFileO.setGeometry(QRect(550, 140, 691, 241))
        self.textFileC = QTextEdit(showFile)
        self.textFileC.setObjectName(u"textFileC")
        self.textFileC.setGeometry(QRect(550, 420, 691, 241))
        self.label = QLabel(showFile)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 110, 151, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label_3 = QLabel(showFile)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(560, 110, 151, 31))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(showFile)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(560, 390, 181, 31))
        self.label_4.setFont(font1)

        self.retranslateUi(showFile)

        QMetaObject.connectSlotsByName(showFile)
    # setupUi

    def retranslateUi(self, showFile):
        showFile.setWindowTitle(QCoreApplication.translate("showFile", u"Form", None))
        self.back_btn.setText(QCoreApplication.translate("showFile", u"Volver", None))
        self.label_2.setText(QCoreApplication.translate("showFile", u"Comparar Archivos", None))
        ___qtablewidgetitem = self.tableFile.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("showFile", u"Archivo", None))
        ___qtablewidgetitem1 = self.tableFile.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("showFile", u"Tama\u00f1o", None))
        self.label.setText(QCoreApplication.translate("showFile", u"Seleccionar Archivo:", None))
        self.label_3.setText(QCoreApplication.translate("showFile", u"Contenido Original:", None))
        self.label_4.setText(QCoreApplication.translate("showFile", u"Contenido Comprimido:", None))
    # retranslateUi

