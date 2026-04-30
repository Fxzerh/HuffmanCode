# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'decompactFilePanel.ui'
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

class Ui_decompactFile(object):
    def setupUi(self, decompactFile):
        if not decompactFile.objectName():
            decompactFile.setObjectName(u"decompactFile")
        decompactFile.resize(1280, 720)
        self.decompact_btn = QPushButton(decompactFile)
        self.decompact_btn.setObjectName(u"decompact_btn")
        self.decompact_btn.setGeometry(QRect(240, 640, 151, 41))
        font = QFont()
        font.setPointSize(12)
        self.decompact_btn.setFont(font)
        self.tableFile = QTableWidget(decompactFile)
        if (self.tableFile.columnCount() < 2):
            self.tableFile.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableFile.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableFile.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableFile.setObjectName(u"tableFile")
        self.tableFile.setGeometry(QRect(30, 130, 571, 481))
        self.label_2 = QLabel(decompactFile)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 30, 451, 51))
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)
        self.textFile = QTextEdit(decompactFile)
        self.textFile.setObjectName(u"textFile")
        self.textFile.setGeometry(QRect(670, 130, 571, 481))
        self.back_btn = QPushButton(decompactFile)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(10, 10, 81, 26))
        self.label = QLabel(decompactFile)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 100, 151, 31))
        self.label.setFont(font)
        self.label_3 = QLabel(decompactFile)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(680, 100, 81, 31))
        self.label_3.setFont(font)

        self.retranslateUi(decompactFile)

        QMetaObject.connectSlotsByName(decompactFile)
    # setupUi

    def retranslateUi(self, decompactFile):
        decompactFile.setWindowTitle(QCoreApplication.translate("decompactFile", u"Form", None))
        self.decompact_btn.setText(QCoreApplication.translate("decompactFile", u"Descompactar", None))
        ___qtablewidgetitem = self.tableFile.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("decompactFile", u"Archivo", None))
        ___qtablewidgetitem1 = self.tableFile.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("decompactFile", u"Tama\u00f1o", None))
        self.label_2.setText(QCoreApplication.translate("decompactFile", u"Descompactar Archivo", None))
        self.back_btn.setText(QCoreApplication.translate("decompactFile", u"Volver", None))
        self.label.setText(QCoreApplication.translate("decompactFile", u"Seleccionar Archivo:", None))
        self.label_3.setText(QCoreApplication.translate("decompactFile", u"Contenido: ", None))
    # retranslateUi

