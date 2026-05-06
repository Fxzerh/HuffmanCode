from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QTableWidget
from Clases.nodo import Nodo 
from PyQt6 import uic
import json
import os

class CompactFileController(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("Ventanas/compactFilePanel.ui", self)
        self.mainWindow = main_window

        # Obtenemos la ruta donde estan los archivos
        self.directorioBase = os.path.dirname(os.path.abspath(__file__))            # Directorio Actual
        self.carpetaArchivos = os.path.join(self.directorioBase, "..", "Archivos")  # Carpeta donde se guardan los archivos

        self.fileSelect = None              # Variable para guardar el nombre del archivo que se selecciona de la tabla
        self.raiz = None                    # Variable para guardar la raiz del arbol de huffman
        self.dicCaracteres = {}             # Variable para guardar el diccionario de caracteres y sus frecuencias
        self.tablaCodigos = {}              # Variable para guardar los codigos de huffman
        self.cantNodos = 0

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
        self.compact_btn.clicked.connect(self.comprimirArchivo)
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

    def comprimirArchivo(self):
        seleccion = self.tableFile.selectedItems()
        if not seleccion:
            return
        fila = seleccion[0].row()
        nombreArchivo = self.tableFile.item(fila, 0).text()
        rutaFile = os.path.join(self.carpetaArchivos, nombreArchivo)
        try:
            if os.path.exists(rutaFile):
                with open(rutaFile, "r", encoding='utf-8') as f:
                    contenido = f.read()
                # CREAMOS EL ARBOL DE HUFFMAN
                self.arbolHuffman(contenido)

                # GENERAMOS LOS CODIGOS DE HUFFMAN
                self.generarCodigos(self.raiz, "")

                # COMPRIMIMOS EL CONTENIDO DEL ARCHIVO
                bitsComprimidos = ""
                cantPadding = 0
                for caracter in contenido:                      # Creamos un string con la traduccion del texto al codigo de huffman
                    codigo = self.tablaCodigos[caracter]
                    bitsComprimidos += codigo
                while len(bitsComprimidos) % 8 != 0:            # Agregamos bits de padding (0s) para que el string sea multiplo de 8
                    bitsComprimidos += "0"
                    cantPadding += 1
                
                bytesComprimidos = b""                          # Convertimos el string de bits a bytes para poder escribirlo en el archivo binario
                for i in range(0, len(bitsComprimidos), 8):     # Vamos tomando de a 8 bits para convertirlos a bytes
                    byte = bitsComprimidos[i:i+8]
                    byteDecimal = int(byte, 2)                                      # Pasamos los 8 bits a decimal
                    bytesComprimidos += byteDecimal.to_bytes(1, byteorder='big')    # Pasamos los decimales a byte y los concatenamos
                
                # GUARDAMOS EL ARCHIVO COMPRIMIDO
                dicBytes = json.dumps(self.dicCaracteres).encode()
                nombreFile = os.path.splitext(nombreArchivo)[0]  # Obtener el nombre del archivo sin la extensión
                #  Formato del archivo comprimido: [Header][Contenido Comprimido]
                with open(os.path.join(self.carpetaArchivos, nombreFile + ".huf"), "wb") as f:
                    # Agregamos el header 
                    f.write(cantPadding.to_bytes(1, byteorder='big'))       # Guardamos la cantidad de bits de padding en el header
                    f.write(len(dicBytes).to_bytes(4, byteorder='big'))     # Guardamos la cantidad de caractereres del diccionario en el header
                    f.write(dicBytes)                                       # Guardamos el diccionario de caracteres en el header
                    # Agregamos el contenido comprimido
                    f.write(bytesComprimidos)  
                self.dicCaracteres = {}     # Limpiamos el diccionario de caracteres para la proxima compresion
                self.tablaCodigos = {}      # Limpiamos la tabla de codigos para la proxima compresion                                 
                self.refrescarPanel()
                QMessageBox.information(self, "Éxito", f"Archivo comprimido con Huffman correctamente. \nGuardado en '{nombreFile}.huf'.")               

            else:
                QMessageBox.warning(self, "Error", "El archivo no existe en la ruta especificada.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo comprimir el archivo: {str(e)}")

    def arbolHuffman(self, texto):
        listCaracteres = list(texto)        # Dividimos el texto en caracteres
        listNodos = []
        for caracter in listCaracteres:     # Creamos el diccionario con la frecuencia de cada caracter
            self.dicCaracteres[caracter] = self.dicCaracteres.get(caracter, 0) + 1

        for par in self.dicCaracteres.items():      # Por cada par (caracter, frecuencia) del diccionario creamos un nodo
            nodo = Nodo(simbolo=par[0], frecuencia=par[1])
            listNodos.append(nodo)
        
        self.cantNodos = len(listNodos)
        while len(listNodos) > 1:           # Creamos nodos padres hasta llegar a la raiz y crear asi el arbol de Huffman
            listNodos.sort()                # Ordenamos la lista de nodos por frecuencia
            nodoI = listNodos.pop(0)
            nodoD = listNodos.pop(0)
            padre = Nodo(simbolo=None, frecuencia=nodoI.frecuencia + nodoD.frecuencia)  # Creamos el nodo padre de los 2 nodos con menos frecuencia
            padre.hijoIzq = nodoI
            padre.hijoDer = nodoD
            listNodos.append(padre)         # Agregamos el padre a la lista de nodos para seguir creando el arbol
        self.raiz = listNodos[0]
    
    def generarCodigos(self, nodo, codigo=""):                  # Creamos la tabla de codigos de Huffman recorriendo recursivamente el arbol
        if self.cantNodos == 1:                         # Caso especial donde el archivo original solo tiene 1 unico caracter, por lo que la raiz seria una hoja
            self.tablaCodigos[nodo.simbolo] = "0"
            return
        
        if nodo.simbolo != None:
            self.tablaCodigos[nodo.simbolo] = codigo            # Si el nodo es una hoja, guardamos el codigo en la tabla
        else:
            self.generarCodigos(nodo.hijoIzq, codigo + "0")     # Si el nodo es interno, seguimos recorriendo el arbol por izq agregando "0" al codigo
            self.generarCodigos(nodo.hijoDer, codigo + "1")     # Si el nodo es interno, seguimos recorriendo el arbol por der agregando "1" al codigo
