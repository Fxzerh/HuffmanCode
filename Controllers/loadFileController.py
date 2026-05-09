from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt6 import uic
import shutil
import os

class LoadFileController(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("Ventanas/loadFilePanel.ui", self)
        self.mainWindow = main_window

        # Acciones de los botones, los eventos
        self.back_btn.clicked.connect(lambda: self.cambiarPanel(0))     # Cambia al panel de inicio, el indice 0 es el panel_inicio
        self.buscarFile_btn.clicked.connect(self.seleccionar_y_guardar)
        

    def cambiarPanel (self, indice):
        self.mainWindow.cambiar_pantalla(indice)
        self.showFile.clear()

    def seleccionar_y_guardar(self):
        # Abrimos el buscador de archivos
        ruta_origen, _ = QFileDialog.getOpenFileName(
            self, 
            "Seleccionar archivo", 
            "", 
            "Todos los archivos (*.*)"
        )

        if ruta_origen:
            try:
                # Obtenemos la carpeta destino donde queremos guardar los archivos
                directorio_actual = os.path.dirname(os.path.abspath(__file__))
                carpeta_destino = os.path.join(directorio_actual, "..", "Archivos")
                
                # Controlamos que la carpeta destino exista
                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)

                nombre_archivo = os.path.basename(ruta_origen)              # Obtiene el nombre del archivo
                ruta_final = os.path.join(carpeta_destino, nombre_archivo)  # Obtiene la ruta que va a tener el archivo al final, dentro de la carpeta destino

                # Copiamos el archivo del origen al destino
                shutil.copy2(ruta_origen, ruta_final)

                # Feedback al usuario
                print(f"Archivo guardado en: {ruta_final}")
                if os.path.split(ruta_final)[1] == ".txt":
                    with open(ruta_final, "r", encoding="utf-8") as file:
                        self.showFile.setPlainText(file.read())
                else:
                    self.showFile.setPlainText("No se puede mostrar archivos que no sean '.txt' por el momento")

                QMessageBox.information(self, "Éxito", f"Archivo '{nombre_archivo}' guardado correctamente.")

            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo: {str(e)}")
    
    