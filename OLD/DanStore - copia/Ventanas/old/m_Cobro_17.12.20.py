#Importar librerias necesarias
import sys

#Importar ventana de Login creada en QT Designes y exportada a python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Pantallas.f_Cobro import Ui_MainWindow

#Libreria para poder validar si los datos son numeros, texto, enteros o
#flotantes
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

#Importar módulo de Ventas
import Ventanas.m_Ventas as m_Ventas

#Variable global para cambio de ventana
window = None

class Cobro_GUI(QtWidgets.QMainWindow):
  #Función para iniciar ventana de Login
  def __init__(self):
    super(Cobro_GUI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    #Habilitar o deshabilitar botones al iniciar
    self.ui.b_Cancelar.setEnabled(True)
    self.ui.b_Cobrar.setEnabled(False)
    
    #Habilitar o deshabilitar Efectivo / Tarjeta
    self.ui.b_efectivo.setChecked(True)
    self.ui.b_tarjeta.setChecked(False)

    #Deshabilitar las cajas de texto a solo lectura
    self.ui.D_Total.setReadOnly(True)
    self.ui.D_Pago.setReadOnly(False)
    self.ui.D_Cambio.setReadOnly(True)

    #Tipo de datos en las cajas de texto
    #Solo acepta números con punto flotante y 2 cifras después del .
    flotante = QRegExp("(([0-9]*[.])?[0-9]{1,2})")
    #Validacion de los caracteres ingresados
    validar_flotante = QRegExpValidator(flotante)

    #Valida que los caracteres ingresados sean válidos
    self.ui.D_Pago.setValidator(validar_flotante)

    #Acción de botón b_Cancelar
    self.ui.b_Cobrar.clicked.connect(self.fn_Calcular_Cambio)
    self.ui.b_Cancelar.clicked.connect(self.fn_Cancelar)

    #Acción de botones opcionales Efectivo/ Tarjeta
    self.ui.b_efectivo.clicked.connect(self.fn_botones_acciones)
    self.ui.b_tarjeta.clicked.connect(self.fn_botones_acciones)

    #Comprobar que las celdas tengan datos
    self.ui.D_Pago.textChanged.connect(self.fn_Comprobacion)

    
    #Cargar Total en las cajas de texto
    self.fn_Cargar_Total()
    
  # ----------------- Funciones para uso de botones ----------------- #

  def fn_botones_acciones(self):
    if self.ui.b_efectivo.isChecked():
      #Para seleccionar solo una opción
      self.ui.b_tarjeta.setChecked(False)

    elif self.ui.b_tarjeta.isChecked():
      #Para seleccionar solo una opción
      self.ui.b_efectivo.setChecked(False)
      self.ui.D_Pago.setText(str(self.fn_Total()))

      
  def fn_Total(self):
    #Obtener datos del módulo m_Ventas
    Total = m_Ventas.Ventas_GUI.fn_Calcular_Total(m_Ventas.Ventas_GUI)
    return Total

  def fn_Cargar_Total(self):
    Total = self.fn_Total()
    #Poner datos en cajas de texto
    self.ui.D_Total.setText("$ " + f"{Total:,}")

  def fn_Cargar_Pago(self):
    Total = self.fn_Total()
    #Poner datos en cajas de texto
    self.ui.D_Pago.setText(Total)

  def fn_Calcular_Cambio(self):
    Total = self.fn_Total()
    Pago = float(self.ui.D_Pago.text())
    Cambio = round(Total - Pago,2)
    #Poner datos en cajas de texto
    self.ui.D_Cambio.setText("$ " + f"{Cambio:,}")
    #Poner valor en mascara
    self.ui.L_Mascara.setText("$ " + f"{Pago:,}")
  


  def fn_Comprobacion(self):
    #Acciones por Caso
    if self.fn_Casos() == "Efectivo":
      if (not self.ui.D_Pago.text() 
          or self.ui.D_Pago.text() == "" 
          or self.ui.D_Pago.text() == 0):
        
        self.ui.L_Mascara.setText("$ 0.00")

        self.ui.b_Cobrar.setEnabled(False)
      else:
        self.ui.b_Cobrar.setEnabled(True)
        
        #Poner datos en cajas de texto
        self.fn_Calcular_Cambio()

    elif self.fn_Casos() == "Tarjeta":
      self.ui.b_Cobrar.setEnabled(True)
      

  def fn_Casos(self):
    if self.ui.b_efectivo.isChecked():
      Caso = "Efectivo"
    if self.ui.b_tarjeta.isChecked():
      Caso = "Tarjeta"
    return Caso

  #Función del boton b_Cancelar
  def fn_Cancelar(self):
    self.fn_Cerrar_Ventana()


  # ------------- Funciones para Eventos en la ventana ------------- #
  #Evento para cuando la ventana se cierra
  def closeEvent(self, event):
    self.fn_Cerrar_Ventana()

  #Cerrar ventana
  def fn_Cerrar_Ventana(self):
    self.destroy()





#Función para iniciar ventana de Cobro
def start():
    global window  
    window = Cobro_GUI()
    window.show()


#Mostrar ventana Login
if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  application = Cobro_GUI()
  application.show()
  sys.exit(app.exec())