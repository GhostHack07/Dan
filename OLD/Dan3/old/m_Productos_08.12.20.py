#Importar librerias necesarias
import sys
import sqlite3

#Importar ventana de Login creada en QT Designes  y exportada a python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from f_Productos import Ui_MainWindow

#Importar módulos para abrir otras ventanas
import m_Ventas

#Importar módulo m_Constantes
import m_Constantes as C

#Variable global para cambio de ventana
window = None

class Productos_GUI(QtWidgets.QMainWindow):
  #Función para iniciar ventana de Login
  def __init__(self):
    super(Productos_GUI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    #Habilitar o deshabilitar botones al iniciar
    self.ui.b_Buscar.setEnabled(False)
    self.ui.b_Cancelar.setEnabled(True)
    self.ui.b_Agregar.setEnabled(False)
    self.ui.t_Productos.setEnabled(True)
    self.ui.b_sku.setChecked(True)

    #Habilitar o deshabilitar ingresos de textos / comboboxes
    self.ui.D_sku.setEnabled(True)
    self.ui.D_categoria.setEnabled(False)
    self.ui.D_producto.setEnabled(False)

    #Agregar categorias a la tabla
    for item in C.Constante_Categorias():
      self.ui.D_categoria.addItem(item)

    #Agregar productos a la tabla
    for item in C.Constante_Productos():
      self.ui.D_producto.addItem(item)

    #Acción de botones
    self.ui.b_Buscar.clicked.connect(self.fn_Buscar)

    #Acción de botones opcionales SKU / Categoria / Producto
    self.ui.b_sku.clicked.connect(self.fn_Seleccion_Botones)
    self.ui.b_categoria.clicked.connect(self.fn_Seleccion_Botones)
    self.ui.b_producto.clicked.connect(self.fn_Seleccion_Botones)

    #Comprobar que existan datos para buscar
    self.ui.D_sku.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_categoria.currentIndexChanged.connect(self.fn_Comprobacion)
    self.ui.D_producto.currentIndexChanged.connect(self.fn_Comprobacion)

  # ----------------- Funciones para uso de botones ----------------- #
  #Funcion para habilitar con qué criterio se va a buscar
  def fn_Seleccion_Botones(self):
    #Asegurar que solo se seleccione una opción
    if self.ui.b_sku.isChecked():
      self.ui.b_categoria.setChecked(False)
      self.ui.b_producto.setChecked(False)

      self.ui.D_sku.setEnabled(True)
      self.ui.D_categoria.setEnabled(False)
      self.ui.D_producto.setEnabled(False)

    elif self.ui.b_categoria.isChecked():
      self.ui.b_sku.setChecked(False)
      self.ui.b_producto.setChecked(False)

      self.ui.D_sku.setEnabled(False)
      self.ui.D_categoria.setEnabled(True)
      self.ui.D_producto.setEnabled(False)

    elif self.ui.b_producto.isChecked():
      self.ui.b_sku.setChecked(False)
      self.ui.b_categoria.setChecked(False)

      self.ui.D_sku.setEnabled(False)
      self.ui.D_categoria.setEnabled(False)
      self.ui.D_producto.setEnabled(True)


  def fn_Comprobacion(self):
    #Acciones por Caso 
    if self.fn_Casos() == "SKU":
      if not self.ui.D_sku.text():
        self.ui.b_Buscar.setEnabled(False)
      else:
        self.ui.b_Buscar.setEnabled(True)

    if self.fn_Casos() == "Categoria":
      if self.ui.D_categoria.currentIndex == 0:
        self.ui.b_Buscar.setEnabled(False)
      else:
        self.ui.b_Buscar.setEnabled(True)

    if self.fn_Casos() == "Producto":
      if self.ui.D_producto.currentIndex == 0:
        self.ui.b_Buscar.setEnabled(False)
      else:
        self.ui.b_Buscar.setEnabled(True)

  def fn_Casos(self):
    if self.ui.b_sku.isChecked():
      Caso = "SKU"
    if self.ui.b_categoria.isChecked():
      Caso = "Categoria"
    if self.ui.b_producto.isChecked():
      Caso = "Producto"
    return Caso

     
  # --------- Funciones para Administrar acciones en SQLite --------- #
  def fn_Buscar(self):
    #Leer datos ingresados
    sku = self.ui.D_sku.text()
    categoria = self.ui.D_categoria.currentText()
    producto = self.ui.D_producto.currentText()

    #Comprobar que el producto existe
    if self.fn_Producto_Existe(sku) == "Si":
      #Leer datos ingresados
      sku = self.ui.D_sku.text()
      categoria = self.ui.D_categoria.currentText()
      producto = self.ui.D_producto.currentText()

      if self.fn_Casos() == "SKU":
        #Abrir Base de Datos con SQLite3
        miConexion = sqlite3.connect("Productos")
        miCursor = miConexion.cursor()

        miCursor.execute("SELECT * FROM Inventario WHERE SKU = ?", [sku])
        #Extraer datos de la lista usando la posición 0 de la lista
        datos = miCursor.fetchall()
        #Acomodar datos en la tabla
        self.fn_Acomodar_Datos(datos)

      elif self.fn_Casos() == "Categoria":
        #Abrir Base de Datos con SQLite3
        miConexion = sqlite3.connect("Productos")
        miCursor = miConexion.cursor()

        miCursor.execute("SELECT * FROM Inventario WHERE Categoria = ?", [categoria])
        #Extraer datos de la lista usando la posición 0 de la lista
        datos = miCursor.fetchall()
        #Acomodar datos en la tabla
        self.fn_Acomodar_Datos(datos)
    
      elif self.fn_Casos() == "Producto":
        pass
    else:
      self.msg_info("Producto no encontrado", f"El SKU {sku} no se encuentra en la "
                      + "Base de Datos" + '\n' + "Favor de volver a intentar")

    
  
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