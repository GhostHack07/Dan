#Importar librerias necesarias
import sys
import sqlite3

#Importar ventana de Login creada en QT Designes y exportada a python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Pantallas.f_Cupon import Ui_MainWindow

#Libreria para poder validar si los datos son numeros, texto, enteros o
#flotantes
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

#Importar módulo de Ventas
import Ventanas.m_AdmCupones as m_AdmCupones

#Variable global para cambio de ventana
window = None

class Cupon_GUI(QtWidgets.QMainWindow):
  #Función para iniciar ventana de Login
  def __init__(self):
    super(Cupon_GUI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    #Habilitar o deshabilitar botones al iniciar
    self.ui.b_Aplicar.setEnabled(False)
    self.ui.b_Cancelar.setEnabled(True)

    #Comprobar que las celdas tengan datos
    self.ui.D_Cupon.textChanged.connect(self.fn_Comprobacion)



    # ------------------- Acciones para  botones ------------------- #
    #Acción de botón b_Cancelar
    self.ui.b_Cancelar.clicked.connect(self.fn_Cancelar)
    #Acción de botón b_Aplicar
    self.ui.b_Aplicar.clicked.connect(self.fn_Aplicar)
    #Accion de boton b_Administrar
    self.ui.b_Administrar.clicked.connect(self.Abrir_AdmCupones)

  

  def fn_Comprobacion(self):
    if not self.ui.D_Cupon.text():
      self.ui.b_Aplicar.setEnabled(False)
    else:
      self.ui.b_Aplicar.setEnabled(True)


  #Función del boton b_Cancelar
  def fn_Cancelar(self):
    self.fn_Cerrar_Ventana()


  # --------- Funciones para Administrar acciones en SQLite --------- #
  def fn_Aplicar(self):
    cupon = self.ui.D_Cupon.text()
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Ventas")
    miCursor = miConexion.cursor()

    miCursor.execute('''
      CREATE TABLE IF NOT EXISTS Cupones (
      Cupon VARCHAR(5) PRIMARY KEY,
      Descuento REAL(4))
      ''')

    if self.fn_Cupon_Existente(cupon) == "Si":
      self.fn_Aplicar_Descuento(cupon)
      self.msg_info("Cupón Aplicado", f"El cupón {cupon} se aplicó exitosamente")

    elif self.fn_Cupon_Existente(cupon) == "No":
      self.msg_info("Cupón Inexistente", f"El cupón {cupon} no se encuentra registrado"
                       + '\n' + "Favor de volver a intentar")

  def fn_Cupon_Existente(self, cupon):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Ventas")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM Cupones WHERE Cupon = ?", [cupon])
    if miCursor.fetchall():
      return "Si"
    else:
      return "No"
    miConexion.close()

  def fn_Descuento(self, cupon):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Ventas")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT Descuento FROM Cupones WHERE Cupon = ?", [cupon])
    Descuento = miCursor.fetchone()[0]
    miConexion.close()

    return Descuento

  def fn_Aplicar_Descuento(self, cupon):
    Descuento = self.fn_Descuento(cupon)
    print (Descuento)
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Productos")
    miCursor = miConexion.cursor()

    #Aplicar descuento adicional en la Base de Datos temporal
    miCursor.execute("UPDATE TEMP SET Cupon = ?", [Descuento])
    miConexion.commit()
    miConexion.close()


  def fn_Acceso_Administrar(self):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    #Conusltar datos en la Base de Datos temporal
    miCursor.execute("SELECT Usuario, Nivel FROM TEMP LIMIT 0, 1")
    #Extraer el usuario del renglon 1 en formato de Lista
    r = miCursor.fetchall()[0]
    #Extraer datos de la lista usando la posición 0 de la lista
    Datos = r[1]
    #Cerrar conexion de Base de Datos
    miConexion.close()
    #La fucnion adquiere el valor de Datos en forma de Tupla
    return Datos


  # -------------------- Funciones para Mensajes -------------------- #
  #Función para mensajes de información
  def msg_info(self, titulo, mensaje):
      msgbox = QMessageBox()
      msgbox.setIcon(QMessageBox.Information)
      msgbox.setWindowTitle(titulo)
      msgbox.setText(mensaje)
      msgbox.exec_()   


  # ----------------- Funciones para Abrir Ventanas ----------------- #
  def Abrir_AdmCupones(self):
    
    #Comproabr que se tengan derechos de administrador
    if self.fn_Acceso_Administrar() == "Administrador":
      self.destroy()
      ventana = m_AdmCupones
      ventana.start()
    else:
      self.msg_info("Sin derechos de acceso", "No tienes nivel de administrador para"
                       + '\n' + "hacer modificaciones en los cupones")
    


  # ------------- Funciones para Eventos en la ventana ------------- #
  #Evento para cuando la ventana se cierra
  def closeEvent(self, event):
    self.fn_Cerrar_Ventana()

  #Cerrar ventana
  def fn_Cerrar_Ventana(self):
    self.destroy()


#Función para iniciar ventana de Cobro
def start():
    global window  
    window = Cupon_GUI()
    window.show()


#Mostrar ventana Login
if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  application = Cupon_GUI()
  application.show()
  sys.exit(app.exec())