# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inicioPanel.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Inicio(object):
    def setupUi(self, Inicio):
        if not Inicio.objectName():
            Inicio.setObjectName(u"Inicio")
        Inicio.resize(1280, 720)
        self.gridLayout = QGridLayout(Inicio)
        self.gridLayout.setObjectName(u"gridLayout")
        self.menuLabel = QLabel(Inicio)
        self.menuLabel.setObjectName(u"menuLabel")
        self.menuLabel.setMaximumSize(QSize(400, 65))
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setHintingPreference(QFont.PreferNoHinting)
        self.menuLabel.setFont(font)
        self.menuLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.menuLabel, 0, 0, 1, 1)

        self.encodeFile_btn = QPushButton(Inicio)
        self.encodeFile_btn.setObjectName(u"encodeFile_btn")
        self.encodeFile_btn.setMaximumSize(QSize(1100, 70))
        self.encodeFile_btn.setFlat(True)

        self.gridLayout.addWidget(self.encodeFile_btn, 2, 0, 1, 1)

        self.decodeFixFile_btn = QPushButton(Inicio)
        self.decodeFixFile_btn.setObjectName(u"decodeFixFile_btn")
        self.decodeFixFile_btn.setMaximumSize(QSize(1100, 70))
        self.decodeFixFile_btn.setFlat(True)

        self.gridLayout.addWidget(self.decodeFixFile_btn, 4, 0, 1, 1)

        self.decodeFile_btn = QPushButton(Inicio)
        self.decodeFile_btn.setObjectName(u"decodeFile_btn")
        self.decodeFile_btn.setMaximumSize(QSize(1100, 70))
        self.decodeFile_btn.setAutoDefault(True)
        self.decodeFile_btn.setFlat(True)

        self.gridLayout.addWidget(self.decodeFile_btn, 5, 0, 1, 1)

        self.addError_btn = QPushButton(Inicio)
        self.addError_btn.setObjectName(u"addError_btn")
        self.addError_btn.setMaximumSize(QSize(1100, 70))
        self.addError_btn.setFlat(True)

        self.gridLayout.addWidget(self.addError_btn, 3, 0, 1, 1)

        self.loadFile_btn = QPushButton(Inicio)
        self.loadFile_btn.setObjectName(u"loadFile_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadFile_btn.sizePolicy().hasHeightForWidth())
        self.loadFile_btn.setSizePolicy(sizePolicy)
        self.loadFile_btn.setMaximumSize(QSize(1000, 70))
        self.loadFile_btn.setSizeIncrement(QSize(0, 0))
        self.loadFile_btn.setBaseSize(QSize(0, 0))
        self.loadFile_btn.setAutoFillBackground(False)
        self.loadFile_btn.setAutoDefault(False)
        self.loadFile_btn.setFlat(True)

        self.gridLayout.addWidget(self.loadFile_btn, 1, 0, 1, 1)


        self.retranslateUi(Inicio)

        self.encodeFile_btn.setDefault(False)
        self.addError_btn.setDefault(False)
        self.loadFile_btn.setDefault(False)


        QMetaObject.connectSlotsByName(Inicio)
    # setupUi

    def retranslateUi(self, Inicio):
        Inicio.setWindowTitle(QCoreApplication.translate("Inicio", u"Form", None))
        self.menuLabel.setText(QCoreApplication.translate("Inicio", u"Menu", None))
        self.encodeFile_btn.setText(QCoreApplication.translate("Inicio", u"Proteger Archivo", None))
        self.decodeFixFile_btn.setText(QCoreApplication.translate("Inicio", u"Desproteger y Corregir Archivo", None))
        self.decodeFile_btn.setText(QCoreApplication.translate("Inicio", u"Solo Desproteger Archivo", None))
        self.addError_btn.setText(QCoreApplication.translate("Inicio", u"Insertar Error", None))
        self.loadFile_btn.setText(QCoreApplication.translate("Inicio", u"Cargar Archivo", None))
    # retranslateUi

