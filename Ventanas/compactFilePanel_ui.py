# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'compactFilePanel.ui'
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

class Ui_compactFile(object):
    def setupUi(self, compactFile):
        if not compactFile.objectName():
            compactFile.setObjectName(u"compactFile")
        compactFile.resize(1280, 720)
        self.tableFile = QTableWidget(compactFile)
        if (self.tableFile.columnCount() < 2):
            self.tableFile.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableFile.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableFile.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableFile.setObjectName(u"tableFile")
        self.tableFile.setGeometry(QRect(30, 130, 571, 481))
        self.label_2 = QLabel(compactFile)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(430, 30, 411, 51))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)
        self.back_btn = QPushButton(compactFile)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(10, 10, 81, 26))
        self.textFile = QTextEdit(compactFile)
        self.textFile.setObjectName(u"textFile")
        self.textFile.setGeometry(QRect(670, 130, 571, 481))
        self.compact_btn = QPushButton(compactFile)
        self.compact_btn.setObjectName(u"compact_btn")
        self.compact_btn.setGeometry(QRect(240, 640, 151, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.compact_btn.setFont(font1)
        self.label = QLabel(compactFile)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 100, 151, 31))
        self.label.setFont(font1)
        self.label_3 = QLabel(compactFile)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(680, 100, 91, 31))
        self.label_3.setFont(font1)

        self.retranslateUi(compactFile)

        QMetaObject.connectSlotsByName(compactFile)
    # setupUi

    def retranslateUi(self, compactFile):
        compactFile.setWindowTitle(QCoreApplication.translate("compactFile", u"Form", None))
        ___qtablewidgetitem = self.tableFile.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("compactFile", u"Archivo", None))
        ___qtablewidgetitem1 = self.tableFile.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("compactFile", u"Tama\u00f1o", None))
        self.label_2.setText(QCoreApplication.translate("compactFile", u"Compactar Archivo", None))
        self.back_btn.setText(QCoreApplication.translate("compactFile", u"Volver", None))
        self.compact_btn.setText(QCoreApplication.translate("compactFile", u"Compactar", None))
        self.label.setText(QCoreApplication.translate("compactFile", u"Seleccionar Archivo:", None))
        self.label_3.setText(QCoreApplication.translate("compactFile", u"Contenido:", None))
    # retranslateUi

