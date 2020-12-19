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
    #self.ui.b_Cobrar.clicked.connect()
    self.ui.b_Cancelar.clicked.connect(self.fn_Cancelar)

    #Acción de botones opcionales Efectivo/ Tarjeta
    self.ui.b_efectivo.clicked.connect(self.fn_botones_acciones)
    self.ui.b_tarjeta.clicked.connect(self.fn_botones_acciones)

    #Comprobar que las celdas tengan datos
    self.ui.D_Pago.textChanged.connect(self.fn_Comprobacion)


    #Cargar Total en las cajas de texto
    self.fn_Cargar_Total()

    #Deshabilitar boton de autolimpieza
    self.ui.D_Pago.setClearButtonEnabled(False)
    
  # ----------------- Funciones para uso de botones ----------------- #
    

  def fn_botones_acciones(self):
    if self.ui.b_efectivo.isChecked():
      #Permitir solo una opción
      self.ui.b_tarjeta.setChecked(False)

      #Deshabilitar caja de texto de Pago
      self.ui.D_Pago.setEnabled(True)

      #Hacer comprobacion
      self.fn_Comprobacion()

    elif self.ui.b_tarjeta.isChecked():
      #Permitir solo una opción
      self.ui.b_efectivo.setChecked(False)

      #Valor de cero en la caja de texto
      self.ui.D_Pago.clear()

      #Deshabilitar caja de texto de Pago
      self.ui.D_Pago.setEnabled(False)

      #Hacer comprobacion
      self.fn_Comprobacion()

      
  def fn_Total(self):
    #Obtener datos del módulo m_Ventas
    Montos = m_Ventas.Ventas_GUI.fn_Calcular_Montos(m_Ventas.Ventas_GUI)
    
    Total = Montos[5]
    return Total

  def fn_Cargar_Total(self):
    #Obtener Total
    Total = self.fn_Total()

    #Poner Total en la caja de texto correspondiente
    self.ui.D_Total.setText("$ " + f"{Total:,.2f}")


  def fn_Cargar_Pago(self, Pago):
    Pago = self.fn_Pago()

    #Poner Total en la caja de texto correspondiente
    self.ui.D_Pago.setText(Pago)
    self.ui.L_Mascara.setText(Pago)

  def fn_Cargar_Mascara(self, Pago):
    if Pago == 0 or Pago == "":
      self.ui.L_Mascara.setText("$ 0.00")
    else:
      #Poner el valor en valor en la mascara
      self.ui.L_Mascara.setText("$ " + f"{Pago:,.2f}")

  def fn_Pago(self):
    Pago = self.ui.D_Pago.text()

    if Pago == "" or Pago == 0:
      Pago = 0
      self.fn_Cargar_Mascara(Pago)
    else:
      #Convertir en numero con punto flotante
      Pago = float(Pago)

    return Pago

  def fn_Calcular_Cambio(self):
    Total = self.fn_Total()
    Pago = self.fn_Pago()

    Cambio = round(Total - Pago, 2)

    return Cambio

  def fn_Cargar_Cambio(self):
    Cambio = self.fn_Calcular_Cambio()

    if Cambio <= 0:
      #Poner Total en la caja de texto correspondiente
      self.ui.D_Cambio.setText("$ " + f"{Cambio:,.2f}")

    elif Cambio > 0:
      #Poner Total en la caja de texto correspondiente
      self.ui.D_Cambio.setText("$ N/A")
      
  def fn_Comprobacion(self):
    if self.fn_Casos() == "Efectivo":
      Pago = self.fn_Pago()
      
      #Comprobar que haya texto escrito
      if not self.ui.D_Pago.text():
        #Deshabilitar boron b_Cobrar
        self.ui.b_Cobrar.setEnabled(False)

      elif self.ui.D_Pago.text():
        #Cargar el valor de Pago en la máscara
        self.fn_Cargar_Mascara(Pago)
        #Cargar el valor del Cambio en la caja de texto
        self.fn_Cargar_Cambio()

        if self.fn_Calcular_Cambio() > 0:
          #Deshabilitar boron b_Cobrar
          self.ui.b_Cobrar.setEnabled(False)

        elif self.fn_Calcular_Cambio() <= 0:
          #Habilitar boron b_Cobrar
          self.ui.b_Cobrar.setEnabled(True)


    elif self.fn_Casos() == "Tarjeta":
      #La cantidad de pago es exacta a la cantidad total
      Pago = self.fn_Total()
      self.fn_Cargar_Mascara(Pago)
      #No hay cambio
      self.ui.D_Cambio.setText("$ 0.00")

      #Habilitar boron b_Cobrar
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


  # --------- Funciones para Administrar acciones en SQLite --------- #
  def fn_Cobrar(self):
    pass


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
