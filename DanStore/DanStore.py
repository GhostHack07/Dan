#Importar modulos de ventanas individuales

#from m_Registro import Registro_GUI
from Ventanas.m_Login import Login_GUI

#Importar librerias necesarias
import sys

#Importar ventanas de los formularios
import Ventanas.m_Login as m_Login

##Importar ventana de Login creada en QT Designes  y exportada a python
from PyQt5 import QtWidgets

if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  application = Login_GUI()
  application.show()
  sys.exit(app.exec())