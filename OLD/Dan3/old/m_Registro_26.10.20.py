#Importar librerias necesarias
import sys
import sqlite3

#Importar ventana de Login creada en QT Designes  y exportada a python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from f_Registro import Ui_MainWindow
class Registro_GUI(QtWidgets.QMainWindow):
  #Función para iniciar ventana de Login
  def __init__(self):
    super(Registro_GUI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    #Habilitar o deshabilitar botones
    self.ui.b_Registrar.setEnabled(False)
    self.ui.b_Cancelar.setEnabled(True)
    self.ui.b_emp.setChecked(True)
    self.ui.b_adm.setChecked(False)
    #Acción de botones opcionales
    self.ui.b_emp.clicked.connect(self.fn_botones_nivel)
    #Acción de botón b_Cancelar
    self.ui.b_Cancelar.clicked.connect(self.fn_Cancelar)
    #Accíon del botón b_Registrar
    self.ui.b_Registrar.clicked.connect(self.fn_Registrar)
  def fn_botones_nivel(self):
    if self.ui.b_emp.isChecked():
      self.ui.b_adm.setChecked(False)
    else:
      self.ui.b_emp.setChecked(True)
  #Función del boton b_Cancelar
  def fn_Cancelar(self):
    sys.exit()
  def fn_Registrar(self):
    #Abrir Base de datos con SQLite3
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    #Comprobar que los campos no esten vacíos
    #if (not self.ui.D_usuario.text()
    #  and not self.ui.D_psw.text()
    #  and not self.ui.D_psw_2.text()):
    #  self.msg_info("Sin datos...", "Las celdas están vacías"
    #                + '\n' + "Favor de introducir datos")
    if (not self.ui.D_usuario.text()
      or not self.ui.D_psw.text()
      or not self.ui.D_psw_2.text()):
      self.ui.b_Registrar.setEnabled(False)
    if (self.ui.D_usuario.text()
      or self.ui.D_psw.text()
      or self.ui.D_psw_2.text()):
      self.ui.b_Registrar.setEnabled(True)
    #else:
    #  self.ui.b_Registrar.setEnabled(True)
      #self.msg_info("Datos incompletos...", "Todas las celdas deben estar llenas"
      #              + '\n' + "Favor de introducir todos los datos")
      #Comporbar que la contraseña y la confirmación sean iguales
    elif (not self.ui.D_usuario.text()
      and self.ui.D_psw.text() == self.ui.D_psw_2.text()):
      self.msg_info("Exito", "Exito    ")

  def msg_info(self, titulo, mensaje):
      msgbox = QMessageBox()
      msgbox.setIcon(QMessageBox.Information)
      msgbox.setWindowTitle(titulo)
      msgbox.setText(mensaje)
      msgbox.exec_()      
if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  application = Registro_GUI()
  application.show()
  sys.exit(app.exec())
