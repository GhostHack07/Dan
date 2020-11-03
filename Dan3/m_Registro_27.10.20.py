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
    
    ##Habilitar o deshabilitar botones al iniciar
    self.ui.b_Registrar.setEnabled(False)
    self.ui.b_Cancelar.setEnabled(True)
    self.ui.b_emp.setChecked(True)
    self.ui.b_adm.setChecked(False)

    #Comprobar que las celdas tengan datos
    self.ui.D_usuario.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_psw.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_psw_2.textChanged.connect(self.fn_Comprobacion)

    #Acción de botones opcionales
    self.ui.b_emp.clicked.connect(self.fn_botones_nivel)

    #Acción de botón b_Cancelar
    self.ui.b_Cancelar.clicked.connect(self.fn_Cancelar)

    #Accíon del botón b_Registrar
    self.ui.b_Registrar.clicked.connect(self.fn_Registrar)

  #Funciones de los botones de opción
  def fn_botones_nivel(self):
    if self.ui.b_emp.isChecked():
      self.ui.b_adm.setChecked(False)
    else:
      self.ui.b_emp.setChecked(True)

  #Función del boton b_Cancelar
  def fn_Cancelar(self):
    sys.exit()
  
  #Función del boton b_Registrar
  def fn_Registrar(self):
    #Leer datos ingresados
    User = self.ui.D_usuario.text()
    Password = self.ui.D_psw.text()
    Confirmacion = self.ui.D_psw_2.text()
    #Revisar Nivel de usuario seleccionado
    if self.ui.b_emp.isChecked():
      Nivel = "Empleado"
    else:
      Nivel = "Administrador" 
    
    #Comprobar que la contraseña y confirmación sean iguales
    if Password == Confirmacion:
      #Abrir Base de Datos con SQLite3
      miConexion = sqlite3.connect("Usuarios")
      miCursor = miConexion.cursor()

      #Verificar si el usiario ya existe
      #miCursor.execute("SELECT * FROM USUARIOS WHERE Usuario = ?", (User,))
      #miCursor.execute("SELECT Usuario FROM USUARIOS WHERE Usuario = ?", (User,))
      miCursor.execute("SELECT count(*) FROM USUARIOS WHERE Usuario = ?", [User])
      a = miCursor.fetchall()
      b = len(a)
      c = a[0]
      print(a)
      print(b)
      print(c)

      print(a[0])

      print(type(a))
      print(type(b))
      print(type(c))

      if 0 in a:
        print("Si esta")
      else:
        print("No esta")

      #if miCursor.fetchall() > [0]:
      if (len(miCursor.fetchall()) > 0):
        print("Usuario existente")
      else:
        print("Usuario nuevo")
      
      miConexion.close
      #Ingresar nuevo usuario y contraseña a la Base de Datos

    else:
      self.msg_info("Contraseña inválida", "La contraseña y su confirmación no "
                    + "coinciden" + '\n' + "Favor de volver a intentar")

  #Función que deshabilita botón Registrar si estan vacias las celdas
  def fn_Comprobacion(self):
    if (not self.ui.D_usuario.text()
      and not self.ui.D_psw.text()
      and not self.ui.D_psw_2.text()):
      self.ui.b_Registrar.setEnabled(False)
    elif (not self.ui.D_usuario.text()
      or not self.ui.D_psw.text()
      or not self.ui.D_psw_2.text()):
      self.ui.b_Registrar.setEnabled(False)
    else:
      self.ui.b_Registrar.setEnabled(True)
      #self.msg_info("Sin datos...", "Las celdas están vacías"
      #              + '\n' + "Favor de introducir datos")
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


      #Comprobar que los campos no esten vacíos
    #if (not self.ui.D_usuario.text()
    #  and not self.ui.D_psw.text()
    #  and not self.ui.D_psw_2.text()):
    #  self.msg_info("Sin datos...", "Las celdas están vacías"
    #                + '\n' + "Favor de introducir datos")
    #if (not self.ui.D_usuario.text()
    #  or not self.ui.D_psw.text()
    #  or not self.ui.D_psw_2.text()):
    #  self.ui.b_Registrar.setEnabled(False)
    #if (self.ui.D_usuario.text()
    #  or self.ui.D_psw.text()
    #  or self.ui.D_psw_2.text()):
    #  self.ui.b_Registrar.setEnabled(True)
    #else:
    #  self.ui.b_Registrar.setEnabled(True)
      #self.msg_info("Datos incompletos...", "Todas las celdas deben estar llenas"
      #              + '\n' + "Favor de introducir todos los datos")
      #Comporbar que la contraseña y la confirmación sean iguales
    #elif (not self.ui.D_usuario.text()
    #  and self.ui.D_psw.text() == self.ui.D_psw_2.text()):
    #  self.msg_info("Exito", "Exito    ")
  
  #Habilitar o deshabilitar botones al inicio
  #def fn_botones_inicio(self):
  #  self.ui.b_Registrar.setEnabled(False)
  #  self.ui.b_Cancelar.setEnabled(True)
  #  self.ui.b_emp.setChecked(True)
  #  self.ui.b_adm.setChecked(False)