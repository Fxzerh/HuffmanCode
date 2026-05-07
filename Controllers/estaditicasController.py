from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6 import uic
import os
import json
from Clases.nodo import Nodo

class EstadisticasController(QWidget):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("Ventanas/estadisticasPanel.ui", self)
        self.mainWindow = main_window

        self.directorioBase = os.path.dirname(os.path.abspath(__file__))
        self.carpetaArchivos = os.path.join(self.directorioBase, "..", "Archivos")

        self.statsTable.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.statsTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.statsTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.statsTable.setColumnCount(5)
        self.statsTable.setHorizontalHeaderLabels([
            "Archivo",
            "Original",
            "Compactado",
            "Descompactado",
            "Ahorro"
        ])
        self.header = self.statsTable.horizontalHeader()
        self.header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # ---------------------------- ACCIONES Y EVENTOS -----------------------------------------------------------------------------------------
        self.back_btn.clicked.connect(lambda: self.cambiarPanel(0))
        self.refresh_btn.clicked.connect(self.refrescarPanel)
        self.statsTable.itemClicked.connect(self.mostrarDetalle)

    def cambiarPanel(self, indice):
        self.mainWindow.cambiar_pantalla(indice)

    def showEvent(self, event):
        super().showEvent(event)
        self.refrescarPanel()

    def refrescarPanel(self):
        self.statsTable.setRowCount(0)
        self.label_info.setText("Cargando estadísticas de archivos...")
        self.cargarTabla()
        if self.statsTable.rowCount() == 0:
            self.label_info.setText("No se encontraron archivos .txt en la carpeta Archivos.")
        else:
            self.label_info.setText("Seleccione un archivo para ver la comparación de tamaños.")
            self.statsTable.resizeColumnsToContents()
        self.header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def cargarTabla(self):
        if not os.path.exists(self.carpetaArchivos):
            return

        for nombreArchivo in sorted(os.listdir(self.carpetaArchivos)):
            if not nombreArchivo.lower().endswith(".txt"):
                continue

            rutaTxt = os.path.join(self.carpetaArchivos, nombreArchivo)
            if not os.path.isfile(rutaTxt):
                continue

            sizeTxt = os.path.getsize(rutaTxt)
            rutaHuf = os.path.splitext(rutaTxt)[0] + ".huf"
            rutaDhu = os.path.splitext(rutaTxt)[0] + ".dhu"

            sizeHuf = os.path.getsize(rutaHuf) if os.path.exists(rutaHuf) else None
            sizeDhu = None
            if os.path.exists(rutaDhu):
                sizeDhu = os.path.getsize(rutaDhu)
            elif sizeHuf is not None:
                sizeDhu = self.get_decompressed_size(rutaHuf)

            ahorro = "N/A"
            if sizeHuf is not None and sizeTxt > 0:
                ahorro = f"{(1 - sizeHuf / sizeTxt) * 100:.2f}%"

            row = self.statsTable.rowCount()
            self.statsTable.insertRow(row)
            self.statsTable.setItem(row, 0, QTableWidgetItem(nombreArchivo))
            self.statsTable.setItem(row, 1, QTableWidgetItem(self.format_size(sizeTxt)))
            self.statsTable.setItem(row, 2, QTableWidgetItem(self.format_size(sizeHuf) if sizeHuf is not None else "No existe"))
            self.statsTable.setItem(row, 3, QTableWidgetItem(self.format_size(sizeDhu) if sizeDhu is not None else "No existe"))
            self.statsTable.setItem(row, 4, QTableWidgetItem(ahorro))

    def mostrarDetalle(self):
        seleccion = self.statsTable.selectedItems()
        if not seleccion:
            return

        fila = seleccion[0].row()
        archivo = self.statsTable.item(fila, 0).text()
        original = self.statsTable.item(fila, 1).text()
        compactado = self.statsTable.item(fila, 2).text()
        descompactado = self.statsTable.item(fila, 3).text()
        ahorro = self.statsTable.item(fila, 4).text()
        self.label_info.setText(
            f"Archivo: {archivo} | Original: {original} | Compactado: {compactado} | "
            f"Descompactado: {descompactado} | Ahorro: {ahorro}"
        )

    def get_decompressed_size(self, rutaHuf):
        try:
            with open(rutaHuf, "rb") as f:
                padding = f.read(1)
                cantPadding = int.from_bytes(padding, byteorder="big")
                tamañoDic = f.read(4)
                longDic = int.from_bytes(tamañoDic, byteorder="big")
                dicBytes = f.read(longDic)
                self.dicCaracteres = json.loads(dicBytes.decode())
                contenido = f.read()
                strBytes = ""
                for byte in contenido:
                    strBytes += format(byte, "08b")
                if cantPadding > 0:
                    strBytes = strBytes[:-cantPadding]

                self.reconstruirArbol()
                textoDescomprimido = self.descomprimirTexto(strBytes)
                return len(textoDescomprimido.encode("utf-8"))
        except Exception:
            return None

    def format_size(self, size):
        if size is None:
            return "No existe"
        if size < 1024:
            return f"{size} B"
        if size < 1024 * 1024:
            return f"{size / 1024:.2f} KB"
        return f"{size / (1024 * 1024):.2f} MB"

    def reconstruirArbol(self):
        listNodos = []
        for par in self.dicCaracteres.items():
            nodo = Nodo(simbolo=par[0], frecuencia=par[1])
            listNodos.append(nodo)

        while len(listNodos) > 1:
            listNodos.sort()
            nodoI = listNodos.pop(0)
            nodoD = listNodos.pop(0)
            padre = Nodo(simbolo=None, frecuencia=nodoI.frecuencia + nodoD.frecuencia)
            padre.hijoIzq = nodoI
            padre.hijoDer = nodoD
            listNodos.append(padre)

        self.raiz = listNodos[0] if listNodos else None

    def descomprimirTexto(self, textoComprimido):
        if not self.raiz:
            return ""

        nodoActual = self.raiz
        textoDescomprimido = ""
        for c in textoComprimido:
            if c == "0":
                nodoActual = nodoActual.hijoIzq
            else:
                nodoActual = nodoActual.hijoDer

            if nodoActual.simbolo is not None:
                textoDescomprimido += nodoActual.simbolo
                nodoActual = self.raiz

        return textoDescomprimido
