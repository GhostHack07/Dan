#Importar librerias necesarias
import sys
import sqlite3

#Importar ventana de Login creada en QT Designes  y exportada a python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Pantallas.f_Login import Ui_MainWindow

from PyQt5 import Qt

#Importar módulo de ventana de Registro
import Ventanas.m_Registro as m_Registro
import Ventanas.m_Ventas as m_Ventas

#Variable global para cambio de ventana
window = None

###-------------------------------- USAR SOLO PARA PRUEBAS --------------------------------###

##Manejo de Base de datos con SQLite3
#miConexion = sqlite3.connect("Usuarios")
#miCursor = miConexion.cursor()
##Crear Base de Datos si no existe
#miCursor.execute('''
#  CREATE TABLE IF NOT EXISTS USUARIOS (
#  Usuario VARCHAR(10) PRIMARY KEY,
#  PSW VARCHAR(10))
#''')
##Cerrar conexión de la Base de Datos
#miConexion.close()

##Ejemplo para introducir usuario desde el código

#miCursor.execute("INSERT INTO USUARIOS VALUES ('Daniel', '1234')")
#miConexion.commit()

###-------------------------------- USAR SOLO PARA PRUEBAS --------------------------------###

##Cerrar conexión de la Base de Datos
#miConexion.close()

#Contador para dar al usuario 3 intentos
intento = 3

#Leer y cargar ventan creada con QT Designer y exportada a Python
class Login_GUI(QtWidgets.QMainWindow):
  #Función para iniciar ventana de Login
  def __init__(self):
    super(Login_GUI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    #Habilitar o deshabilitar botones
    self.ui.b_Entrar.setEnabled(False)
    self.ui.b_Cancelar.setEnabled(True)
    self.ui.b_Registrar.setEnabled(False)

    #Acción de botón b_Cancelar
    self.ui.b_Cancelar.clicked.connect(self.fn_Cancelar)
    #Accíon del botón b_Entrar
    self.ui.b_Entrar.clicked.connect(self.fn_Entrar)
    #Accion del botón b_Registrar
    self.ui.b_Registrar.clicked.connect(self.Abrir_Registrar)

    #Comprobar que las celdas tengan datos
    self.ui.D_usuario.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_psw.textChanged.connect(self.fn_Comprobacion)

  
  #Función que deshabilita botón Entrar y Registrar si estan vacias las celdas
  def fn_Comprobacion(self):
    if (not self.ui.D_usuario.text() and not self.ui.D_psw.text()):
      self.ui.b_Entrar.setEnabled(False)
      self.ui.b_Registrar.setEnabled(False)
    elif (not self.ui.D_usuario.text() or not self.ui.D_psw.text()):
      self.ui.b_Entrar.setEnabled(False)
      self.ui.b_Registrar.setEnabled(False)
    else:
      self.ui.b_Entrar.setEnabled(True)
      self.ui.b_Registrar.setEnabled(True)

  #Función para abrir formulario de Registro
  def Abrir_Registrar(self):
    #Leer datos ingresados
    User = self.ui.D_usuario.text()
    Password = self.ui.D_psw.text()
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute('''SELECT * FROM USUARIOS WHERE Usuario = ? AND PSW = ? 
                        AND Nivel = "Administrador" ''', [User, Password])
    
    #Abrir registro de usuarios si se tienen derechos de administrador
    if miCursor.fetchall():
      self.hide()
      ventana = m_Registro
      ventana.start()
    else:
      self.msg_warning("Sin derechos de acceso", "Verificar que el usuario y contraseña "
                       + "sean correctos y" + '\n' + "que tengas nivel de administrador." 
                        + '\n' + "Favor de volver a intentar")

  #Función del boton b_Cancelar
  def fn_Cancelar(self):
    #self.destroy()
    sys.exit()
  
  #Función del boton b_Entrar
  def fn_Entrar(self):
    #Leer datos ingresados
    User = self.ui.D_usuario.text()
    Password = self.ui.D_psw.text()
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    #Crear Base de Datos si no existe
    miCursor.execute('''
      CREATE TABLE IF NOT EXISTS USUARIOS (
      Usuario VARCHAR(10) PRIMARY KEY,
      PSW VARCHAR(10),
      Nivel VARCHAR(15))
      ''')
    
    #Contador para dar al usuario 3 intentos
    global intento
    #Leer los datos de la Base de Datos y comparar 
    miCursor.execute("SELECT * FROM USUARIOS WHERE Usuario = ? AND PSW = ?",
                    (User, Password))
    if miCursor.fetchall() and intento <=3:
      
      ##self.msg_info("Login correcto", "Bienvenido " + User)
      miConexion.close()

      self.fn_temporal(User)

      self.Abrir_Ventas()

    else:
      #Descontar intentos
      intento = intento - 1
      if intento == 0:
        self.msg_warning("Login incorrecto", "Se agotaron los intentos")
        self.fn_Cancelar()
      else:
        self.msg_warning("Login incorrecto", "Usuario y contraseña incorrectos" 
                        + '\n' + f"Te quedan {intento} intentos")

  #Función para mensajes de Información
  def msg_info(self, titulo, mensaje):
      msgbox = QMessageBox()
      msgbox.setIcon(QMessageBox.Information)
      msgbox.setWindowTitle(titulo)
      msgbox.setText(mensaje)
      msgbox.exec_()
  
  #Función para mensajes de Advertencia
  def msg_warning(self, titulo, mensaje):
      msgbox = QMessageBox()
      msgbox.setIcon(QMessageBox.Warning)
      msgbox.setWindowTitle(titulo)
      msgbox.setText(mensaje)
      msgbox.exec_()

  #Función para crear Base de Datos Temporal
  def fn_temporal(self, User):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    #Crear Base de Datos si no existe
    miCursor.execute('''
      CREATE TABLE IF NOT EXISTS TEMP (
      Usuario VARCHAR(10),
      Nivel VARCHAR(15))
      ''')

    #Eliminar cualquier usuario en tabla temporal
    miCursor.execute("DELETE FROM TEMP")
    miConexion.commit()

    #Insertar valor de Usuario y Nivel en tabla temporal
    miCursor.execute('''INSERT INTO TEMP (Usuario, Nivel)
                        SELECT Usuario, Nivel FROM USUARIOS WHERE Usuario = ?''' , [User])
    miConexion.commit()
    miConexion.close()

  #Funciones para abrir otras ventanas
  def Abrir_Ventas(self):
    self.destroy()
    ventana = m_Ventas
    ventana.start()

  def closeEvent(self, event):
    self.fn_Cancelar()

#Función para iniciar ventana de Login
def start():
    global window  
    window = Login_GUI()
    window.show()



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