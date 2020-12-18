#Importar librerias necesarias
import sys
import sqlite3

#Importar ventana de Login creada en QT Designes  y exportada a python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Pantallas.f_Inventario import Ui_MainWindow

#Libreria para poder validar si los datos son numeros, texto, enteros o flotantes
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

#Importar módulo m_Ventas
import Ventanas.m_Ventas as m_Ventas

#Importar módulo m_Constantes
import Ventanas.m_Constantes as C

#Variable global para cambio de ventana
window = None

class Inventario_GUI(QtWidgets.QMainWindow):
  #Función para iniciar ventana de Inventario
  def __init__(self):
    super(Inventario_GUI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    #Habilitar o deshabilitar botones al iniciar
    self.ui.b_Buscar.setEnabled(True)
    self.ui.b_Registrar.setEnabled(False)
    self.ui.b_Cancelar.setEnabled(True)
    self.ui.D_sku.setEnabled(False)

    #Tipo de datos en las cajas de texto
    #Solo acepta números
    entero = QRegExp("(\\d+)")
    #Solo acepta números con punto flotante y 2 cifras después del .
    flotante = QRegExp("(([0-9]*[.])?[0-9]{1,2})")
    #Solo se aceptan numeros de 0-100 y 2 cifras después del .
    descuento = QRegExp("(^(0*(\d{1,2}(\.\d{1,2})?)|\.\d{1,2}|100(\.0{1,2}$)?)$)")
    #Validacion de los caracteres ingresados
    validar_entero = QRegExpValidator(entero)
    validar_flotante = QRegExpValidator(flotante)
    validar_descuento = QRegExpValidator(descuento)
    
    #Valida que los caracteres ingresados sean válidos
    self.ui.D_inventario.setValidator(validar_entero)
    self.ui.D_precio.setValidator(validar_flotante)
    self.ui.D_descuento.setValidator(validar_descuento)

    #Comprobar que las celdas tengan datos
    self.ui.D_sku.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_sku_2.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_producto.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_categoria.currentIndexChanged.connect(self.fn_Comprobacion)
    self.ui.D_inventario.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_precio.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_descuento.textChanged.connect(self.fn_Comprobacion)

    #Agregar Categorias en el combobox D_categoria tomando el módulo m_Constantes
    #Agregar categorias a la lista seleccionable
    for item in C.Constante_Categorias():
      self.ui.D_categoria.addItem(item)

    #Llamar función para activar botones al inicio
    self.fn_botones_acciones()
    self.fn_Comprobacion()


    #Acción de botones opcionales Nuevo / Actualizar / Eliminar
    self.ui.b_nuevo.clicked.connect(self.fn_botones_acciones)
    self.ui.b_actualizar.clicked.connect(self.fn_botones_acciones)
    self.ui.b_eliminar.clicked.connect(self.fn_botones_acciones)

    #Acción de botón b_Buscar
    self.ui.b_Buscar.clicked.connect(self.fn_Buscar)

    #Accíon del botón b_Registrar
    self.ui.b_Registrar.clicked.connect(self.fn_Registrar)
    
    #Acción de botón b_Cancelar
    self.ui.b_Cancelar.clicked.connect(self.fn_Cancelar)



  # ----------------- Funciones para uso de botones ----------------- #
  #Función para acción de optionbutton Nuevo / Actualizar / Eliminar
  def fn_botones_acciones(self):
    if self.ui.b_nuevo.isChecked():
      #Para seleccionar solo una opción
      self.ui.b_actualizar.setChecked(False)
      self.ui.b_eliminar.setChecked(False)

      #Función de comprobación de datos vacíos
      self.fn_Comprobacion()

      #Función para limpiar datos al cambiar de opción
      self.fn_Limpiar_Datos()

      #Cambiar texto de botón b_Registrar
      self.ui.b_Registrar.setText("Registrar")

    elif self.ui.b_actualizar.isChecked():
      #Para seleccionar solo una opción
      self.ui.b_nuevo.setChecked(False)
      self.ui.b_eliminar.setChecked(False)

      #Función de comprobación de celdas vacío
      self.fn_Comprobacion()

      #Función para limpiar datos al cambiar de opción
      self.fn_Limpiar_Datos()

      #Cambiar texto de botón b_Registrar
      self.ui.b_Registrar.setText("Actualizar")

    elif self.ui.b_eliminar.isChecked():
      #Para seleccionar solo una opción
      self.ui.b_nuevo.setChecked(False)
      self.ui.b_actualizar.setChecked(False)

      #Función de comprobación de celdas vacío
      self.fn_Comprobacion()

      #Función para limpiar datos al cambiar de opción
      self.fn_Limpiar_Datos()

      #Cambiar texto de botón b_Registrar
      self.ui.b_Registrar.setText("Eliminar")

  #Función que deshabilita botón Registrar si estan vacias las celdas
  def fn_Comprobacion(self):
    if self.fn_Casos() == "Nuevo":
      #Habilitar todos los cuadros de texto
      self.ui.D_sku.setEnabled(False)
      self.ui.D_sku_2.setEnabled(True)
      self.ui.D_producto.setEnabled(True)
      self.ui.D_categoria.setEnabled(True)
      self.ui.D_inventario.setEnabled(True)
      self.ui.D_precio.setEnabled(True)
      self.ui.D_descuento.setEnabled(True)
      self.ui.b_Registrar.setEnabled(True)

      #Deshabilitar botón b_Buscar
      self.ui.b_Buscar.setEnabled(False)

      #Habilitar/Deshabilitar botón b_Registrar
      self.fn_Activar_Registrar()

    elif self.fn_Casos() == "Actualizar":
      #Habilitar todos los cuadros de texto
      self.ui.D_sku.setEnabled(True)
      self.ui.D_sku_2.setEnabled(True)
      self.ui.D_producto.setEnabled(True)
      self.ui.D_categoria.setEnabled(True)
      self.ui.D_inventario.setEnabled(True)
      self.ui.D_precio.setEnabled(True)
      self.ui.D_descuento.setEnabled(True)
      self.ui.b_Registrar.setEnabled(True)

      #Deshabilitar botón b_Buscar
      self.ui.b_Buscar.setEnabled(True)

      #Habilitar/Deshabilitar botón b_Registrar
      self.fn_Activar_Registrar()

    elif self.fn_Casos() == "Eliminar":
      #Habilitar todos los cuadros de texto
      self.ui.D_sku.setEnabled(True)
      self.ui.D_sku_2.setEnabled(False)
      self.ui.D_producto.setEnabled(False)
      self.ui.D_categoria.setEnabled(False)
      self.ui.D_inventario.setEnabled(False)
      self.ui.D_precio.setEnabled(False)
      self.ui.D_descuento.setEnabled(False)
      self.ui.b_Registrar.setEnabled(False)

      #Deshabilitar botón b_Buscar
      self.ui.b_Buscar.setEnabled(True)

      #Habilitar/Deshabilitar botón b_Registrar
      self.fn_Activar_Registrar()

  def fn_Activar_Registrar(self):
    if self.fn_Casos() == "Nuevo" or self.fn_Casos() == "Actualizar":
      #Habilitar botón b_Registrar
      if (not self.ui.D_sku_2.text()
          and not self.ui.D_producto.toPlainText()
          and self.ui.D_categoria.currentIndex() == 0
          and not self.ui.D_inventario.text()
          and not self.ui.D_precio.text()
          and not self.ui.D_descuento.text()):
        self.ui.b_Registrar.setEnabled(False)
      elif (not self.ui.D_sku_2.text()
          or not self.ui.D_producto.toPlainText()
          or self.ui.D_categoria.currentIndex() == 0
          or not self.ui.D_inventario.text()
          or not self.ui.D_precio.text()
          or not self.ui.D_descuento.text()):
        self.ui.b_Registrar.setEnabled(False)
      else:
        self.ui.b_Registrar.setEnabled(True)
    elif self.fn_Casos() == "Eliminar":
      if not self.ui.D_sku.text():
        self.ui.b_Registrar.setEnabled(False)
      else:
        self.ui.b_Registrar.setEnabled(True)
  
  #Función para limpiar datos
  def fn_Limpiar_Datos(self):
    #Limpiar datos
    self.ui.D_sku_2.clear()
    self.ui.D_producto.clear()
    self.ui.D_categoria.setCurrentIndex(0)
    self.ui.D_inventario.clear()
    self.ui.D_precio.clear()
    self.ui.D_descuento.clear()

    if self.fn_Casos() == "Nuevo":
      self.ui.D_sku.clear()

  def fn_Casos(self):
    if self.ui.b_nuevo.isChecked():
      return "Nuevo"
    elif self.ui.b_actualizar.isChecked():
      return "Actualizar"
    elif self.ui.b_eliminar.isChecked():
      return "Eliminar"
  
  # --------- Funciones para Administrar acciones en SQLite --------- #
  #Función para buscar producto existente
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

  #Función para buscar productos
  def fn_Buscar(self):
    sku = self.ui.D_sku.text()
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Productos")
    miCursor = miConexion.cursor()

    #Comporbar que el producto existe en la Base de Datos
    if self.fn_Producto_Existe(sku) == "Si":
      miCursor.execute("SELECT * FROM Inventario WHERE SKU = ?", [sku])
      resultado = miCursor.fetchall()
      #Extraer datos de la lista usando la posición 0 de la lista
      datos = resultado[0]

      #Acomodar los datos en las cajas de texto
      self.ui.D_sku_2.setText(datos[0])
      self.ui.D_producto.setText(datos[1])
      self.ui.D_categoria.setCurrentText(datos[2])
      self.ui.D_inventario.setText(str(datos[3]))
      self.ui.D_precio.setText(str(datos[4]))
      self.ui.D_descuento.setText(str(datos[5]))
    else:
      self.msg_info("Producto no encontrado", f"El SKU {sku} no se encuentra en la "
                      + "Base de Datos" + '\n' + "Favor de volver a intentar")

  #Función para agregar un producto nuevo
  def fn_Producto_Nuevo(self, sku, producto, categoria, inventario, precio, descuento):
    #Comporbar que el producto existe en la Base de Datos
    if self.fn_Producto_Existe(sku) == "No":
      #Abrir Base de Datos con SQLite3
      miConexion = sqlite3.connect("Productos")
      miCursor = miConexion.cursor()
      #Registrar nuevo producto en la Base de Datos
      miCursor.execute("INSERT INTO Inventario VALUES (?, ?, ?, ?, ?, ?)", 
                       [sku, producto, categoria, inventario, precio, descuento])
      miConexion.commit()
      miConexion.close()

      self.msg_info("Producto agregado", f"El producto {sku} se ha agregado "
                    + "exitosamente a la Base de Datos")

    else:
      self.msg_info("Producto existente", f"El producto {sku} ya se encuentra en la "
                      + "Base de Datos" + '\n' + "Favor de volver a intentar")
      
  #Función para actualizar un producto
  def fn_Producto_Actualizar(self, sku, producto, categoria, inventario, precio, 
                             descuento):
    
    #Comporbar que el producto existe en la Base de Datos
    if self.fn_Producto_Existe(sku) == "Si":
      #Abrir Base de Datos con SQLite3
      miConexion = sqlite3.connect("Productos")
      miCursor = miConexion.cursor()
      miCursor.execute('''UPDATE Inventario SET Producto = ?, Categoria = ?,
                          Inventario = ?, Precio = ?, Descuento = ? WHERE SKU = ?''',
                          [producto, categoria, inventario, precio, descuento, sku])
      miConexion.commit()
      miConexion.close()
      self.msg_info("Producto actualizado", f"El producto {sku} se ha actualizado "
                    + "exitosamente en la Base de Datos")
    else:
      self.msg_info("Producto no existe", f"El producto {sku} no se encuentra en la "
                      + "Base de Datos" + '\n' + "Favor de volver a intentar")
    
  #Función para eliminar un producto
  def fn_Producto_Eliminar(self, sku):
    #self.ui.D_inventario.setText(0)
    #Comporbar que el producto existe en la Base de Datos
    if self.fn_Producto_Existe(sku) == "Si":
      #Mensaje de confirmación
        if self.msg_confirmacion("Confirmación", "¿Estas seguro que quieres "
                                 + f"eliminar al producto {sku}?") == "Eliminar":
          #Abrir Base de Datos con SQLite3
          miConexion = sqlite3.connect("Productos")
          miCursor = miConexion.cursor()
          #Eliminar artículo
          miCursor.execute("DELETE FROM Inventario WHERE SKU = ?", [sku])
          miConexion.commit()
          miConexion.close()
          #Limpiar dato de D_sku
          self.ui.D_sku.clear()
          #Limpiar datos después de eliminar
          self.fn_Limpiar_Datos()

    elif self.fn_Producto_Existe(sku) == "No":
      self.msg_info("Producto no existe", f"El producto {sku} no se encuentra en la "
                      + "Base de Datos" + '\n' + "Favor de volver a intentar")


  #Función del boton b_Resgistrar    
  def fn_Registrar(self):
    #Leer los datos de la ventana
    sku = self.ui.D_sku_2.text()
    sku_eliminar = self.ui.D_sku.text()
    producto = self.ui.D_producto.toPlainText()
    categoria = self.ui.D_categoria.currentText()
    inventario = self.ui.D_inventario.text()
    precio = self.ui.D_precio.text()
    descuento = self.ui.D_descuento.text()

    if self.fn_Casos() == "Nuevo":
      self.fn_Producto_Nuevo(sku, producto, categoria, inventario, precio, descuento)

    elif self.fn_Casos() == "Actualizar":
      self.fn_Producto_Actualizar(sku, producto, categoria, inventario, precio, descuento)

    elif self.fn_Casos() == "Eliminar":
      self.fn_Producto_Eliminar(sku_eliminar)

  #Función del boton b_Cancelar
  def fn_Cancelar(self):
    #Función de volver a ventana de Login
    self.fn_Cerrar_Ventana()

  # -------------------- Funciones para Mensajes -------------------- #
  #Función para mensajes de información
  def msg_info(self, titulo, mensaje):
      msgbox = QMessageBox()
      msgbox.setIcon(QMessageBox.Information)
      msgbox.setWindowTitle(titulo)
      msgbox.setText(mensaje)
      msgbox.exec_()    
  
  #Función para mensajes de advertencia
  def msg_confirmacion(self, titulo, mensaje):
      msgbox = QMessageBox()
      msgbox.setIcon(QMessageBox.Question)
      msgbox.setWindowTitle(titulo)
      msgbox.setText(mensaje)
      msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
      b_Si = msgbox.button(QMessageBox.Yes)
      b_Si.setText("Si")
      b_No = msgbox.button(QMessageBox.No)
      b_No.setText("No")
      msgbox.exec_()

      Respuesta = ""
      if msgbox.clickedButton() == b_Si:
        Respuesta = "Eliminar"

      elif msgbox.clickedButton() == b_No:
        Respuesta  = ""
      return Respuesta

  # ------------- Funciones para Eventos en la ventana  ------------- #
  #Evento para cuando la ventana se cierra
  def closeEvent(self, event):
    ##ventana = m_Ventas
    ##ventana.start()
    self.close()

  #Cerrar ventana
  def fn_Cerrar_Ventana(self):
    self.close()
    ##self.destroy()
    ##ventana = m_Ventas
    ##ventana.start()

#Función para iniciar ventana de Registro
def start():
    global window  
    window = Inventario_GUI()
    window.show()

##if __name__ == '__main__':
##  app = QtWidgets.QApplication([])
##  application = Inventario_GUI()
##  application.show()
##  sys.exit(app.exec())