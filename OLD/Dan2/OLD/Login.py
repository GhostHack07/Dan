#Iniciar ventana de Login exportada de .ui a .py
import sys
from PyQt5 import QtWidgets
from f_Login import QMainWindow

class Login_GUI(QtWidgets.QMainWindow):
  def __init__(self):
    super(Login_GUI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
app = QtWidgets.QApplication([])
application = Login_GUI()
application.show()
sys.exit(app.exec())



  
