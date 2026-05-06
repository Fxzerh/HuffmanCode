from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt6 import uic
import os

class ShowFileController(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("Ventanas/showFilePanel.ui", self)
        self.mainWindow = main_window

        # Obtenemos la ruta donde estan los archivos
        self.directorioBase = os.path.dirname(os.path.abspath(__file__))            # Directorio Actual
        self.carpetaArchivos = os.path.join(self.directorioBase, "..", "Archivos")  # Carpeta donde se guardan los archivos

        self.fileSelect = None              # Variable para guardar el nombre del archivo que se selecciona de la tabla

        # ---------- SETEOS INICIALES ---------------------------------------------------------------------------------------------------------
        self.textFileO.setReadOnly(True)  # Hacer los QTextEdit de solo lectura
        self.textFileC.setReadOnly(True)
        try:
            self.tableFile.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)  # Para que se selecciones la fila completa
            self.tableFile.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)    # Para que permita seleccionar una fila a la vez
            self.tableFile.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)      # Para que no permita editar las celdas
            self.tableFile.horizontalHeader().resizeSection(0, 330)
            self.tableFile.horizontalHeader().resizeSection(1, 112)
            self.tableFile.setRowCount(0)  # Limpiar la tabla antes de cargar los datos
            self.cargarTabla()          # Cargamos la tabla
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla: {str(e)}")

        # ---------------------------- ACCIONES Y EVENTOS ---------------------------------------------------------------------------------------------------------
        self.back_btn.clicked.connect(lambda: self.cambiarPanel(0))     # Cambia al panel de inicio, el indice 0 es el panel_inicio
        self.tableFile.itemClicked.connect(self.mostrarArchivo)
        

    def cambiarPanel (self, indice):
        self.mainWindow.cambiar_pantalla(indice)

    def refrescarPanel(self):
        self.tableFile.setRowCount(0)
        self.cargarTabla()
        self.textFileO.clear()
        self.textFileC.clear()

    def showEvent(self, event):
        super().showEvent(event)
        self.refrescarPanel()
    
    def cargarTabla(self):
        if os.path.exists(self.carpetaArchivos):
            files = os.listdir(self.carpetaArchivos)
            for f in files:
                fileType = os.path.splitext(f)[1]
                file_path = os.path.join(self.carpetaArchivos, f)   # Ruta completa del archivo f
                if fileType != ".huf":
                    if os.path.isfile(file_path):  # Pregunta si f es un archivo (y no una carpeta)
                        # Obtenemos el tamaño de f
                        tamaño = os.path.getsize(file_path)

                        # Convertir tamaño a formato B, KB o MB
                        if tamaño < 1024:
                            tamaño_str = f"{tamaño} B"
                        elif tamaño < 1024 * 1024:
                            tamaño_str = f"{tamaño / 1024:.2f} KB"
                        else:
                            tamaño_str = f"{tamaño / (1024 * 1024):.2f} MB"
                        
                        # Agregamos el archivo a la tabla
                        rowPosition = self.tableFile.rowCount()
                        self.tableFile.insertRow(rowPosition)
                        self.tableFile.setItem(rowPosition, 0, QTableWidgetItem(f))             # Nombre
                        self.tableFile.setItem(rowPosition, 1, QTableWidgetItem(tamaño_str))    # Tamaño
    
    def mostrarArchivo(self):
        seleccion = self.tableFile.selectedItems()
        if not seleccion:
            return
        fila = seleccion[0].row()
        archivo = self.tableFile.item(fila, 0).text()
        nombreArchivo = os.path.splitext(archivo)[0]
        rutaFileO = os.path.join(self.carpetaArchivos, archivo)
        rutaFileC = os.path.join(self.carpetaArchivos, nombreArchivo + ".dhu")
        self.textFileO.clear()
        self.textFileC.clear()
        try:
            if os.path.splitext(archivo)[1] != ".dhu":
                if os.path.exists(rutaFileO):
                    with open(rutaFileO, 'r', encoding='utf-8') as f:
                        contenido = f.read()
                        self.textFileO.setPlainText(contenido)
                else:
                    QMessageBox.warning(self, "Error", "El archivo no existe en la ruta especificada.")
                if os.path.exists(rutaFileC):
                    with open(rutaFileC, 'r', encoding='utf-8') as f:
                        contenido = f.read()
                        self.textFileC.setPlainText(contenido)   
                else:
                    QMessageBox.warning(self, "Error", f"No se encontro la versión descomprimida del archivo: {archivo}.")
            else:
                self.textFileO.setPlainText("Seleccionar un archivo que no sea .dhu")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo leer el archivo: {str(e)}")