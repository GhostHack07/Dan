#Importar librerias necesarias
import sys
import sqlite3

#Importar ventana de Login creada en QT Designes  y exportada a python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QTableWidget
from PyQt5.QtCore import Qt
from f_Productos import Ui_MainWindow

from PyQt5 import QtGui

#Importar módulos para abrir otras ventanas
import m_Ventas

#Importar módulo m_Constantes
import m_Constantes as C
import m_Cantidad

#Variable global para cambio de ventana
window = None

class Productos_GUI(QtWidgets.QMainWindow):
  #Función para iniciar ventana de Login
  def __init__(self):
    super(Productos_GUI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    self.doc = QtGui.QTextDocument(self)


    #Habilitar o deshabilitar botones al iniciar
    self.ui.b_Buscar.setEnabled(False)
    self.ui.b_Cancelar.setEnabled(True)
    self.ui.b_Agregar.setEnabled(True)
    self.ui.t_Productos.setEnabled(True)
    self.ui.b_producto.setChecked(True)

    #Habilitar o deshabilitar ingresos de textos / comboboxes
    self.ui.D_sku.setEnabled(True)
    self.ui.D_categoria.setEnabled(False)

    # ------------------ CONFIGURACIÓN DE TABLA ------------------ #
    # Deshabilitar edición
    self.ui.t_Productos.setEditTriggers(QTableWidget.NoEditTriggers)
    # Deshabilitar el comportamiento de arrastrar y soltar
    self.ui.t_Productos.setDragDropOverwriteMode(False)
    # Seleccionar toda la fila
    self.ui.t_Productos.setSelectionBehavior(QTableWidget.SelectRows)
    # Seleccionar una fila a la vez
    self.ui.t_Productos.setSelectionMode(QTableWidget.SingleSelection)
    # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
    # textos que no encajan
    self.ui.t_Productos.setWordWrap(True)
    self.ui.t_Productos.setTextElideMode(Qt.ElideNone)    #Qt.ElideRight
    # Deshabilitar clasificación
    self.ui.t_Productos.setSortingEnabled(False)
    # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
    self.ui.t_Productos.horizontalHeader().setHighlightSections(False)
    # Establecer ancho de las columnas
    for indice, ancho in enumerate((50, 240, 85, 80, 85), start=0):
        self.ui.t_Productos.setColumnWidth(indice, ancho)

    #Agregar categorias a la tabla
    for item in C.Constante_Categorias():
      self.ui.D_categoria.addItem(item)

    #Acción de botones
    self.ui.b_Buscar.clicked.connect(self.fn_Buscar)
    self.ui.b_Limpiar.clicked.connect(self.fn_Limpiar_Tabla)
    self.ui.b_Agregar.clicked.connect(self.fn_Agregar)
    self.ui.b_Cancelar.clicked.connect(self.fn_Cancelar)

    #Acción de botones opcionales SKU / Categoria / Producto
    self.ui.b_sku.clicked.connect(self.fn_Seleccion_Botones)
    self.ui.b_categoria.clicked.connect(self.fn_Seleccion_Botones)

    #Comprobar que existan datos para buscar
    self.ui.D_sku.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_categoria.currentIndexChanged.connect(self.fn_Comprobacion)
  
  # ----------------- Funciones para uso de botones ----------------- #
  #Funcion para habilitar con qué criterio se va a buscar
  def fn_Seleccion_Botones(self):
    #Asegurar que solo se seleccione una opción
    if self.ui.b_sku.isChecked():
      self.ui.b_categoria.setChecked(False)
      self.ui.b_producto.setChecked(False)

      self.ui.D_sku.setEnabled(True)
      self.ui.D_categoria.setEnabled(False)
      #Borrar dato al cambiar la selección
      self.ui.D_categoria.setCurrentIndex(0)
      #Limpiar tabla al cambiar de opción
      self.fn_Limpiar_Tabla()

    elif self.ui.b_categoria.isChecked():
      self.ui.b_sku.setChecked(False)
      self.ui.b_producto.setChecked(False)

      self.ui.D_sku.setEnabled(False)
      self.ui.D_categoria.setEnabled(True)
      #Borrar dato al cambiar la selección
      self.ui.D_sku.clear()
      #Limpiar tabla al cambiar de opción
      self.fn_Limpiar_Tabla()

    elif self.ui.b_producto.isChecked():
      self.ui.b_sku.setChecked(False)
      self.ui.b_categoria.setChecked(False)

      self.ui.D_sku.setEnabled(True)
      self.ui.D_categoria.setEnabled(False)
      #Borrar dato al cambiar la selección
      self.ui.D_categoria.setCurrentIndex(0)
      #Limpiar tabla al cambiar de opción
      self.fn_Limpiar_Tabla()

  def fn_Comprobacion(self):
    #Acciones por Caso 
    if self.fn_Casos() == "SKU" or self.fn_Casos() == "Producto":
      if not self.ui.D_sku.text():
        self.ui.b_Buscar.setEnabled(False)
      else:
        self.ui.b_Buscar.setEnabled(True)

    if self.fn_Casos() == "Categoria":
      if self.ui.D_categoria.currentIndex == 0:
        self.ui.b_Buscar.setEnabled(False)
      else:
        self.ui.b_Buscar.setEnabled(True)

  def fn_Casos(self):
    if self.ui.b_sku.isChecked():
      Caso = "SKU"
    elif self.ui.b_categoria.isChecked():
      Caso = "Categoria"
    elif self.ui.b_producto.isChecked():
      Caso = "Producto"
    return Caso

  def fn_Limpiar_Tabla(self):
    self.ui.t_Productos.clearContents()
    self.ui.t_Productos.setRowCount(1)
     
  # --------- Funciones para Administrar acciones en SQLite --------- #
  def fn_Buscar(self):
    #Leer datos ingresados
    sku = self.ui.D_sku.text()
    categoria = self.ui.D_categoria.currentText()

    if self.fn_Casos() == "SKU":
      #Abrir Base de Datos con SQLite3
      miConexion = sqlite3.connect("Productos")
      miCursor = miConexion.cursor()
    
      #Comprobar que el producto existe
      if self.fn_Producto_Existe(sku) == "Si":
        miCursor.execute("SELECT * FROM Inventario WHERE SKU = ?", [sku])
        #Extraer datos de la lista usando la posición 0 de la lista
        datos = miCursor.fetchall()
        #Acomodar datos en la tabla
        self.fn_Acomodar_Datos(datos)
        #cerrar conexión SQLite
        miConexion.close()

      else:
        self.msg_info("Producto no encontrado", f"El SKU {sku} no se encuentra en la "
                        + "Base de Datos" + '\n' + "Favor de volver a intentar")

    elif self.fn_Casos() == "Categoria":
      #Abrir Base de Datos con SQLite3
      miConexion = sqlite3.connect("Productos")
      miCursor = miConexion.cursor()

      miCursor.execute("SELECT * FROM Inventario WHERE Categoria = ?", [categoria])
      #Extraer datos de la lista usando la posición 0 de la lista
      datos = miCursor.fetchall()
      #Acomodar datos en la tabla
      self.fn_Acomodar_Datos(datos)
      #cerrar conexión SQLite
      miConexion.close()

    elif self.fn_Casos() == "Producto":
      #Leer dato ingresado
      texto = self.ui.D_sku.text()
      #Abrir Base de Datos con SQLite3
      miConexion = sqlite3.connect("Productos")
      miCursor = miConexion.cursor()

      busqueda = texto + "%"

      miCursor.execute("SELECT * FROM Inventario WHERE Producto LIKE ?", [busqueda])
      datos = miCursor.fetchall()

      #Acomodar datos en la tabla
      self.fn_Acomodar_Datos(datos)
      #cerrar conexión SQLite
      miConexion.close()

  #Función para agregar producto a la ventana de Ventas
  def fn_Agregar(self):
    seleccion = self.ui.t_Productos.selectedItems()
    #Verificar que se haya seleccionado un renglon
    if seleccion:
      sku = seleccion[0].data(0)
      
      self.fn_Abrir_Cantidad()

      #Abrir Base de Datos con SQLite3
      miConexion = sqlite3.connect("Productos")
      miCursor = miConexion.cursor()

      miCursor.execute("SELECT Cantidad FROM Cantidad_Temp")
      cantidad = miCursor.fetchall()

      print (cantidad)

      #miCursor.execute('''INSERT INTO TEMP (SKU, Producto, Precio, Descuento)
      #                    SELECT SKU, Producto, Precio, Descuento FROM Inventario
      #                    WHERE SKU = ?''', [sku])

      #miConexion.commit()
      #miConexion.close()


    else:
      self.msg_info("Sin selección", "No has seleccionado ningún producto."
                    + '\n' + "Favor de seleccionar un producto.")


    #if Producto_Seleccionado:


  def fn_Cancelar(self):
    #Función de volver a ventana de Ventas
    self.fn_Cerrar_Ventana()

  def fn_Abrir_Cantidad(self):
    ventana = m_Cantidad
    ventana.start()

    
  #Función para acomodar datos en la tabla
  def fn_Acomodar_Datos(self, datos):
    r = 0
    for valor in datos:
      self.ui.t_Productos.setRowCount(r + 1)
      self.ui.t_Productos.setItem(r, 0, QTableWidgetItem(str(valor[0])))
      self.ui.t_Productos.setItem(r, 1, QTableWidgetItem(str(valor[1])))
      self.ui.t_Productos.setItem(r, 2, QTableWidgetItem(str(valor[3])))
      self.ui.t_Productos.setItem(r, 3, QTableWidgetItem(str(valor[4])))
      self.ui.t_Productos.setItem(r, 4, QTableWidgetItem(str(valor[5])))
      #Pasar al siguiente renglón
      r = r + 1
    #Autoajustar renglon para que se muestre todo el texto
    self.ui.t_Productos.resizeRowsToContents()

  def fn_Producto_Existe(self, sku):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Productos")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM Inventario WHERE SKU = ?", [sku])
    if miCursor.fetchall():
      return "Si"
    else:
      return "No"
    miConexion.close()

  # -------------------- Funciones para Mensajes -------------------- #
  #Función para mensajes de información
  def msg_info(self, titulo, mensaje):
      msgbox = QMessageBox()
      msgbox.setIcon(QMessageBox.Information)
      msgbox.setWindowTitle(titulo)
      msgbox.setText(mensaje)
      msgbox.exec_()

  # ------------- Funciones para Eventos en la ventana  ------------- #
  #Evento para cuando la ventana se cierra
  def closeEvent(self, event):
    #ventana = m_Ventas
    #ventana.start()

    # == TEMPORAL == #
    self.close()

  #Cerrar ventana
  def fn_Cerrar_Ventana(self):
    #self.destroy()
    #ventana = m_Ventas
    #ventana.start()
    
    # == TEMPORAL == #
    self.close()

#Función para iniciar ventana de Ventas
def start():
    global window  
    window = Productos_GUI()
    window.show()

#Función para iniciar ventana de Registro 
if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  application = Productos_GUI()
  application.show()
  sys.exit(app.exec())
