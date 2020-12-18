#Importar librerias necesarias
import sys
import sqlite3

#Importar ventana de Login creada en QT Designes  y exportada a python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Pantallas.f_Cantidad import Ui_MainWindow

#Importar módulo de ventana de Registro
import Ventanas.m_Productos as m_Productos

#Variable global para cambio de ventana
window = None

class Cantidad_GUI(QtWidgets.QMainWindow):
  #Función para iniciar ventana de Login
  def __init__(self):
    super(Cantidad_GUI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    #Comprobar que las celdas tengan datos

    #Acción de botones
    self.ui.b_Cancelar.clicked.connect(self.fn_Cancelar)
    self.ui.b_Aceptar.clicked.connect(self.fn_Aceptar)

  def fn_Aceptar(self):
    #Borrar cantidad de la Base de Datos temporal
    self.fn_Limpiar_BD()

    cantidad = self.ui.D_cantidad.value()
    
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Productos")
    miCursor = miConexion.cursor()
    #Crear Base de Datos si no existe
    miCursor.execute('''
      CREATE TABLE IF NOT EXISTS Cantidad (
      Cantidad INTEGER(4))
      ''')

    #Agregar valor en la tabla temporal
    miCursor.execute("INSERT INTO Cantidad VALUES (?)", [cantidad])
    miConexion.commit()
    miConexion.close()
    
    #Cerrar ventana
    self.fn_Cerrar_Ventana()

  def fn_Cancelar(self):
    #Función de volver a ventana de Login
    self.fn_Cerrar_Ventana()

  def fn_Limpiar_BD(self):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Productos")
    miCursor = miConexion.cursor()

    #Borrar valores de la Base de Datos temporal para la cantidad
    miCursor.execute("DELETE FROM Cantidad")
    miConexion.commit()
  

  # ------------- Funciones para Eventos en la ventana  ------------- #
  #Evento para cuando la ventana se cierra
  def closeEvent(self, event):
    self.destroy()
    self.fn_Cerrar_Ventana

  #Cerrar ventana
  def fn_Cerrar_Ventana(self):
    self.destroy()
    #ventana = m_Productos
    #ventana.start()


#Función para iniciar ventana de Ventas
def start():
    global window  
    window = Cantidad_GUI()
    window.show()



#Mostrar ventana Login
if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  application = Cantidad_GUI()
  application.show()
  sys.exit(app.exec())