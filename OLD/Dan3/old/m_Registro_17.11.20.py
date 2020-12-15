#Importar librerias necesarias
import sys
import sqlite3

#Importar ventana de Login creada en QT Designes  y exportada a python
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QDesktopWidget

from PyQt5.QtWidgets import QMessageBox
from f_Registro import Ui_MainWindow

window = None

class Registro_GUI(QtWidgets.QMainWindow):
  #Función para iniciar ventana de Login
  def __init__(self):
    super(Registro_GUI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    
    #Habilitar o deshabilitar botones al iniciar
    self.ui.b_Registrar.setEnabled(False)
    self.ui.b_Cancelar.setEnabled(True)
    self.ui.b_emp.setChecked(True)
    self.ui.b_adm.setChecked(False)
    self.ui.b_nuevo.setChecked(True)
    self.ui.b_actualizar.setChecked(False)
    self.ui.b_eliminar.setChecked(False)
    self.ui.fr_Actualizacion.setVisible(False)
    self.ui.fr_Nivel.setVisible(True)
    #self.ui.D
    #self.ui.D_usuario.setFocus()
    
    #Función para activar botones al inicio
    self.fn_botones_acciones()
    self.fn_Comprobacion()
    #self.fn_checkbox_nivel()

    #Comprobar que las celdas tengan datos
    self.ui.D_usuario.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_usuario_2.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_psw_old.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_psw.textChanged.connect(self.fn_Comprobacion)
    self.ui.D_psw_2.textChanged.connect(self.fn_Comprobacion)

    self.ui.ch_Usuario.stateChanged.connect(self.fn_Comprobacion)
    self.ui.ch_psw.stateChanged.connect(self.fn_Comprobacion)
    self.ui.ch_Nivel.stateChanged.connect(self.fn_Comprobacion)

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

  # ----------------- Funciones para uso de botones ----------------- #
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
      
    #Casos de activación de botón
    # ------------------- Caso NUEVO usuario ------------------- #
    if self.fn_Casos() == "Nuevo":
      #Comprobar que la contraseña y confirmación sean iguales
      if Password == Confirmacion:
 
        #Acciones si existe o no alguna coincidencia de Usuario
        if self.fn_Usuario_Existente(User) == "Si":
          #Usuario existente
          self.msg_info("Usuario Existente...", f"El usuario {User} ya existe "
                      + '\n' + "Favor de intentar nuevamente")
        if self.fn_Usuario_Existente(User) == "No":
          #Usuario no existente --> Registrar en la Base de Datos
          self.fn_Registro(User, Password, Nivel)

      #Contraseña incorrecta
      else:
        self.msg_info("Contraseña inválida", "La contraseña y su confirmación no "
                      + "coinciden" + '\n' + "Favor de volver a intentar")
    
    # ---------------- Caso ACTUALIZAR usuario ---------------- #
    if self.fn_Casos() == "Actualizar":
      #Leer contraseña anterior
      old_psw = self.ui.D_psw_old.text()
      new_User = self.ui.D_usuario_2.text()

      #Verificar si el usuario existe en la Base de Datos
      if self.fn_Usuario_Existente(User) == "No":
        self.msg_info("Usuario Inexistente...", f"El usuario {User} no existe "
                      + '\n' + "Favor de intentar nuevamente")
      
      #Acciones si existe o no alguna coincidencia de Usuario
      if self.fn_Usuario_Existente(User) == "Si":
        self.fn_Actualizar(User, new_User, old_psw, Password, Confirmacion, Nivel)

    # ----------------- Caso ELIMINAR usuario ----------------- #
    if self.fn_Casos() == "Eliminar":
      #No existe el usuario
      if self.fn_Usuario_Existente(User) == "No":
        self.msg_info("Usuario Inexistente...", f"El usuario {User} no existe "
                      + '\n' + "Favor de intentar nuevamente")
      
      if self.fn_Usuario_Existente(User) == "Si":
        #Mensaje de confirmación
        if self.msg_confirmacion("Confirmación", "¿Estas seguro que quieres "
                                 + f"eliminar al usuario {User}?") == "Eliminar":
          self.fn_Eliminar(User)

  #Función para conocer si es un Caso Nuevo, Actualizar o Eliminar
  def fn_Casos(self):
    if self.ui.b_nuevo.isChecked():
      Caso = "Nuevo"
    if self.ui.b_actualizar.isChecked():
      Caso = "Actualizar"
    if self.ui.b_eliminar.isChecked():
      Caso = "Eliminar"
    return Caso

  #Función que deshabilita botón Registrar si estan vacias las celdas
  def fn_Comprobacion(self):
    #Acciones por Caso
    if self.fn_Casos() == "Nuevo":
      #Desmarcar checkboxes
      self.ui.ch_Usuario.setChecked(False)
      self.ui.ch_psw.setChecked(False)
      self.ui.ch_Nivel.setChecked(False)

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
    elif self.fn_Casos() == "Actualizar":
      if self.fn_checkbox_casos() == 0:
        self.ui.b_Registrar.setEnabled(False)
      
      if self.fn_checkbox_casos() == 1:
        if not self.ui.D_usuario.text():
          self.ui.b_Registrar.setEnabled(False)
        else:
          self.ui.b_Registrar.setEnabled(True)

      if self.fn_checkbox_casos() == 3 or self.fn_checkbox_casos() == 5:
        if (not self.ui.D_usuario.text()
            and not self.ui.D_usuario_2.text()):
          self.ui.b_Registrar.setEnabled(False)
        elif (not self.ui.D_usuario.text()
            or not self.ui.D_usuario_2.text()):
          self.ui.b_Registrar.setEnabled(False)
        else:
          self.ui.b_Registrar.setEnabled(True)

      if self.fn_checkbox_casos() == 2 or self.fn_checkbox_casos() == 4:
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

      if self.fn_checkbox_casos() == 6 or self.fn_checkbox_casos() == 7:
        if (not self.ui.D_usuario.text()
            and not self.ui.D_usuario_2.text()
            and not self.ui.D_psw_old.text()
            and not self.ui.D_psw.text()
            and not self.ui.D_psw_2.text()):
          self.ui.b_Registrar.setEnabled(False)
        elif (not self.ui.D_usuario.text()
            or not self.ui.D_usuario_2.text()
            or not self.ui.D_psw_old.text()
            or not self.ui.D_psw.text()
            or not self.ui.D_psw_2.text()):
          self.ui.b_Registrar.setEnabled(False)
        else:
          self.ui.b_Registrar.setEnabled(True)

      if self.fn_checkbox_casos() == 4:
        if not self.ui.D_usuario.text():
          self.ui.b_Registrar.setEnabled(False)
        else:
          self.ui.b_Registrar.setEnabled(True)

    elif self.fn_Casos() == "Eliminar":
      #Desmarcar checkboxes
      self.ui.ch_Usuario.setChecked(False)
      self.ui.ch_psw.setChecked(False)
      self.ui.ch_Nivel.setChecked(False)

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
  #Mostrar u Ocultar botones segun selección
  def fn_botones_acciones(self):
    if self.ui.b_nuevo.isChecked():
      #Para seleccionar solo una opción
      self.ui.b_actualizar.setChecked(False)
      self.ui.b_eliminar.setChecked(False)

      #Ocultar frame de botones actualización
      self.ui.fr_Actualizacion.setVisible(False)

      #Mostrar botón usuario
      self.ui.L3.setEnabled(True)
      self.ui.L3.setVisible(True)
      self.ui.D_usuario.setEnabled(True)
      self.ui.D_usuario.setVisible(True)
      #Mover botones
      self.ui.L3.setGeometry(10,110,86,20)
      self.ui.D_usuario.setGeometry(100,110,150,20)
      self.ui.D_usuario.setFocus()

      #Ocultar botón de usuario nuevo
      self.ui.L8.setEnabled(False)
      self.ui.L8.setVisible(False)
      self.ui.D_usuario_2.setEnabled(False)
      self.ui.D_usuario_2.setVisible(False)

      #Ocultar botón de contraseña antigua
      self.ui.L7.setEnabled(False)
      self.ui.L7.setVisible(False)
      self.ui.D_psw_old.setEnabled(False)
      self.ui.D_psw_old.setVisible(False)

      #Mostrar botón de contraseña
      self.ui.L4.setEnabled(True)
      self.ui.L4.setVisible(True)
      self.ui.D_psw.setEnabled(True)
      self.ui.D_psw.setVisible(True)
      #Mover botones
      self.ui.L4.setGeometry(10,140,86,20)
      self.ui.D_psw.setGeometry(100,140,150,20)

      #Mostrar botón de Confirmar
      self.ui.L5.setEnabled(True)
      self.ui.L5.setVisible(True)
      self.ui.D_psw_2.setEnabled(True)
      self.ui.D_psw_2.setVisible(True)
      #Mover botones
      self.ui.L5.setGeometry(10,170,86,20)
      self.ui.D_psw_2.setGeometry(100,170,150,20)

      #Mostrar Frame de botones Empleado / Administrador
      self.ui.fr_Nivel.setVisible(True)
      #Mover frame
      self.ui.fr_Nivel.setGeometry(9,210,241,40)

      #Cambiar texto del botón Registrar
      self.ui.b_Registrar.setText("Registrar")

      #Función de comprobación
      self.fn_Comprobacion()

    elif self.ui.b_actualizar.isChecked():
      #Para seleccionar solo una opción
      self.ui.b_nuevo.setChecked(False)
      self.ui.b_eliminar.setChecked(False)

      #Mostrar frame de botones actualización
      self.ui.fr_Actualizacion.setVisible(True)

      #Ocultar todos los textos
      self.ui.L3.setEnabled(False)
      self.ui.L3.setVisible(False)
      self.ui.D_usuario.setEnabled(False)
      self.ui.D_usuario.setVisible(False)

      self.ui.L8.setEnabled(False)
      self.ui.L8.setVisible(False)
      self.ui.D_usuario_2.setEnabled(False)
      self.ui.D_usuario_2.setVisible(False)
      
      self.ui.L7.setEnabled(False)
      self.ui.L7.setVisible(False)
      self.ui.D_psw_old.setEnabled(False)
      self.ui.D_psw_old.setVisible(False)

      self.ui.L4.setEnabled(False)
      self.ui.L4.setVisible(False)
      self.ui.D_psw.setEnabled(False)
      self.ui.D_psw.setVisible(False)

      self.ui.L5.setEnabled(False)
      self.ui.L5.setVisible(False)
      self.ui.D_psw_2.setEnabled(False)
      self.ui.D_psw_2.setVisible(False)

      #Ocultar frame de Nivel
      self.ui.fr_Nivel.setVisible(False)

      #Acciones al utilizar los checkboxes Usuario / Contraseña / Nivel
      self.ui.ch_Usuario.stateChanged.connect(self.fn_checkbox)
      self.ui.ch_psw.stateChanged.connect(self.fn_checkbox)
      self.ui.ch_Nivel.stateChanged.connect(self.fn_checkbox_Nivel)

      #Cambiar texto del botón Registrar
      self.ui.b_Registrar.setText("Actualizar")

      #Función de comprobación
      self.fn_Comprobacion()

    elif self.ui.b_eliminar.isChecked():
      #Para seleccionar solo una opción
      self.ui.b_nuevo.setChecked(False)
      self.ui.b_actualizar.setChecked(False)

      #Ocultar frame de botones actualización
      self.ui.fr_Actualizacion.setVisible(False)

      #Mostrar botón usuario
      self.ui.L3.setEnabled(True)
      self.ui.L3.setVisible(True)
      self.ui.D_usuario.setEnabled(True)
      self.ui.D_usuario.setVisible(True)
      #Mover botones
      self.ui.L3.setGeometry(10,110,86,20)
      self.ui.D_usuario.setGeometry(100,110,150,20)
      self.ui.D_usuario.setFocus()

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

      #Ocultar botón de Confirmar
      self.ui.L5.setEnabled(False)
      self.ui.L5.setVisible(False)
      self.ui.D_psw_2.setEnabled(False)
      self.ui.D_psw_2.setVisible(False)

      #Ocultar Frame de botones Empleado / Administrador
      self.ui.fr_Nivel.setVisible(False)

      #Cambiar texto del botón Registrar
      self.ui.b_Registrar.setText("Eliminar")

      #Función de comprobación
      self.fn_Comprobacion()

  #Función para acción de optionbutton Empleado / Administrador
  def fn_botones_nivel(self):
    if self.ui.b_emp.isChecked():
      self.ui.b_emp.setChecked(True)
      self.ui.b_adm.setChecked(False)
    else:
      self.ui.b_emp.setChecked(False)
      self.ui.b_adm.setChecked(True)

  #Funcion casos de Checkboxes
  def fn_checkbox_casos(self):
    if (not self.ui.ch_Nivel.isChecked()
        and not self.ui.ch_Usuario.isChecked()
        and not self.ui.ch_psw.isChecked()):
      caso = 0

    elif (self.ui.ch_Nivel.isChecked()
        and not self.ui.ch_Usuario.isChecked()
        and not self.ui.ch_psw.isChecked()):
      caso = 1

    elif (self.ui.ch_Nivel.isChecked()
        and self.ui.ch_psw.isChecked()
        and not self.ui.ch_Usuario.isChecked()):
      caso = 2

    elif (self.ui.ch_Nivel.isChecked()
        and not self.ui.ch_psw.isChecked()
        and self.ui.ch_Usuario.isChecked()):
      caso = 3

    elif (not self.ui.ch_Nivel.isChecked()
        and self.ui.ch_psw.isChecked()
        and not self.ui.ch_Usuario.isChecked()):
      caso = 4

    elif (not self.ui.ch_Nivel.isChecked()
        and not self.ui.ch_psw.isChecked()
        and self.ui.ch_Usuario.isChecked()):
      caso = 5

    elif (self.ui.ch_Nivel.isChecked()
        and self.ui.ch_psw.isChecked()
        and self.ui.ch_Usuario.isChecked()):
      caso = 6

    elif (not self.ui.ch_Nivel.isChecked()
        and self.ui.ch_psw.isChecked()
        and self.ui.ch_Usuario.isChecked()):
      caso = 7

    return caso

  #Función para acción de checkbox Usuario / Contraseña / Nivel
  def fn_checkbox(self):
    if self.fn_checkbox_casos() == 0:
      if self.ui.b_actualizar.isChecked():
        #Ocultar todos los textos
        self.ui.L3.setEnabled(False)
        self.ui.L3.setVisible(False)
        self.ui.D_usuario.setEnabled(False)
        self.ui.D_usuario.setVisible(False)

        self.ui.L8.setEnabled(False)
        self.ui.L8.setVisible(False)
        self.ui.D_usuario_2.setEnabled(False)
        self.ui.D_usuario_2.setVisible(False)
      
        self.ui.L7.setEnabled(False)
        self.ui.L7.setVisible(False)
        self.ui.D_psw_old.setEnabled(False)
        self.ui.D_psw_old.setVisible(False)

        self.ui.L4.setEnabled(False)
        self.ui.L4.setVisible(False)
        self.ui.D_psw.setEnabled(False)
        self.ui.D_psw.setVisible(False)

        self.ui.L5.setEnabled(False)
        self.ui.L5.setVisible(False)
        self.ui.D_psw_2.setEnabled(False)
        self.ui.D_psw_2.setVisible(False)

        #Ocultar frame de Nivel
        self.ui.fr_Nivel.setVisible(False)
      elif self.ui.b_eliminar.isChecked():
        #Mostrar botón usuario
        self.ui.L3.setEnabled(True)
        self.ui.L3.setVisible(True)
        self.ui.D_usuario.setEnabled(True)
        self.ui.D_usuario.setVisible(True)
        #Mover botones
        self.ui.L3.setGeometry(10,110,86,20)
        self.ui.D_usuario.setGeometry(100,110,150,20)
        self.ui.D_usuario.setFocus()

        #Ocultar botón usuario nuevo
        self.ui.L8.setEnabled(False)
        self.ui.L8.setVisible(False)
        self.ui.D_usuario_2.setEnabled(False)
        self.ui.D_usuario_2.setVisible(False)
      
        #Ocultar botón contraseña anterior
        self.ui.L7.setEnabled(False)
        self.ui.L7.setVisible(False)
        self.ui.D_psw_old.setEnabled(False)
        self.ui.D_psw_old.setVisible(False)

        #Ocultar botón contraseña
        self.ui.L4.setEnabled(False)
        self.ui.L4.setVisible(False)
        self.ui.D_psw.setEnabled(False)
        self.ui.D_psw.setVisible(False)

        #Ocultar botón confimración de contraseña
        self.ui.L5.setEnabled(False)
        self.ui.L5.setVisible(False)
        self.ui.D_psw_2.setEnabled(False)
        self.ui.D_psw_2.setVisible(False)

        #Ocultar frame de Nivel
        self.ui.fr_Nivel.setVisible(False)

    if self.fn_checkbox_casos() == 1:
      #Mostrar botón usuario
      self.ui.L3.setEnabled(True)
      self.ui.L3.setVisible(True)
      self.ui.D_usuario.setEnabled(True)
      self.ui.D_usuario.setVisible(True)
      #Mover botones
      self.ui.L3.setGeometry(10,110+40,86,20)
      self.ui.D_usuario.setGeometry(100,110+40,150,20)
      self.ui.D_usuario.setFocus()
          
      #Ocultar botón usuario nuevo
      self.ui.L8.setEnabled(False)
      self.ui.L8.setVisible(False)
      self.ui.D_usuario_2.setEnabled(False)
      self.ui.D_usuario_2.setVisible(False)

      #Ocultar botón contraseña anterior
      self.ui.L7.setEnabled(False)
      self.ui.L7.setVisible(False)
      self.ui.D_psw_old.setEnabled(False)
      self.ui.D_psw_old.setVisible(False)

      #Ocultar botón contraseña
      self.ui.L4.setEnabled(False)
      self.ui.L4.setVisible(False)
      self.ui.D_psw.setEnabled(False)
      self.ui.D_psw.setVisible(False)

      #Ocultar botón confimración de contraseña
      self.ui.L5.setEnabled(False)
      self.ui.L5.setVisible(False)
      self.ui.D_psw_2.setEnabled(False)
      self.ui.D_psw_2.setVisible(False)



    if self.fn_checkbox_casos() == 5 or self.fn_checkbox_casos() == 3:
      #Mostrar botón usuario
      self.ui.L3.setEnabled(True)
      self.ui.L3.setVisible(True)
      self.ui.D_usuario.setEnabled(True)
      self.ui.D_usuario.setVisible(True)
      #Mover botones
      self.ui.L3.setGeometry(10,110+40,86,20)
      self.ui.D_usuario.setGeometry(100,110+40,150,20)
      self.ui.D_usuario.setFocus()
          
      #Mostrar botón usuario nuevo
      self.ui.L8.setEnabled(True)
      self.ui.L8.setVisible(True)
      self.ui.D_usuario_2.setEnabled(True)
      self.ui.D_usuario_2.setVisible(True)
      #Mover botones
      self.ui.L8.setGeometry(10,180,86,20)
      self.ui.D_usuario_2.setGeometry(100,180,150,20)

      #Ocultar botón contraseña anterior
      self.ui.L7.setEnabled(False)
      self.ui.L7.setVisible(False)
      self.ui.D_psw_old.setEnabled(False)
      self.ui.D_psw_old.setVisible(False)

      #Ocultar botón contraseña
      self.ui.L4.setEnabled(False)
      self.ui.L4.setVisible(False)
      self.ui.D_psw.setEnabled(False)
      self.ui.D_psw.setVisible(False)

      #Ocultar botón confimración de contraseña
      self.ui.L5.setEnabled(False)
      self.ui.L5.setVisible(False)
      self.ui.D_psw_2.setEnabled(False)
      self.ui.D_psw_2.setVisible(False)
    
    if self.fn_checkbox_casos() == 4 or self.fn_checkbox_casos() == 2:
      #Mostrar botón usuario
      self.ui.L3.setEnabled(True)
      self.ui.L3.setVisible(True)
      self.ui.D_usuario.setEnabled(True)
      self.ui.D_usuario.setVisible(True)
      #Mover botones
      self.ui.L3.setGeometry(10,110+40,86,20)
      self.ui.D_usuario.setGeometry(100,110+40,150,20)
      self.ui.D_usuario.setFocus()
          
      #Ocultar botón usuario nuevo
      self.ui.L8.setEnabled(False)
      self.ui.L8.setVisible(False)
      self.ui.D_usuario_2.setEnabled(False)
      self.ui.D_usuario_2.setVisible(False)
      #Mover botones
      self.ui.L8.setGeometry(10,180,86,20)
      self.ui.D_usuario_2.setGeometry(100,180,150,20)

      #Mostrar botón contraseña anterior
      self.ui.L7.setEnabled(True)
      self.ui.L7.setVisible(True)
      self.ui.D_psw_old.setEnabled(True)
      self.ui.D_psw_old.setVisible(True)
      #Mover botones
      self.ui.L7.setGeometry(10,140+40,86,20)
      self.ui.D_psw_old.setGeometry(100,140+40,150,20)

      #Mostrar botón contraseña
      self.ui.L4.setEnabled(True)
      self.ui.L4.setVisible(True)
      self.ui.D_psw.setEnabled(True)
      self.ui.D_psw.setVisible(True)
      #Mover botones
      self.ui.L4.setGeometry(10,170+40,86,20)
      self.ui.D_psw.setGeometry(100,170+40,150,20)

      #Mostrar botón confimración de contraseña
      self.ui.L5.setEnabled(True)
      self.ui.L5.setVisible(True)
      self.ui.D_psw_2.setEnabled(True)
      self.ui.D_psw_2.setVisible(True)
      #Mover botones
      self.ui.L5.setGeometry(10,200+40,86,20)
      self.ui.D_psw_2.setGeometry(100,200+40,150,20)

    if self.fn_checkbox_casos() == 7 or self.fn_checkbox_casos() == 6:
      #Mostrar botón usuario
      self.ui.L3.setEnabled(True)
      self.ui.L3.setVisible(True)
      self.ui.D_usuario.setEnabled(True)
      self.ui.D_usuario.setVisible(True)
      #Mover botones
      self.ui.L3.setGeometry(10,110+40,86,20)
      self.ui.D_usuario.setGeometry(100,110+40,150,20)
      self.ui.D_usuario.setFocus()
          
      #Mostrar botón usuario nuevo
      self.ui.L8.setEnabled(True)
      self.ui.L8.setVisible(True)
      self.ui.D_usuario_2.setEnabled(True)
      self.ui.D_usuario_2.setVisible(True)
      #Mover botones
      self.ui.L8.setGeometry(10,140+40,86,20)
      self.ui.D_usuario_2.setGeometry(100,140+40,150,20)

      #Mostrar botón contraseña anterior
      self.ui.L7.setEnabled(True)
      self.ui.L7.setVisible(True)
      self.ui.D_psw_old.setEnabled(True)
      self.ui.D_psw_old.setVisible(True)
      #Mover botones
      self.ui.L7.setGeometry(10,140+70,86,20)
      self.ui.D_psw_old.setGeometry(100,140+70,150,20)

      #Mostrar botón contraseña
      self.ui.L4.setEnabled(True)
      self.ui.L4.setVisible(True)
      self.ui.D_psw.setEnabled(True)
      self.ui.D_psw.setVisible(True)
      #Mover botones
      self.ui.L4.setGeometry(10,170+70,86,20)
      self.ui.D_psw.setGeometry(100,170+70,150,20)

      #Mostrar botón confimración de contraseña
      self.ui.L5.setEnabled(True)
      self.ui.L5.setVisible(True)
      self.ui.D_psw_2.setEnabled(True)
      self.ui.D_psw_2.setVisible(True)
      #Mover botones
      self.ui.L5.setGeometry(10,200+70,86,20)
      self.ui.D_psw_2.setGeometry(100,200+70,150,20)
  
  #Función para acción de checkbox Nivel
  def fn_checkbox_Nivel(self):
    if self.fn_checkbox_casos() == 0:
      #Ocultar botón usuario
      self.ui.L3.setEnabled(False)
      self.ui.L3.setVisible(False)
      self.ui.D_usuario.setEnabled(False)
      self.ui.D_usuario.setVisible(False)

      #Ocultar frame de Nivel
      self.ui.fr_Nivel.setVisible(False)

    if self.fn_checkbox_casos() == 1:
      #Mostrar botón usuario
      self.ui.L3.setEnabled(True)
      self.ui.L3.setVisible(True)
      self.ui.D_usuario.setEnabled(True)
      self.ui.D_usuario.setVisible(True)
      #Mover botones
      self.ui.L3.setGeometry(10,110+40,86,20)
      self.ui.D_usuario.setGeometry(100,110+40,150,20)
      self.ui.D_usuario.setFocus()

      #Mostrar frame de Nivel
      self.ui.fr_Nivel.setVisible(True)
      self.ui.fr_Nivel.setGeometry(9,300,241,40)

    if self.fn_checkbox_casos() == 2:
      #Mostrar frame de Nivel
      self.ui.fr_Nivel.setVisible(True)
      self.ui.fr_Nivel.setGeometry(9,300,241,40)
      self.ui.D_usuario.setFocus()

    if self.fn_checkbox_casos() == 3:
      #Mostrar frame de Nivel
      self.ui.fr_Nivel.setVisible(True)
      self.ui.fr_Nivel.setGeometry(9,300,241,40)
      self.ui.D_usuario.setFocus()

    if (self.fn_checkbox_casos() == 4 
        or self.fn_checkbox_casos() == 5
        or self.fn_checkbox_casos() == 7):
      #Ocultar frame de Nivel
      self.ui.fr_Nivel.setVisible(False)
      self.ui.D_usuario.setFocus()


    if self.fn_checkbox_casos() == 6:
      #Mostrar frame de Nivel
      self.ui.fr_Nivel.setVisible(True)
      self.ui.fr_Nivel.setGeometry(9,300,241,40)
      self.ui.D_usuario.setFocus()

  #Función del boton b_Cancelar
  def fn_Cancelar(self):
    sys.exit()
  
  # --------- Funciones para Administrar acciones en SQLite --------- #
  #Función para comprobar si existe o no el usiario    
  def fn_Usuario_Existente(self, User):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    #Buscar Usuario en la Base de Datos
    miCursor.execute("SELECT count(*) FROM USUARIOS WHERE Usuario = ?", [User])
    #Saber si se encontro alguna coincidencia de la lista
    resultado = miCursor.fetchall()
    resultado = resultado[0]        #Extrae el Index 0 de la Tupla para hacer comparación
    #Cerrar conexxion se SQLite
    miConexion.close

    if 1 in resultado:
      return "Si"         #El usuario ya existe
    if 0 in resultado:
      return "No"         #El usuario NO existe

  #Función para registrar nuevo usuario
  def fn_Registro(self, User, Password, Nivel):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    #Usuario nuevo: Ingresar nuevo usuario y contraseña a la Base de Datos
    miCursor.execute("INSERT INTO USUARIOS VALUES (?, ?, ?)", [User, Password, Nivel])
    miConexion.commit()
    self.msg_info("Registro Exitoso...", f"El usuario {User} ha sido añadido a la Base de Datos")
    miConexion.close
    
    sys.exit()

  #Función para actualizar usuario
  def fn_Actualizar(self, User, new_User, old_psw, Password, Confirmacion, Nivel):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    if self.fn_checkbox_casos() == 1:
      miCursor.execute("UPDATE USUARIOS SET Nivel = ? WHERE Usuario = ?", (Nivel, User))
      miConexion.commit()
      miConexion.close()
      self.msg_info("Actualización de Datos", "El Nivel ha sido actualizado")
      sys.exit()

    if self.fn_checkbox_casos() == 2:
      #Verificar constraseña anterior en la Base de Datos
      miCursor.execute("SELECT * FROM USUARIOS WHERE Usuario = ? AND PSW = ?",
                      (User, old_psw))
      if miCursor.fetchall():
        #Verificar constraseñas iguales
        if Password == Confirmacion:
          miCursor.execute("UPDATE USUARIOS SET PSW = ?, Nivel = ? WHERE Usuario = ?",
                          (Password, Nivel, User))
          miConexion.commit()
          miConexion.close()
          self.msg_info("Actualización de Datos", "Los datos de Contraseña y Nivel " 
                      + "han sido actualizados")
          sys.exit()

        else:
          self.msg_info("Contraseña inválida", "La contraseña y su confirmación no "
                      + "coinciden" + '\n' + "Favor de volver a intentar")
      else:
        self.msg_info("Contraseña inválida", "La contraseña anterior no coincide "
                      + "con el valor registrado" + '\n' + "Favor de volver a intentar")

    if self.fn_checkbox_casos() == 3:
      #Verificar constraseña anterior en la Base de Datos
      miCursor.execute("SELECT * FROM USUARIOS WHERE Usuario = ?", (User))
      if miCursor.fetchall():
        #Verificar constraseñas iguales
        if User != new_User:
          miCursor.execute("UPDATE USUARIOS SET Usuario = ?, Nivel = ? WHERE Usuario = ?",
                          (new_User, Nivel, User))
          miConexion.commit()
          miConexion.close()
          self.msg_info("Actualización de Datos", "Los datos de Usuario y Nivel "
                        + "han sido actualizados")
          sys.exit()
        else:
          self.msg_info("Usuario inválido", f"El usuario {new_User} es igual usuario "
                        + "anterior" + '\n' + "Favor de volver a intentar")
      else:
        self.msg_info("Usuario inválido", f"El Usuario {User} no se encuentra en la "
                      + "Base de Datos" + '\n' + "Favor de volver a intentar")

    if self.fn_checkbox_casos() == 4:
      #Verificar constraseña anterior en la Base de Datos
      miCursor.execute("SELECT * FROM USUARIOS WHERE Usuario = ? AND PSW = ?",
                      (User, old_psw))
      if miCursor.fetchall():
        #Verificar constraseñas iguales
        if Password == Confirmacion:
          miCursor.execute("UPDATE USUARIOS SET PSW = ? WHERE Usuario = ?",
                          (Password, User))
          miConexion.commit()
          miConexion.close()
          self.msg_info("Actualización de Datos", "El dato de Contraseña " 
                      + "ha sido actualizado")
          sys.exit()
        else:
          self.msg_info("Contraseña inválida", "La contraseña y su confirmación no "
                      + "coinciden" + '\n' + "Favor de volver a intentar")
      else:
        self.msg_info("Contraseña inválida", "La contraseña anterior no coincide "
                      + "con el valor registrado" + '\n' + "Favor de volver a intentar")

    if self.fn_checkbox_casos() == 5:
      #Verificar constraseña anterior en la Base de Datos
      miCursor.execute("SELECT * FROM USUARIOS WHERE Usuario = ?", (User))
      if miCursor.fetchall():
        #Verificar constraseñas iguales
        if User != new_User:
          miCursor.execute("UPDATE USUARIOS SET Usuario = ? WHERE Usuario = ?",
                          (new_User, User))
          miConexion.commit()
          miConexion.close()
          self.msg_info("Actualización de Datos", "El dato de Usuario "
                        + "ha sido actualizados")
          sys.exit()
        else:
          self.msg_info("Usuario inválido", f"El usuario {new_User} es igual usuario "
                        + "anterior" + '\n' + "Favor de volver a intentar")
      else:
        self.msg_info("Usuario inválido", f"El Usuario {User} no se encuentra en la "
                      + "Base de Datos" + '\n' + "Favor de volver a intentar")

    if self.fn_checkbox_casos() == 6:
      #Verificar constraseña anterior en la Base de Datos
      miCursor.execute("SELECT * FROM USUARIOS WHERE Usuario = ? AND PSW = ?",
                      (User, old_psw))
      if miCursor.fetchall():
        #Verificar constraseñas iguales
        if User != new_User:
          if Password == Confirmacion:
            miCursor.execute('''UPDATE USUARIOS SET Usuario = ?, PSW = ?, Nivel = ?
                            WHERE Usuario = ?''', (new_User, Password, Nivel, User))
            miConexion.commit()
            miConexion.close()
            self.msg_info("Actualización de Datos", "Los datos de Usuario, Contraseña "
                          + "y Nivel han sido actualizados")
            sys.exit()
          else:
            self.msg_info("Contraseña inválida", "La contraseña y su confirmación no "
                      + "coinciden" + '\n' + "Favor de volver a intentar")
        else:
          self.msg_info("Usuario inválido", f"El usuario {new_User} es igual usuario "
                        + "anterior" + '\n' + "Favor de volver a intentar")
      else:
        self.msg_info("Contraseña inválida", "La contraseña anterior no coincide "
                      + "con el valor registrado" + '\n' + "Favor de volver a intentar")

    if self.fn_checkbox_casos() == 7:
      #Verificar constraseña anterior en la Base de Datos
      miCursor.execute("SELECT * FROM USUARIOS WHERE Usuario = ? AND PSW = ?",
                      (User, old_psw))
      if miCursor.fetchall():
        #Verificar constraseñas iguales
        if User != new_User:
          if Password == Confirmacion:
            miCursor.execute("UPDATE USUARIOS SET Usuario = ?, PSW = ? WHERE Usuario = ?",
                            (new_User, Password, User))
            miConexion.commit()
            miConexion.close()
            self.msg_info("Actualización de Datos", "Los datos de Usuario y Contraseña "
                          + "han sido actualizados")
            sys.exit()
          else:
            self.msg_info("Contraseña inválida", "La contraseña y su confirmación no "
                      + "coinciden" + '\n' + "Favor de volver a intentar")
        else:
          self.msg_info("Usuario inválido", f"El usuario {new_User} es igual usuario "
                        + "anterior" + '\n' + "Favor de volver a intentar")
      else:
        self.msg_info("Contraseña inválida", "La contraseña anterior no coincide "
                      + "con el valor registrado" + '\n' + "Favor de volver a intentar")
  
  #Función para eliminar usuario
  def fn_Eliminar(self, User):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    #Eliminar usuario después de la confirmación
    miCursor.execute("DELETE FROM USUARIOS WHERE Usuario = ?", [User])
    miConexion.commit()
    miConexion.close()
    self.msg_info("Usuario Eliminado...", f"El usuario {User} se elimino exitosamente")
    sys.exit()
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

#Función para iniciar ventana de Registro
def start():
    global window  
    window = Registro_GUI()
    window.show()


##Función para iniciar ventana de Registro 
#if __name__ == '__main__':
#  app = QtWidgets.QApplication([])
#  application = Registro_GUI()
#  application.show()
#  sys.exit(app.exec())