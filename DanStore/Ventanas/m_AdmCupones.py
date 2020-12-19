#Importar librerias necesarias
import sys
import sqlite3

#Importar ventana de Login creada en QT Designes  y exportada a python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Pantallas.f_AdmCupones import Ui_MainWindow

#Libreria para poder validar si los datos son numeros, texto, enteros o flotantes
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

#Importar módulo de Ventas
import Ventanas.m_Ventas as m_Ventas

#Variable global para cambio de ventana
window = None

class AdmCupones_GUI(QtWidgets.QMainWindow):
  #Función para iniciar ventana de Inventario
  def __init__(self):
    super(AdmCupones_GUI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    #Habilitar o deshabilitar botones al iniciar
    self.ui.b_Buscar.setEnabled(True)
    self.ui.b_Registrar.setEnabled(False)
    self.ui.b_Cancelar.setEnabled(True)
    self.ui.D_cupon.setEnabled(False)

    #Tipo de datos en las cajas de texto
    #Solo se aceptan numeros de 0-100 y 2 cifras después del .
    descuento = QRegExp("(^(0*(\d{1,2}(\.\d{1,2})?)|\.\d{1,2}|100(\.0{1,2}$)?)$)")
    #Validacion de los caracteres ingresados
    validar_descuento = QRegExpValidator(descuento)
    
    #Valida que los caracteres ingresados sean válidos
    self.ui.D_descuento.setValidator(validar_descuento)

    #Comprobar que las celdas tengan datos
    self.ui.D_cupon.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_cupon_2.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_descuento.textChanged.connect(self.fn_Comprobacion)

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
      self.ui.D_cupon.setEnabled(False)
      self.ui.D_cupon_2.setEnabled(True)
      self.ui.D_descuento.setEnabled(True)
      self.ui.b_Registrar.setEnabled(True)

      #Deshabilitar botón b_Buscar
      self.ui.b_Buscar.setEnabled(False)

      #Habilitar/Deshabilitar botón b_Registrar
      self.fn_Activar_Registrar()

    elif self.fn_Casos() == "Actualizar":
      #Habilitar todos los cuadros de texto
      self.ui.D_cupon.setEnabled(True)
      self.ui.D_cupon_2.setEnabled(True)
      self.ui.D_descuento.setEnabled(True)
      self.ui.b_Registrar.setEnabled(True)

      #Deshabilitar botón b_Buscar
      self.ui.b_Buscar.setEnabled(True)

      #Habilitar/Deshabilitar botón b_Registrar
      self.fn_Activar_Registrar()

    elif self.fn_Casos() == "Eliminar":
      #Habilitar todos los cuadros de texto
      self.ui.D_cupon.setEnabled(True)
      self.ui.D_cupon_2.setEnabled(False)
      self.ui.D_descuento.setEnabled(False)
      self.ui.b_Registrar.setEnabled(False)

      #Deshabilitar botón b_Buscar
      self.ui.b_Buscar.setEnabled(True)

      #Habilitar/Deshabilitar botón b_Registrar
      self.fn_Activar_Registrar()

  def fn_Activar_Registrar(self):
    if self.fn_Casos() == "Nuevo" or self.fn_Casos() == "Actualizar":
      #Habilitar botón b_Registrar
      if (not self.ui.D_cupon_2.text()
          and not self.ui.D_descuento.text()):
        self.ui.b_Registrar.setEnabled(False)
      elif (not self.ui.D_cupon_2.text()
            or not self.ui.D_descuento.text()):
        self.ui.b_Registrar.setEnabled(False)
      else:
        self.ui.b_Registrar.setEnabled(True)
    elif self.fn_Casos() == "Eliminar":
      if not self.ui.D_cupon.text():
        self.ui.b_Registrar.setEnabled(False)
      else:
        self.ui.b_Registrar.setEnabled(True)
  
  #Función para limpiar datos
  def fn_Limpiar_Datos(self):
    #Limpiar datos
    self.ui.D_cupon_2.clear()
    self.ui.D_descuento.clear()

    if self.fn_Casos() == "Nuevo":
      self.ui.D_cupon.clear()

  def fn_Casos(self):
    if self.ui.b_nuevo.isChecked():
      return "Nuevo"
    elif self.ui.b_actualizar.isChecked():
      return "Actualizar"
    elif self.ui.b_eliminar.isChecked():
      return "Eliminar"
  
  # --------- Funciones para Administrar acciones en SQLite --------- #
  #Función para buscar producto existente
  def fn_Producto_Existe(self, cupon):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Productos")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM Inventario WHERE Cupon = ?", [cupon])
    if miCursor.fetchall():
      return "Si"
    else:
      return "No"
    miConexion.close()

  #Función para buscar productos
  def fn_Buscar(self):
    cupon = self.ui.D_cupon.text()
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Productos")
    miCursor = miConexion.cursor()

    #Comporbar que el producto existe en la Base de Datos
    if self.fn_Producto_Existe(cupon) == "Si":
      miCursor.execute("SELECT * FROM Inventario WHERE Cupon = ?", [cupon])
      resultado = miCursor.fetchall()
      #Extraer datos de la lista usando la posición 0 de la lista
      datos = resultado[0]

      #Acomodar los datos en las cajas de texto
      self.ui.D_cupon_2.setText(datos[0])
      self.ui.D_descuento.setText(str(datos[5]))
    else:
      self.msg_info("Producto no encontrado", f"El Cupon {cupon} no se encuentra en la "
                      + "Base de Datos" + '\n' + "Favor de volver a intentar")

  #Función para agregar un producto nuevo
  def fn_Producto_Nuevo(self, cupon, producto, categoria, inventario, precio, descuento):
    #Comporbar que el producto existe en la Base de Datos
    if self.fn_Producto_Existe(cupon) == "No":
      #Abrir Base de Datos con SQLite3
      miConexion = sqlite3.connect("Productos")
      miCursor = miConexion.cursor()
      #Registrar nuevo producto en la Base de Datos
      miCursor.execute("INSERT INTO Inventario VALUES (?, ?, ?, ?, ?, ?)", 
                       [cupon, producto, categoria, inventario, precio, descuento])
      miConexion.commit()
      miConexion.close()

      self.msg_info("Producto agregado", f"El producto {cupon} se ha agregado "
                    + "exitosamente a la Base de Datos")

    else:
      self.msg_info("Producto existente", f"El producto {cupon} ya se encuentra en la "
                      + "Base de Datos" + '\n' + "Favor de volver a intentar")
      
  #Función para actualizar un producto
  def fn_Producto_Actualizar(self, cupon, producto, categoria, inventario, precio, 
                             descuento):
    
    #Comporbar que el producto existe en la Base de Datos
    if self.fn_Producto_Existe(cupon) == "Si":
      #Abrir Base de Datos con SQLite3
      miConexion = sqlite3.connect("Productos")
      miCursor = miConexion.cursor()
      miCursor.execute('''UPDATE Inventario SET Producto = ?, Categoria = ?,
                          Inventario = ?, Precio = ?, Descuento = ? WHERE Cupon = ?''',
                          [producto, categoria, inventario, precio, descuento, cupon])
      miConexion.commit()
      miConexion.close()
      self.msg_info("Producto actualizado", f"El producto {cupon} se ha actualizado "
                    + "exitosamente en la Base de Datos")
    else:
      self.msg_info("Producto no existe", f"El producto {cupon} no se encuentra en la "
                      + "Base de Datos" + '\n' + "Favor de volver a intentar")
    
  #Función para eliminar un producto
  def fn_Producto_Eliminar(self, cupon):
    #self.ui.D_inventario.setText(0)
    #Comporbar que el producto existe en la Base de Datos
    if self.fn_Producto_Existe(cupon) == "Si":
      #Mensaje de confirmación
        if self.msg_confirmacion("Confirmación", "¿Estas seguro que quieres "
                                 + f"eliminar al producto {cupon}?") == "Eliminar":
          #Abrir Base de Datos con SQLite3
          miConexion = sqlite3.connect("Productos")
          miCursor = miConexion.cursor()
          #Eliminar artículo
          miCursor.execute("DELETE FROM Inventario WHERE Cupon = ?", [cupon])
          miConexion.commit()
          miConexion.close()
          #Limpiar dato de D_cupon
          self.ui.D_cupon.clear()
          #Limpiar datos después de eliminar
          self.fn_Limpiar_Datos()

    elif self.fn_Producto_Existe(cupon) == "No":
      self.msg_info("Producto no existe", f"El producto {cupon} no se encuentra en la "
                      + "Base de Datos" + '\n' + "Favor de volver a intentar")


  #Función del boton b_Resgistrar    
  def fn_Registrar(self):
    #Leer los datos de la ventana
    cupon = self.ui.D_cupon_2.text()
    cupon_eliminar = self.ui.D_cupon.text()
    descuento = self.ui.D_descuento.text()

    if self.fn_Casos() == "Nuevo":
      self.fn_Producto_Nuevo(cupon, producto, categoria, inventario, precio, descuento)

    elif self.fn_Casos() == "Actualizar":
      self.fn_Producto_Actualizar(cupon, producto, categoria, inventario, precio, descuento)

    elif self.fn_Casos() == "Eliminar":
      self.fn_Producto_Eliminar(cupon_eliminar)

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
    self.Abrir_Ventas()

  def Abrir_Ventas(self):
    ventana = m_Ventas
    ventana.start()

#Función para iniciar ventana de Registro
def start():
    global window  
    window = AdmCupones_GUI()
    window.show()

#if __name__ == '__main__':
#  app = QtWidgets.QApplication([])
#  application = AdmCupones_GUI()
#  application.show()
#  sys.exit(app.exec())