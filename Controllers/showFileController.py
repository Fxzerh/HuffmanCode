from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt6 import uic
import shutil
import os
import json
from Clases.nodo import Nodo

class ShowFileController(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("Ventanas/showFilePanel.ui", self)
        self.mainWindow = main_window

        # Obtenemos la ruta donde estan los archivos
        self.directorioBase = os.path.dirname(os.path.abspath(__file__))            # Directorio Actual
        self.carpetaArchivos = os.path.join(self.directorioBase, "..", "Archivos")  # Carpeta donde se guardan los archivos

        self.raiz = None                    # Variable para guardar la raiz del arbol de huffman
        self.dicCaracteres = {}             # Variable para guardar el diccionario de caracteres y sus frecuencias

        # ---------- SETEOS INICIALES -----------------------------------------------------------------------------------------
        self.textFileO.setReadOnly(True)  # Hacer el QTextEdit de solo lectura
        self.textFileC.setReadOnly(True)  # Hacer el QTextEdit de solo lectura
        try:
            self.tableFile.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)  # Para que se selecciones la fila completa
            self.tableFile.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)    # Para que permita seleccionar una fila a la vez
            self.tableFile.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)      # Para que no permita editar las celdas
            self.tableFile.setColumnCount(2)
            self.tableFile.setHorizontalHeaderLabels(["Nombre", "Tamaño"])
            self.tableFile.horizontalHeader().resizeSection(0, 400)
            self.tableFile.horizontalHeader().resizeSection(1, 150)
            self.tableFile.setRowCount(0)  # Limpiar la tabla antes de cargar los datos
            self.cargarTabla()          # Cargamos la tabla
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla: {str(e)}")

        # ---------------------------- ACCIONES Y EVENTOS -----------------------------------------------------------------------------------------
        self.back_btn.clicked.connect(lambda: self.cambiarPanel(0))     # Cambia al panel de inicio, el indice 0 es el panel_inicio
        self.tableFile.itemClicked.connect(self.compararArchivos)

    def cambiarPanel (self, indice):
        self.mainWindow.cambiar_pantalla(indice)

    def refrescarPanel(self):
        self.tableFile.setRowCount(0)
        self.cargarTabla()
        self.textFileO.clear()
        self.textFileC.clear()
        self.label.setText("")

    def showEvent(self, event):
        super().showEvent(event)
        self.refrescarPanel()
    
    def cargarTabla(self):
        if os.path.exists(self.carpetaArchivos):
            files = os.listdir(self.carpetaArchivos)
            for f in files:
                if f.endswith('.txt'):
                    file_path = os.path.join(self.carpetaArchivos, f)   # Ruta completa del archivo f
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
    
    def compararArchivos(self):
        seleccion = self.tableFile.selectedItems()
        if not seleccion:
            return
        fila = seleccion[0].row()
        nombreArchivoTxt = self.tableFile.item(fila, 0).text()
        nombreArchivoHuf = nombreArchivoTxt.replace('.txt', '.huf')
        rutaTxt = os.path.join(self.carpetaArchivos, nombreArchivoTxt)
        rutaHuf = os.path.join(self.carpetaArchivos, nombreArchivoHuf)
        
        # Leer archivo original
        try:
            with open(rutaTxt, 'r', encoding='utf-8') as f:
                contenidoOriginal = f.read()
                self.textFileO.setPlainText(contenidoOriginal)
        except Exception as e:
            self.textFileO.setPlainText(f"Error al leer archivo original: {str(e)}")
            self.textFileC.setPlainText("")
            self.label.setText("Error")
            return
        
        # Descomprimir archivo .huf
        try:
            if os.path.exists(rutaHuf):
                with open(rutaHuf, "rb") as f:
                    # Extraemos la informacion del heap del archivo comprimido
                    padding = f.read(1)
                    cantPadding = int.from_bytes(padding, byteorder='big')      # Obtenemos la cantidad de bits que son de relleno (padding)
                    tamañoDic = f.read(4)
                    longDic = int.from_bytes(tamañoDic, byteorder='big')        # Obtenemos la longitud del diccionario (en bytes) para luego leerlo
                    dicBytes = f.read(longDic)                                  # Recuperamos el diccionario con las frecuencias de cada caracter
                    self.dicCaracteres = json.loads(dicBytes.decode())          # Convertimos el diccionario de bytes a un diccionario de python
                    
                    # Recuperamos el contenido comprimido del archivo
                    contenido = f.read()
                    strBytes = ""                                            
                    for byte in contenido:
                        # Convertimos cada byte a su representación binaria y lo agregamos a la lista
                        strBytes += format(byte, '08b')
                    if cantPadding > 0:
                        strBytes = strBytes[:-cantPadding]               # Eliminamos los bits de relleno (padding) del ultimo byte

                    # Reconstruir el arbol de Huffman
                    self.reconstruirArbol()
                    # Descomprimimos el texto
                    textoDescomprimido = self.descomprimirTexto(strBytes)

                    self.textFileC.setPlainText(textoDescomprimido)
                    
                    # Comparar
                    if contenidoOriginal == textoDescomprimido:
                        self.label.setText("Archivos coinciden")
                    else:
                        self.label.setText("Archivos no coinciden")
            else:
                self.textFileC.setPlainText("Archivo .huf no encontrado")
                self.label.setText("Archivo comprimido no existe")
        except Exception as e:
            self.textFileC.setPlainText(f"Error al descomprimir: {str(e)}")
            self.label.setText("Error en descompresión")

    def reconstruirArbol(self):
        listNodos = []
        for par in self.dicCaracteres.items():      # Por cada par (caracter, frecuencia) del diccionario creamos un nodo
            nodo = Nodo(simbolo=par[0], frecuencia=par[1])
            listNodos.append(nodo)

        while len(listNodos) > 1:           # Creamos nodos padres hasta llegar a la raiz y crear asi el arbol de Huffman
            listNodos.sort()                # Ordenamos la lista de nodos por frecuencia
            nodoI = listNodos.pop(0)
            nodoD = listNodos.pop(0)
            padre = Nodo(simbolo=None, frecuencia=nodoI.frecuencia + nodoD.frecuencia)  # Creamos el nodo padre de los 2 nodos con menos frecuencia
            padre.hijoIzq = nodoI
            padre.hijoDer = nodoD
            listNodos.append(padre)         # Agregamos el padre a la lista de nodos para seguir creando el arbol
        self.raiz = listNodos[0]
    
    def descomprimirTexto(self, textoComprimido):
        nodoActual = self.raiz                              # Agarramos la raiz para recorrer el arbol de huffman generado
        textoDescomprimido = ""
        for c in textoComprimido:                           # Por cada caracter del archivo comprimido recorremos el arbol
            if c == "0":
                nodoActual = nodoActual.hijoIzq             # Si el bit es 0 vamos al hijo izquierdo
            else:
                nodoActual = nodoActual.hijoDer             # Si el bit es 1 vamos al hijo derecho
            
            if nodoActual.simbolo != None:                  # Si el simbolo del nodo es distinto a None, llegamos a una hoja por lo que es un simbolo del texto original
                textoDescomprimido += nodoActual.simbolo    # Agregamos el simbolo al texto descomprimido
                nodoActual = self.raiz                      # Volvemos a la raiz para seguir recorriendo el arbol con los siguientes bits del texto comprimido
        return textoDescomprimido