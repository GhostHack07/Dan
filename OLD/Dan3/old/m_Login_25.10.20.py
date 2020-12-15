#Importar librerias necesarias
import sys
import sqlite3

#Importar ventana de Login creada en QT Designes  y exportada a python
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from f_Login import Ui_MainWindow
#Importar cuadros de dialogo de tkinter
from tkinter import messagebox

#Manejo de Base de datos con SQLite3
miConexion = sqlite3.connect("Usuarios")
miCursor = miConexion.cursor()
#Crear Base de Datos si no existe
miCursor.execute('''
  CREATE TABLE IF NOT EXISTS USUARIOS (
  Usuario VARCHAR(10) PRIMARY KEY,
  PSW VARCHAR(10))
''')

###-------------------------------- USAR SOLO PARA PRUEBAS --------------------------------###
##Ejemplo para introducir usuario desde el código

#miCursor.execute("INSERT INTO USUARIOS VALUES ('Daniel', '1234')")
#miConexion.commit()

###-------------------------------- USAR SOLO PARA PRUEBAS --------------------------------###

##Cerrar conexión de la Base de Datos
#miConexion.close()

#Leer y cargar ventan creada con QT Designer y exportada a Python
class Login_GUI(QtWidgets.QMainWindow):
  def __init__(self):
    super(Login_GUI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    #Habilitar o deshabilitar botones
    self.ui.b_Entrar.setEnabled(True)
    self.ui.b_Cancelar.setEnabled(True)
    self.ui.b_Registrar.setEnabled(True)
    #Acción de botón b_Cancelar
    self.ui.b_Cancelar.clicked.connect(self.fn_Cancelar)
    #Accíon del botón b_Entrar
    self.ui.b_Entrar.clicked.connect(self.fn_Entrar)
  #Función del boton b_Cancelar
  def fn_Cancelar(self):
    sys.exit()
  #Función del boton b_Entrar
  def fn_Entrar(self):
    User = self.ui.D_usuario.text()
    Password = self.ui.D_psw.text()
    #Datos = [(User, Password)]
    #Leer los datos de la Base de Datos y comparar 
    miCursor.execute("SELECT * FROM USUARIOS WHERE Usuario = ? AND PSW = ?", (User, Password))
    if miCursor.fetchall():
      self.msg_info("Login correcto", "Bienvenido")
      #messagebox.showinfo(title = "Login correcto", message = ("Bienvenido", User))
    else:
      #msg = QMessageBox()
      #msg.setIcon(QMessageBox.Information)
      #msg.setText("Usuario y contraseña incorrectos")
      #msg.setWindowTitle("Login incorrecto")
      messagebox.showerror(title = "Login incorrecto", message = "Usuario y contraseña incorrectos")
    miConexion.close
    sys.exit()
  def msg_info(self, titulo, mensaje):
      msgbox = QMessageBox()
      msgbox.setIcon(QMessageBox.Information)
      msgbox.setWindowTitle(titulo)
      msgbox.setText(mensaje)
      msgbox.setFixedWidth(1000)
      #msgbox.setStandardButtons(QtGui.QMessageBox.Ok)
      msgbox.exec_()


#Mostrar ventana Login
if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  application = Login_GUI()
  application.show()
  sys.exit(app.exec())



  #Datos = [(Usuario, Password)]
  #  #Leer los datos de la Base de Datos y comparar 
  #  miCursor.executemany("INSERT INTO USUARIOS VALUES (?, ?)", Datos)
  #  miConexion.commit()
  #  miConexion.close