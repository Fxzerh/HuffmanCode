from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidget, QTableWidgetItem
from Clases.nodo import Nodo
from PyQt6 import uic
import json
import os

class DecompactFileController(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("Ventanas/decompactFilePanel.ui", self)
        self.mainWindow = main_window

        # Obtenemos la ruta donde estan los archivos
        self.directorioBase = os.path.dirname(os.path.abspath(__file__))            # Directorio Actual
        self.carpetaArchivos = os.path.join(self.directorioBase, "..", "Archivos")  # Carpeta donde se guardan los archivos

        self.fileSelect = None              # Variable para guardar el nombre del archivo que se selecciona de la tabla
        self.raiz = None                    # Variable para guardar la raiz del arbol de huffman
        self.dicCaracteres = {}             # Variable para guardar el diccionario de caracteres y sus frecuencias
        self.tablaCodigos = {}              # Variable para guardar los codigos de huffman

        # ---------- SETEOS INICIALES ---------------------------------------------------------------------------------------------------------
        self.textFile.setReadOnly(True)  # Hacer el QTextEdit de solo lectura
        try:
            self.tableFile.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)  # Para que se selecciones la fila completa
            self.tableFile.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)    # Para que permita seleccionar una fila a la vez
            self.tableFile.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)      # Para que no permita editar las celdas
            self.tableFile.horizontalHeader().resizeSection(0, 400)
            self.tableFile.horizontalHeader().resizeSection(1, 150)
            self.tableFile.setRowCount(0)  # Limpiar la tabla antes de cargar los datos
            self.cargarTabla()          # Cargamos la tabla
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla: {str(e)}")

        # ---------------------------- ACCIONES Y EVENTOS ---------------------------------------------------------------------------------------------------------
        self.back_btn.clicked.connect(lambda: self.cambiarPanel(0))     # Cambia al panel de inicio, el indice 0 es el panel_inicio
        self.decompact_btn.clicked.connect(self.descomprimirArchivo)
        self.tableFile.itemClicked.connect(self.mostrarArchivo)


    def cambiarPanel (self, indice):
        self.mainWindow.cambiar_pantalla(indice)

    def refrescarPanel(self):
        self.tableFile.setRowCount(0)
        self.cargarTabla()
        self.textFile.clear()

    def showEvent(self, event):
        super().showEvent(event)
        self.refrescarPanel()
    
    def cargarTabla(self):
        if os.path.exists(self.carpetaArchivos):
            files = os.listdir(self.carpetaArchivos)
            for f in files:
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
    
    def mostrarArchivo(self):
        seleccion = self.tableFile.selectedItems()
        if not seleccion:
            return
        fila = seleccion[0].row()
        nombreArchivo = self.tableFile.item(fila, 0).text()
        rutaFile = os.path.join(self.carpetaArchivos, nombreArchivo)
        try:
            if os.path.exists(rutaFile):
                with open(rutaFile, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    self.textFile.setPlainText(contenido)
            else:
                self.textFile.setPlainText("Error: El archivo no existe en la ruta especificada.")
        except Exception as e:
            self.textFile.setPlainText(f"No se pudo leer el archivo: {str(e)}")
    
    def descomprimirArchivo(self):
        seleccion = self.tableFile.selectedItems()
        if not seleccion:
            return
        fila = seleccion[0].row()
        nombreArchivo = self.tableFile.item(fila, 0).text()
        rutaFile = os.path.join(self.carpetaArchivos, nombreArchivo)
        try:
            if os.path.exists(rutaFile):
                with open(rutaFile, "rb") as f:
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
                    textoOriginal = self.descomprimirTexto(strBytes)

                    self.textFile.clear()
                    self.textFile.setPlainText(textoOriginal)

                    # Guardamos el archivo descomprimido
                    nombreFile = os.path.splitext(nombreArchivo)[0]  # Obtener el nombre del archivo sin la extensión
                    with open(os.path.join(self.carpetaArchivos, nombreFile + ".dhu"), "w", encoding='utf-8') as f:
                        f.write(textoOriginal)
                    self.refrescarPanel()

                    QMessageBox.information(self, "Éxito", f"Archivo comprimido con Huffman correctamente. \nGuardado en '{nombreFile}.dhu'.")                    
            else:
                QMessageBox.warning(self, "Error", "El archivo no existe en la ruta especificada.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo descomprimir el archivo: {str(e)}")

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