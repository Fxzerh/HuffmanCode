from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

class InicioController(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("Ventanas/inicioPanel.ui", self)
        self.mainWindow = main_window

        # Acciones de los botones, los eventos
        # self.loadFile_btn.clicked.connect(lambda: self.cambiarPanel(1))     # Cambia al panel de carga de archivos, el indice 1 es el panel_loadFile
        # self.encodeFile_btn.clicked.connect(lambda: self.cambiarPanel(2))    # Cambia al panel de codificacion, el indice 2 es el panel_encodeFile
        # self.addError_btn.clicked.connect(lambda: self.cambiarPanel(3))      # Cambia al panel de añadir error, el indice 3 es el panel_addError
        # self.decodeFixFile_btn.clicked.connect(lambda: self.cambiarPanel(4))   # Cambia al panel de decodificacion y correccion, el indice 4 es el panel_decodeFixFile
        # self.decodeFile_btn.clicked.connect(lambda: self.cambiarPanel(5))     # Cambia al panel de decodificacion sin correccion, el indice 5 es el panel_decodeFile
    
    def cambiarPanel (self, indice):
        self.mainWindow.cambiar_pantalla(indice)