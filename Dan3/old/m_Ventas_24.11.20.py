#Importar librerias necesarias
import sys
import sqlite3

#Importar ventana de Login creada en QT Designes  y exportada a python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from f_Ventas import Ui_MainWindow

#Importar módulo de Login
import m_Login
import m_Registro


#Variable global para cambio de ventana
window = None

class Ventas_GUI(QtWidgets.QMainWindow):
  #Función para iniciar ventana de Login
  def __init__(self):
    super(Ventas_GUI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    #Habilitar o deshabilitar botones al iniciar
    self.ui.b_Actualizar.setEnabled(False)
    self.ui.b_Actualizar.setStyleSheet('''background-color: rgb(240, 240, 240);
                                          border-width: 1px;
                                          border-style: solid;
                                          border-color: gray;
                                          border-radius: 14px;''')
    self.ui.b_Eliminar.setEnabled(False)
    self.ui.b_Eliminar.setStyleSheet('''background-color: rgb(240, 240, 240);
                                          border-width: 1px;
                                          border-style: solid;
                                          border-color: gray;
                                          border-radius: 14px;''')
    self.ui.b_Cancelar.setEnabled(False)
    self.ui.b_Cancelar.setStyleSheet('''background-color: rgb(240, 240, 240);
                                          border-width: 1px;
                                          border-style: solid;
                                          border-color: gray;
                                          border-radius: 14px;''')
    self.ui.b_Cobrar.setEnabled(False)
    self.ui.b_Cobrar.setStyleSheet('''background-color: rgb(240, 240, 240);
                                          border-width: 1px;
                                          border-style: solid;
                                          border-color: gray;
                                          border-radius: 14px;''')

    self.ui.b_Cerrar.setStyleSheet('''QPushButton::active {
                                      background-color: rgb(240, 240, 240);
                                      border-width: 1px;
                                      border-style: solid;
                                      border-color: gray;
                                      border-radius: 14px;
                                      }
                                      QPushButton::hover {
                                      background-color : rgb(250, 200, 170);
                                      border-width: 1px;
                                      border-style: solid;
                                      border-color: darkred;
                                      border-radius: 14px;
                                      }
                                      QPushButton::pressed {
                                      background-color : darkorange;
                                      border-width: 1px;
                                      border-style: solid;
                                      border-color: darkred;
                                      border-radius: 14px;
                                      }''')

    self.ui.b_Usuarios.setEnabled(False)
    self.ui.b_Cupon.setEnabled(False)
    self.ui.b_Inventario.setEnabled(False)
    self.ui.b_Ticket.setEnabled(False)
    #self.ui.b_Cerrar.setEnabled(False)
    
    #Deshabilitar las cajas de texto
    self.ui.t_Ticket.setEnabled(False)
    self.ui.t_Importe.setEnabled(False)
    self.ui.t_Descuento.setEnabled(False)
    self.ui.t_IVA.setEnabled(False)
    self.ui.t_Total.setEnabled(False)
    self.ui.t_Ventas.setEnabled(False)

    #Acción de botones
    self.ui.b_Cerrar.clicked.connect(self.Abrir_Login)

  def Boton(self):
    self.ui.b_Cerrar.setStyleSheet('''border-width: 1px;
                                      border-style: solid;
                                      border-color: gray;
                                      border-radius: 14px;''')
    
  
  # ----------------- Funciones para Abrir Ventanas ----------------- #
  def Abrir_Login(self):
    self.destroy()
    ventana = m_Login
    ventana.start()

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

#Función para iniciar ventana de Ventas
def start():
    global window  
    window = Ventas_GUI()
    window.show()
#Función para iniciar ventana de Registro 
if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  application = Ventas_GUI()
  application.show()
  sys.exit(app.exec())