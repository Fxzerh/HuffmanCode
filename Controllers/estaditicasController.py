from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt6 import uic
import shutil
import os

class EstadisticasController(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("Ventanas/estadisticasPanel.ui", self)
        self.mainWindow = main_window

        # ---------------------------- ACCIONES Y EVENTOS ---------------------------------------------------------------------------------------------------------
        self.back_btn.clicked.connect(lambda: self.cambiarPanel(0))     # Cambia al panel de inicio, el indice 0 es el panel_inicio
        

    def cambiarPanel (self, indice):
        self.mainWindow.cambiar_pantalla(indice)