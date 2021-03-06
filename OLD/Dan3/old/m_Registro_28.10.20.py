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
    self.ui.b_nuevo.setChecked(True)
    self.ui.b_actualizar.setChecked(False)
    self.ui.b_eliminar.setChecked(False)
    #Función para activar botones al inicio
    #if self.ui.b_nuevo.isChecked():
    self.fn_botones_acciones()
    self.fn_Comprobacion()

    #Comprobar que las celdas tengan datos
    self.ui.D_usuario.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_psw_old.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_psw.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_psw_2.textChanged.connect(self.fn_Comprobacion)

    #Acción de botones opcionales Empleado / Administrador
    self.ui.b_emp.clicked.connect(self.fn_botones_nivel)
    self.ui.b_adm.clicked.connect(self.fn_botones_nivel)

    #Acción de botones opcionales Empleado / Administrador
    self.ui.b_nuevo.clicked.connect(self.fn_botones_acciones)
    self.ui.b_actualizar.clicked.connect(self.fn_botones_acciones)
    self.ui.b_eliminar.clicked.connect(self.fn_botones_acciones)

    #Acción de botón b_Cancelar
    self.ui.b_Cancelar.clicked.connect(self.fn_Cancelar)

    #Accíon del botón b_Registrar
    self.ui.b_Registrar.clicked.connect(self.fn_Registrar)

  #Función para acción de optionbutton Empleado / Administrador
  def fn_botones_nivel(self):
    if self.ui.b_emp.isChecked():
      self.ui.b_emp.setChecked(True)
      self.ui.b_adm.setChecked(False)
    else:
      self.ui.b_emp.setChecked(False)
      self.ui.b_adm.setChecked(True)

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

      #Buscar Usuario en la Base de Datos
      miCursor.execute("SELECT count(*) FROM USUARIOS WHERE Usuario = ?", [User])
      #Saber si se encontro alguna coincidencia de la lista
      resultado = miCursor.fetchall()
      resultado = resultado[0]        #Extrae el Index 0 de la Tupla para hacer comparación
      
      #Acciones si existe o no alguna coincidencia de Usuario
      if 1 in resultado:
        #Usuario existente
        self.msg_info("Usuario Existente...", f"El usuario {User} ya existe "
                    + '\n' + "Favor de intentar nuevamente")
      else:
        #Usuario nuevo: Ingresar nuevo usuario y contraseña a la Base de Datos
        miCursor.execute("INSERT INTO USUARIOS VALUES (?, ?, ?)", [User, Password, Nivel])
        miConexion.commit()
        self.msg_info("Registro Exitoso...", f"El usuario {User} ha sido añadido a la Base de Datos")
      
      #Cerrar conexion de Base de Datos
      miConexion.close
    #Contraseña incorrecta
    else:
      self.msg_info("Contraseña inválida", "La contraseña y su confirmación no "
                    + "coinciden" + '\n' + "Favor de volver a intentar")

  #Función que deshabilita botón Registrar si estan vacias las celdas
  def fn_Comprobacion(self):
    #Selección de Caso
    if self.ui.b_nuevo.isChecked():
      Caso = "Nuevo"
    if self.ui.b_actualizar.isChecked():
      Caso = "Actualizar"
    if self.ui.b_eliminar.isChecked():
      Caso = "Eliminar"
    #Acciones por Caso
    if Caso == "Nuevo":
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
    elif Caso == "Actualizar":
      if (not self.ui.D_usuario.text()
        and not self.ui.D_psw_old.text()
        and not self.ui.D_psw.text()
        and not self.ui.D_psw_2.text()):
        self.ui.b_Registrar.setEnabled(False)
      elif (not self.ui.D_usuario.text()
        or not self.ui.D_psw_old.text()
        or not self.ui.D_psw.text()
        or not self.ui.D_psw_2.text()):
        self.ui.b_Registrar.setEnabled(False)
      else:
        self.ui.b_Registrar.setEnabled(True)
    elif Caso == "Eliminar":
      if (not self.ui.D_usuario.text()):
        self.ui.b_Registrar.setEnabled(False)
      elif (not self.ui.D_usuario.text()):
        self.ui.b_Registrar.setEnabled(False)
      else:
        self.ui.b_Registrar.setEnabled(True)
      
  #Función para mostrar / ocultar botones al dependiendo de la acción a realizar
  def fn_botones(self):
    if self.ui.b_nuevo.isChecked():
      self.ui.L7.setEnabled(False)
      self.ui.L7.setVisible(False)
  
  #Función para acción de optionbutton Nuevo / Actualizar / Eliminar
  def fn_botones_acciones(self):
    if self.ui.b_nuevo.isChecked():
      #Para seleccionar solo una opción
      self.ui.b_actualizar.setChecked(False)
      self.ui.b_eliminar.setChecked(False)

      #Ocultar botón de contraseña antigua
      self.ui.L7.setEnabled(False)
      self.ui.L7.setVisible(False)
      self.ui.D_psw_old.setEnabled(False)
      self.ui.D_psw_old.setVisible(False)

      #Ocultar botón de Contraseña
      self.ui.L4.setEnabled(True)
      self.ui.L4.setVisible(True)
      self.ui.D_psw.setEnabled(True)
      self.ui.D_psw.setVisible(True)
      #Mover botones
      self.ui.L4.setGeometry(10,140,80,20)
      self.ui.D_psw.setGeometry(100,140,150,20)

      #Mostrar botón de Confirmar
      self.ui.L5.setEnabled(True)
      self.ui.L5.setVisible(True)
      self.ui.D_psw_2.setEnabled(True)
      self.ui.D_psw_2.setVisible(True)
      #Mover botones
      self.ui.L5.setGeometry(10,170,80,20)
      self.ui.D_psw_2.setGeometry(100,170,150,20)

      #Mostrar Frame de botones Empleado / Administrador
      self.ui.fr_Nivel.setVisible(True)

      #Cambiar texto del botón Registrar
      self.ui.b_Registrar.setText("Registrar")

      #Función de comprobación
      self.fn_Comprobacion()

    elif self.ui.b_actualizar.isChecked():
      #Para seleccionar solo una opción
      self.ui.b_nuevo.setChecked(False)
      self.ui.b_eliminar.setChecked(False)

      #Mostrar botón de contraseña antigua
      self.ui.L7.setEnabled(True)
      self.ui.L7.setVisible(True)
      self.ui.D_psw_old.setEnabled(True)
      self.ui.D_psw_old.setVisible(True)

      #Ocultar botón de Contraseña
      self.ui.L4.setEnabled(True)
      self.ui.L4.setVisible(True)
      self.ui.D_psw.setEnabled(True)
      self.ui.D_psw.setVisible(True)
      #Mover botones
      #Mover botones
      self.ui.L4.setGeometry(10,170,80,20)
      self.ui.D_psw.setGeometry(100,170,150,20)

      #Mostrar botón de Confirmar
      self.ui.L5.setEnabled(True)
      self.ui.L5.setVisible(True)
      self.ui.D_psw_2.setEnabled(True)
      self.ui.D_psw_2.setVisible(True)
      #Mover botones
      self.ui.L5.setGeometry(10,200,80,20)
      self.ui.D_psw_2.setGeometry(100,200,150,20)

      #Mostrar Frame de botones Empleado / Administrador
      self.ui.fr_Nivel.setVisible(True)

      #Cambiar texto del botón Registrar
      self.ui.b_Registrar.setText("Actualizar")

      #Función de comprobación
      self.fn_Comprobacion()

    elif self.ui.b_eliminar.isChecked():
      #Para seleccionar solo una opción
      self.ui.b_nuevo.setChecked(False)
      self.ui.b_actualizar.setChecked(False)

      #Ocultar botón de Contraseña antigua
      self.ui.L7.setEnabled(False)
      self.ui.L7.setVisible(False)
      self.ui.D_psw_old.setEnabled(False)
      self.ui.D_psw_old.setVisible(False)

      #Ocultar botón de Contraseña
      self.ui.L4.setEnabled(False)
      self.ui.L4.setVisible(False)
      self.ui.D_psw.setEnabled(False)
      self.ui.D_psw.setVisible(False)
      #Mover botones
      self.ui.L4.setGeometry(10,140,80,20)
      self.ui.D_psw.setGeometry(100,140,150,20)

      #Ocultar botón de Confirmar
      self.ui.L5.setEnabled(False)
      self.ui.L5.setVisible(False)
      self.ui.D_psw_2.setEnabled(False)
      self.ui.D_psw_2.setVisible(False)
      #Mover botones
      self.ui.L5.setGeometry(10,170,80,20)
      self.ui.D_psw_2.setGeometry(100,170,150,20)

      #Ocultar Frame de botones Empleado / Administrador
      self.ui.fr_Nivel.setVisible(False)

      #Cambiar texto del botón Registrar
      self.ui.b_Registrar.setText("Eliminar")

      #Función de comprobación
      self.fn_Comprobacion()


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
