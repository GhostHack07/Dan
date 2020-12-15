#Importar librerias necesarias
import sys
import sqlite3

#Importar ventana de Login creada en QT Designes  y exportada a python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QTableWidget
from Pantallas.f_Ventas import Ui_MainWindow
from PyQt5.QtGui import QFont

#Importar módulos para abrir otras ventanas
import Ventanas.m_Login as m_Login
import Ventanas.m_Registro as m_Registro
import Ventanas.m_Inventario as m_Inventario
import Ventanas.m_Productos as m_Productos


#Variable global para cambio de ventana
window = None

class Ventas_GUI(QtWidgets.QMainWindow):
  #Función para iniciar ventana de Login
  def __init__(self):
    super(Ventas_GUI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    #Habilitar o deshabilitar botones al iniciar
    self.ui.b_Buscar.setEnabled(True)
    self.ui.b_Actualizar.setEnabled(True)
    self.ui.b_Eliminar.setEnabled(True)
    self.ui.b_Cancelar.setEnabled(True)
    self.ui.b_Cobrar.setEnabled(True)

    #Configurar apariencia de botones
    self.ui.b_Buscar.setStyleSheet ('''
      QPushButton::active {
        background-color: rgb(240, 240, 240); border-width: 1px;
        border-style: solid; border-color: black; border-radius: 14px;
        }
      QPushButton::!active {
        background-color: rgb(255, 255, 255); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
        }
      QPushButton::hover {
        background-color: rgb(220, 220, 220); border-width: 1px;
        border-style: solid; border-color: black; border-radius: 14px;
        }
      QPushButton::pressed {
        background-color: rgb(200, 200, 200); border-width: 1px;
        border-style: solid; border-color: black; border-radius: 14px;
        }
    ''')

    self.ui.b_Actualizar.setStyleSheet('''
      QPushButton::active {
        background-color: rgb(170, 200, 255); border-width: 1px;
        border-style: solid; border-color: navy; border-radius: 14px;
        }
      QPushButton::!active {
        background-color: rgb(255, 255, 255); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
        }
      QPushButton::hover {
        background-color: rgb(150, 178, 225); border-width: 1px;
        border-style: solid; border-color: navy; border-radius: 14px;
        }
      QPushButton::pressed {
        background-color: rgb(130, 154, 195); border-width: 1px;
        border-style: solid; border-color: navy; border-radius: 14px;
        }
    ''')

    
    self.ui.b_Eliminar.setStyleSheet('''
      QPushButton::active {
        background-color: rgb(255, 230, 150); border-width: 1px;
        border-style: solid; border-color: orange; border-radius: 14px;
        }
      QPushButton::!active {
        background-color: rgb(255, 255, 255); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
        }
      QPushButton::hover {
        background-color: rgb(240, 216, 141); border-width: 1px;
        border-style: solid; border-color: orange; border-radius: 14px;
        }
      QPushButton::pressed {
        background-color: rgb(220, 198, 129); border-width: 1px;
        border-style: solid; border-color: orange; border-radius: 14px;
        }
    ''')
    
    self.ui.b_Cancelar.setStyleSheet('''
      QPushButton::active {
        background-color: rgb(250, 200, 170); border-width: 1px;
        border-style: solid; border-color: darkred; border-radius: 14px;
        }
      QPushButton::!active {
        background-color: rgb(255, 255, 255); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
        }
      QPushButton::hover {
        background-color: rgb(240, 192, 164); border-width: 1px;
        border-style: solid; border-color: darkred; border-radius: 14px;
        }
      QPushButton::pressed {
        background-color: rgb(220, 176, 150); border-width: 1px;
        border-style: solid; border-color: darkred; border-radius: 14px;
        }
    ''')
    
    self.ui.b_Cobrar.setStyleSheet('''
      QPushButton::active {
        background-color: rgb(135, 250, 120); border-width: 1px;
        border-style: solid; border-color: green; border-radius: 14px;
        }
      QPushButton::!active {
        background-color: rgb(255, 255, 255); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
        }
      QPushButton::hover {
        background-color: rgb(120, 222, 106); border-width: 1px;
        border-style: solid; border-color: green; border-radius: 14px;
        }
      QPushButton::pressed {
        background-color: rgb(100, 185, 88); border-width: 1px;
        border-style: solid; border-color: green; border-radius: 14px;
        }
    ''')

    self.ui.b_Usuarios.setStyleSheet('''
      QPushButton::active {
        background-color: rgb(240, 240, 240); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
        }
      QPushButton::!active {
        background-color: rgb(255, 255, 255); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
        }
      QPushButton::hover {
        background-color: rgb(220, 220, 220); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
        }
      QPushButton::pressed {
        background-color: rgb(200, 200, 200); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
        }
    ''')

    self.ui.b_Cupon.setStyleSheet('''
      QPushButton::active {
        background-color: rgb(240, 240, 240); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
      }
      QPushButton::!active {
        background-color: rgb(255, 255, 255); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
      }
      QPushButton::hover {
        background-color: rgb(220, 220, 220); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
      }
      QPushButton::pressed {
        background-color: rgb(200, 200, 200); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
      }
    ''')

    self.ui.b_Inventario.setStyleSheet('''
      QPushButton::active {
        background-color: rgb(240, 240, 240); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
      }
      QPushButton::!active {
        background-color: rgb(255, 255, 255); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
      }
      QPushButton::hover {
        background-color: rgb(220, 220, 220); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
      }
      QPushButton::pressed {
        background-color: rgb(200, 200, 200); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
      }
    ''')

    self.ui.b_Ticket.setStyleSheet('''
      QPushButton::active {
        background-color: rgb(240, 240, 240); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
      }
      QPushButton::!active {
        background-color: rgb(255, 255, 255); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
      }
      QPushButton::hover {
        background-color: rgb(220, 220, 220); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
      }
      QPushButton::pressed {
        background-color: rgb(200, 200, 200); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
      }
    ''')

    self.ui.b_Cerrar.setStyleSheet('''
      QPushButton::active {
        background-color: rgb(250, 200, 170); border-width: 1px;
        border-style: solid; border-color: darkred; border-radius: 14px;
      }
      QPushButton::!active {
        background-color: rgb(255, 255, 255); border-width: 1px;
        border-style: solid; border-color: grey; border-radius: 14px;
      }
      QPushButton::hover {
        background-color: rgb(240, 192, 164); border-width: 1px;
        border-style: solid; border-color: darkred; border-radius: 14px;
      }
      QPushButton::pressed {
        background-color: rgb(220, 176, 150); border-width: 1px;
        border-style: solid; border-color: darkred; border-radius: 14px;
      }
    ''')

    #Deshabilitar edicion de columnas especificas
    delegar = ReadOnlyDelegate(self.ui.t_Ventas)
    for indice, columna in enumerate((0, 1, 3, 4, 5),start=0):
      self.ui.t_Ventas.setItemDelegateForColumn(columna, delegar)
    
    #renglones = self.ui.t_Ventas.rowCount()
    #spinbox = QtWidgets.QSpinBox()
    #for i in renglones:
    #  self.ui.t_Ventas.setCellWidget(i, 2, QtWidgets.QSpinBox())
    ##self.ui.t_Ventas.setItemDelegateForColumn(0, delegar)
    ##self.ui.t_Ventas.setItemDelegateForColumn(1, delegar)


    #********* Cargar tabla de datos temporal ********
    self.fn_Leer_Datos_BDTemporal()

    self.ui.b_Usuarios.setEnabled(False)
    self.ui.b_Cupon.setEnabled(False)
    self.ui.b_Inventario.setEnabled(True)
    self.ui.b_Ticket.setEnabled(False)
    
    #Deshabilitar las cajas de texto
    self.ui.t_Ticket.setEnabled(False)
    self.ui.t_Importe.setEnabled(False)
    self.ui.t_Descuento.setEnabled(False)
    self.ui.t_IVA.setEnabled(False)
    self.ui.t_Total.setEnabled(False)
    self.ui.t_Ventas.setEnabled(True)

    
    


    #Acción de botones
    self.ui.b_Cerrar.clicked.connect(self.Abrir_Login)
    self.ui.b_Inventario.clicked.connect(self.Abrir_Gestion_Inventario)
    self.ui.b_Buscar.clicked.connect(self.Abrir_Productos)

    ## --------------- EJEMPLO -------------- ##
    self.ui.b_Cobrar.clicked.connect(self.fn_Leer_Datos_BDTemporal)
    ## --------------- EJEMPLO -------------- ##
    
    #Cargar dato de Usuario y Nivel en la ventana
    self.ui.L5.setText(self.fn_tmp_Datos()[0])
    #Cambiar formato del Label
    self.ui.L5.setFont(QFont("Calibri", 11))
    self.ui.L5.setStyleSheet("QLabel {color: rgb(170, 170, 170)}")

    self.ui.L6.setText(self.fn_tmp_Datos()[1])
    #Cambiar formato del Label
    self.ui.L6.setFont(QFont("Calibri", 11))
    self.ui.L6.setStyleSheet("QLabel {color: rgb(170, 170, 170)}")
  
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Productos")
    miCursor = miConexion.cursor()
    #Crear Base de Datos si no existe
    miCursor.execute('''
      CREATE TABLE IF NOT EXISTS Inventario (
      SKU VARCHAR(5) PRIMARY KEY,
      Producto VARCHAR(1000),
      Categoria VARCHAR(50),
      Inventario INTEGER(4),
      Precio REAL(4),
      Descuento REAL(4))
      ''')
    
    #Productos = [
    #  ("P001", "Teclado HTP-10054", "Periferico", 15, 1450.5, 0)
    #  ]
    
    #miCursor.executemany("INSERT INTO Inventario VALUES (?, ?, ?, ?, ?, ?)", Productos)
    #miConexion.commit()
    #miConexion.close()


  # ----------------- Funciones para Abrir Ventanas ----------------- #
  def Abrir_Login(self):
    self.destroy()
    ventana = m_Login
    ventana.start()

  def Abrir_Gestion_Inventario(self):
    #Abrir gestion de inventario si se tienen derechos de administrador
    if self.ui.L6.text() == "Administrador":
      ventana = m_Inventario
      ventana.start()
    else:
      self.msg_info("Sin derechos de acceso", "No tienes nivel de administrador para"
                       + '\n' + "hacer modificaciones en el inventario")

  def Abrir_Productos(self):
    ventana = m_Productos
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

#Función para cargar datos de Usuario desde la Base de Datos temporal
  def fn_tmp_Datos(self):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    #Conusltar datos en la Base de Datos temporal
    miCursor.execute("SELECT Usuario, Nivel FROM TEMP LIMIT 0, 1")
    #Extraer el usuario del renglon 1 en formato de Lista
    r = miCursor.fetchall()
    #Extraer datos de la lista usando la posición 0 de la lista
    Datos = r[0]
    #Cerrar conexion de Base de Datos
    miConexion.close()
    #La fucnion adquiere el valor de Datos en forma de Tupla
    return Datos

  def fn_Leer_Datos_BDTemporal(self):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Productos")
    miCursor = miConexion.cursor()
    #Crear Base de Datos si no existe
    miCursor.execute('''
      CREATE TABLE IF NOT EXISTS TEMP (
      SKU VARCHAR(5),
      Producto VARCHAR(1000),
      Cantidad INTEGER(4),
      Precio REAL(4),
      Descuento REAL(4),
      Importe REAL(4))
      ''')

    #miCursor.execute('''
    #  CREATE TABLE IF NOT EXISTS TEMP (
    #  SKU VARCHAR(5) PRIMARY KEY,
    #  Producto VARCHAR(1000),
    #  Cantidad VARCHAR(4),
    #  Precio VARCHAR(4),
    #  Descuento VARCHAR(4),
    #  Importe VARCHAR(4))
    #  ''')

    #Pedido = [
    #  ("P001", "Teclado HTP-10054", 1, 1450.5, 0, 1450.5),
    #  ("P002", "Teclado HTP-2", 2, 145.5, 0, 145.5),
    #  ("P003", "Teclado HTP-3", 3, 14.5, 0, 14.5)]
      
    #miCursor.executemany("INSERT INTO TEMP VALUES (?, ?, ?, ?, ?, ?)", Pedido)
    #miConexion.commit()
    #miConexion.close()

    #Contar cantidad de renglones en Base de Datos Temporal
    #miCursor.execute("SELECT count(*) FROM TEMP")
    #renglones = miCursor.fetchall()
    #renglones = renglones[0]
    #renglones = renglones[0]

    #Extraer los datos en la Base de Datos Temporal
    miCursor.execute("SELECT * FROM TEMP")
    datos = miCursor.fetchall()

    #spinbox = QtWidgets.QSpinBox()
    r = 0
    for valor in datos:
      #Agrega lista seleccionable para la cantidad
      spinbox = QtWidgets.QSpinBox()
      spinbox.setValue(valor[2])

      self.ui.t_Ventas.setRowCount(r + 1)
      self.ui.t_Ventas.setItem(r, 0, QTableWidgetItem(str(valor[0])))
      self.ui.t_Ventas.setItem(r, 1, QTableWidgetItem(str(valor[1])))
      self.ui.t_Ventas.setCellWidget(r, 2, spinbox)
      self.ui.t_Ventas.setItem(r, 3, QTableWidgetItem(str(valor[3])))
      self.ui.t_Ventas.setItem(r, 4, QTableWidgetItem(str(valor[4])))
      self.ui.t_Ventas.setItem(r, 5, QTableWidgetItem(str(valor[5])))
      #Pasar al siguiente renglón
      r = r + 1
    miConexion.close()

#Clase para devolver un valor nulo en caso de que la columna sea editable  
class ReadOnlyDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return

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


