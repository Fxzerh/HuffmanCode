from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from PyQt6 import uic
# Importamos todos los controladores
from Controllers.inicioController import InicioController
# from Controllers.loadFileController import LoadFileController
# from Controllers.addErrorController import AddErrorController
# from Controllers.decodeFileController import DecodeFileController
# from Controllers.decodeFixFileController import DecodeFixFileController
# from Controllers.encodeFileController import EncodeFileController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ventanas/mainWindow.ui", self)
        self.setWindowTitle("PM 2: Huffman")

        self.stackedWidget = QStackedWidget()      # Creamos el StackedWidget
        self.setCentralWidget(self.stackedWidget)  # Al StackedWidget no ponemos como principal de la ventana principal

        # Instanciamos los controladores
        self.inicioController = InicioController(self)      # Con self hacemos que puedan acceder a MainWindow
        # self.loadFileController = LoadFileController(self)
        # self.encodeFileController = EncodeFileController(self)
        # self.addErrorController = AddErrorController(self)
        # self.decodeFixFileController = DecodeFixFileController(self)
        # self.decodeFileController = DecodeFileController(self)

        # Añadimos el controlador al StackedWidget
        self.stackedWidget.addWidget(self.inicioController)        # Indice 0
        # self.stackedWidget.addWidget(self.loadFileController)      # Indice 1
        # self.stackedWidget.addWidget(self.encodeFileController)    # Indice 2
        # self.stackedWidget.addWidget(self.addErrorController)      # Indice 3
        # self.stackedWidget.addWidget(self.decodeFixFileController) # Indice 4
        # self.stackedWidget.addWidget(self.decodeFileController)    # Indice 5


        self.stackedWidget.setCurrentWidget(self.inicioController)      # Mostramos el panel_inicio al iniciar la aplicación, se puede cambiar a otro panel usando setCurrentWidget() con el panel deseado

    def cambiar_pantalla(self, indice):
        self.stackedWidget.setCurrentIndex(indice)


