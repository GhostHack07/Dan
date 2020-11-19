#Importar modulos de ventanas individuales

#from m_Registro import Registro_GUI
from m_Login import Login_GUI

#Importar librerias necesarias
import sys
#import sqlite3

##Importar ventana de Login creada en QT Designes  y exportada a python
from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QMessageBox
#from f_Registro import Ui_MainWindow

#def fn_Abrir_Ventana_Registro(self):


#if __name__ == '__main__':
#  app = QtWidgets.QApplication([])
#  application = Registro_GUI()
#  application.show()
#  sys.exit(app.exec())

if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  application = Login_GUI()
  application.show()
  sys.exit(app.exec())