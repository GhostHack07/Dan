#Importar librerias necesarias
import sys
import sqlite3

#Importar ventana de Login creada en QT Designes  y exportada a python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from f_Inventario import Ui_MainWindow

#Importar módulo m_Ventas
import m_Ventas

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
    
    #Comprobar que las celdas tengan datos
    self.ui.D_sku_2.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_producto.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_categoria.currentIndexChanged.connect(self.fn_Comprobacion)

    #---------------PRUEBA ------------------
    self.ui.D_categoria.addItem("Item 2")
    self.ui.D_categoria.addItem("Item 3")

    #---------------PRUEBA ------------------


    #Llamar función para activar botones al inicio
    self.fn_botones_acciones()
    #self.fn_Comprobacion()


    #Acción de botones opcionales Nuevo / Actualizar / Eliminar
    self.ui.b_nuevo.clicked.connect(self.fn_botones_acciones)
    self.ui.b_actualizar.clicked.connect(self.fn_botones_acciones)
    self.ui.b_eliminar.clicked.connect(self.fn_botones_acciones)

    #Acción de botón b_Buscar
    self.ui.b_Buscar.clicked.connect(self.fn_Buscar)

    #Acción de botón b_Cancelar
    self.ui.b_Cancelar.clicked.connect(self.fn_Cancelar)

  # ----------------- Funciones para uso de botones ----------------- #
  #Función para acción de optionbutton Nuevo / Actualizar / Eliminar
  def fn_botones_acciones(self):
    if self.ui.b_nuevo.isChecked():
      #Para seleccionar solo una opción
      self.ui.b_actualizar.setChecked(False)
      self.ui.b_eliminar.setChecked(False)
      print ("nuevo")

      #Cambiar texto de botón b_Registrar
      self.ui.b_Registrar.setText("Registrar")

    elif self.ui.b_actualizar.isChecked():
      #Para seleccionar solo una opción
      self.ui.b_nuevo.setChecked(False)
      self.ui.b_eliminar.setChecked(False)
      print ("actualizar")

      #Cambiar texto de botón b_Registrar
      self.ui.b_Registrar.setText("Actualizar")

    elif self.ui.b_eliminar.isChecked():
      #Para seleccionar solo una opción
      self.ui.b_nuevo.setChecked(False)
      self.ui.b_actualizar.setChecked(False)
      print ("actualizar")

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
      self.ui.D_precio.setEnabled(True)
      self.ui.D_descuento.setEnabled(True)
      self.ui.b_Registrar.setEnabled(True)

      #Deshabilitar botón b_Buscar
      self.ui.b_Buscar.setEnabled(False)

      #print (self.ui.D_categoria.currentIndex())
      #print (self.ui.D_categoria.currentData())
      #print (self.ui.D_categoria.currentText())
      #print (self.ui.D_categoria.itemText(1))
      #print (self.ui.D_categoria.count())
      #print ("")

      ##Habilitar botón b_Registrar
      #if (not self.ui.D_sku_2.text()
      #    and not self.ui.D_producto.toPlainText()
          
      #    and not self.ui.D_inventario.text()
      #    and not self.ui.D_precio.text()
      #    and not self.ui.D_descuento.text()):
      #  self.ui.b_Registrar.setEnabled(False)

      #elif (not self.ui.D_sku_2.text()
      #    or not self.ui.D_producto.setPlainText()
          
      #    or not self.ui.D_inventario.text()
      #    or not self.ui.D_precio.text()
      #    or not self.ui.D_descuento.text()):
      #  self.ui.b_Registrar.setEnabled(False)

      ##Habilitar botón b_Registrar
      #if (not self.ui.D_producto.toPlainText()):
      #  self.ui.b_Registrar.setEnabled(False)
      if self.ui.D_categoria.currentIndex() == 0:
        self.ui.b_Registrar.setEnabled(False)
        print ("if")
        print (self.ui.D_categoria.currentIndex())

        
        #print (self.ui.D_categoria.currentText)

      else:
        self.ui.b_Registrar.setEnabled(True)
        print ("else")
        print (self.ui.D_categoria.currentIndex())


      #print (self.ui.D_categoria.currentIndex)
      #print (self.ui.D_categoria.currentData)



    elif self.fn_Casos() == "Actualizar":
      #Deshabilitar botón b_Registrar
      self.ui.b_Buscar.setEnabled(True)
      
      #Habilitar todos los cuadros de texto
      self.ui.D_sku.setEnabled(True)
      self.ui.D_sku_2.setEnabled(True)
      self.ui.D_producto.setEnabled(True)
      self.ui.D_categoria.setEnabled(True)
      self.ui.D_precio.setEnabled(True)
      self.ui.D_descuento.setEnabled(True)
      self.ui.b_Registrar.setEnabled(True)

    elif self.fn_Casos() == "Eliminar":
      #Deshabilitar botón b_Registrar
      self.ui.b_Buscar.setEnabled(False)
      
      #Habilitar todos los cuadros de texto
      self.ui.D_sku.setEnabled(False)
      self.ui.D_sku_2.setEnabled(False)
      self.ui.D_producto.setEnabled(False)
      self.ui.D_categoria.setEnabled(False)
      self.ui.D_precio.setEnabled(False)
      self.ui.D_descuento.setEnabled(False)
      self.ui.b_Registrar.setEnabled(False)

  def fn_Casos(self):
    if self.ui.b_nuevo.isChecked():
      return "Nuevo"
    elif self.ui.b_actualizar.isChecked():
      return "Actualizar"
    elif self.ui.b_eliminar.isChecked():
      return "Eliminar"


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
      print (datos)

      #self.onlyInt = QIntValidator()
      self.ui.D_inventario.setValidator(self.onlyInt)

      #Acomodar los datos en las cajas de texto
      self.ui.D_sku_2.setText(datos[0])
      self.ui.D_producto.setText(datos[1])
      #self.ui.D_categoria.setText(datos[2])
      self.ui.D_inventario.setText(str(datos[3]))
      self.ui.D_precio.setText(str(datos[4]))
      self.ui.D_descuento.setText(str(datos[5]))
    else:
      self.msg_info("Producto no encontrado", f"El SKU {sku} no se encuentra en la "
                      + "Base de Datos" + '\n' + "Favor de volver a intentar")



    
    #print (resultado)
    #if miCursor.fetchall():
    #  #Extraer la lista de datos del SKU correspondiente
    #  resultado = miCursor.fetchall()
    #  print (resultado)
    #  print (sku)
      
      ##Extraer datos de la lista usando la posición 0 de la lista
      #datos = resultado[0]
      #print (datos)
      
      ##Acomodar los datos en las cajas de texto
      #self.ui.D_sku_2.setText(datos[0])
      #self.ui.D_producto.setText(datos[1])
      #self.ui.D_categoria.setText(datos[2])
      #self.ui.D_inventario.setText(datos[3])
      #self.ui.D_precio.setText(datos[4])
      #self.ui.D_descuento.setText(datos[5])
    
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
      
  
      
  #Función del boton b_Cancelar
  def fn_Cancelar(self):
    #Función de volver a ventana de Login
    #self.fn_Cerrar_Ventana()
    #----- TEMPORAL-----
    self.close()


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
  #  ventana = m_Ventas
  #  ventana.start()
  #----- TEMPORAL-----
    self.close()

  #Cerrar ventana
  def fn_Cerrar_Ventana(self):
    self.destroy()
    ventana = m_Ventas
    ventana.start()

#Función para iniciar ventana de Registro
def start():
    global window  
    window = Inventario_GUI()
    window.show()

if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  application = Inventario_GUI()
  application.show()
  sys.exit(app.exec())