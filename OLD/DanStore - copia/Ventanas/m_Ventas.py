#Importar librerias necesarias
import sys
import sqlite3

#Importar ventana de Login creada en QT Designes  y exportada a python
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QTableWidget
from PyQt5.QtCore import Qt
from Pantallas.f_Ventas import Ui_MainWindow
from PyQt5.QtGui import QFont

#Importar módulos para abrir otras ventanas
import Ventanas.m_Login as m_Login
import Ventanas.m_Registro as m_Registro
import Ventanas.m_Inventario as m_Inventario
import Ventanas.m_Productos as m_Productos
import Ventanas.m_Cobro as m_Cobro
import Ventanas.m_Cupon as m_Cupon

#Importar módulo m_Constantes
import Ventanas.m_Constantes as C

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
    
    self.ui.t_Ventas.setEnabled(True)

    
    # ----------- CONFIGURACIÓN APARIENCIA DE BOTONES ----------- #
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

    # ------------------ CONFIGURACIÓN DE TABLA ------------------ #
    #Deshabilitar edicion de columnas especificas
    delegar = ReadOnlyDelegate(self.ui.t_Ventas)
    for indice, columna in enumerate((0, 1, 3, 4, 5),start=0):
      self.ui.t_Ventas.setItemDelegateForColumn(columna, delegar)
    # Deshabilitar el comportamiento de arrastrar y soltar
    self.ui.t_Ventas.setDragDropOverwriteMode(False)
    # Seleccionar toda la fila
    self.ui.t_Ventas.setSelectionBehavior(QTableWidget.SelectRows)
    # Seleccionar una fila a la vez
    self.ui.t_Ventas.setSelectionMode(QTableWidget.SingleSelection)
    # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
    # textos que no encajan
    self.ui.t_Ventas.setWordWrap(True)
    self.ui.t_Ventas.setTextElideMode(Qt.ElideNone)    #Qt.ElideRight
    # Deshabilitar clasificación
    self.ui.t_Ventas.setSortingEnabled(False)
    # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
    self.ui.t_Ventas.horizontalHeader().setHighlightSections(False)
    # Establecer ancho de las columnas
    for indice, ancho in enumerate((50, 427, 85, 80, 85, 85), start=0):
        self.ui.t_Ventas.setColumnWidth(indice, ancho)


    # ---------- Cargar tabla de datos temporal ********
    self.fn_Leer_Datos_BDTemporal()

    #Generar ticket y ponerlo en la caja de texto correspondiente al iniciar
    self.fn_Generar_Ticket()

    #Establecer estado de los botones al iniciar
    self.ui.b_Usuarios.setEnabled(False)
    self.ui.b_Cupon.setEnabled(True)
    self.ui.b_Inventario.setEnabled(True)
    self.ui.b_Ticket.setEnabled(True)
    
    #Deshabilitar las cajas de texto a solo lectura
    self.ui.t_Ticket.setReadOnly(True)
    self.ui.t_Importe.setReadOnly(True)
    self.ui.t_Descuento.setReadOnly(True)
    self.ui.t_Cupon.setReadOnly(True)
    self.ui.t_Subtotal.setReadOnly(True)
    self.ui.t_IVA.setReadOnly(True)
    self.ui.t_Total.setReadOnly(True)
    

    
    


    #Acción de botones
    self.ui.b_Buscar.clicked.connect(self.Abrir_Productos)
    # ACTUALIZAR
    self.ui.b_Eliminar.clicked.connect(self.fn_Eliminar_Producto)
    self.ui.b_Cancelar.clicked.connect(self.fn_Limpiar_BD)
    self.ui.b_Cobrar.clicked.connect(self.Abrir_Cobro)

    #USUARIOS ***
    self.ui.b_Cupon.clicked.connect(self.Abrir_Cupon)
    self.ui.b_Inventario.clicked.connect(self.Abrir_Gestion_Inventario)
    #TICKET
    self.ui.b_Cerrar.clicked.connect(self.Abrir_Login)
    
    
    ## --------------- EJEMPLO -------------- ##
    #self.ui.b_Cobrar.clicked.connect(self.fn_Leer_Datos_BDTemporal)

    #self.ui.b_Ticket.clicked.connect()
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



    # --- BUG --- #
    #Crea un ciclo infino al volver a cargar los datos a la tabla
    #self.ui.t_Ventas.cellChanged.connect(self.fn_Cantidad_Cambio)
    # --- BUG --- #
  def fn_Generar_Ticket(self):
    #Generar texto de ticket con el consecutivo de la base de datos
    Consecutivo = self.fn_Consecutivo_Ticket()
    Ticket = "Ticket # " + str(Consecutivo).zfill(4)

    return Ticket
    #Cargar el número de ticket en la caja de texto correspondiente
    self.ui.t_Ticket.setText(Ticket)

  def fn_Cantidad_Cambio(self):
    seleccion = self.ui.t_Ventas.selectedItems()
    r = self.ui.t_Ventas.currentRow()
    sku = seleccion[0].data(0)
    cantidad = int(seleccion[2].data(0))
    precio = float((seleccion[3].data(0)).replace(",",""))  #Quitar separador miles
    descuento = float(seleccion[4].data(0))
    #Calcular importe con la funcion creada en el módulo m_Productos
    importe = m_Productos.Productos_GUI.fn_Calcular_Importe(m_Productos.Productos_GUI, 
                                                            cantidad, precio, descuento)
    #importe = self.fn_Calcular_Importe(cantidad, precio, descuento)
    
    print(importe)
    print(r)

    ##Actualizar la cantidad en la Base de Datos temporal
    #self.fn_Actualizar_Cantidad(sku, cantidad, importe)
    ###Usando la funcion creada en el módulo m_Productos
    m_Productos.Productos_GUI.fn_Actualizar_Cantidad(m_Productos.Productos_GUI,
                                                     sku, cantidad, importe)
    
    #self.ui.t_Ventas.setItem(0, 5, QTableWidgetItem(f"{importe:,}")) #Separador miles
    
    ##Limpiar tabla
    #self.fn_Limpiar_Tabla()
    
    ##Actualizar tabla
    #self.fn_Leer_Datos_BDTemporal()



  #  #self.ui.t_Ventas.currentCellChanged.connect(self.fn_Prueba)
  #  self.ui.t_Ventas.currentItemChanged.connect(self.fn_Prueba)

  #def fn_Prueba(self):
  #  #seleccion = self.ui.t_Ventas.selectedItems()

  #  #if seleccion:
  #    celda = self.ui.t_Ventas.cellWidget(1,2).value()
    
  #    print(celda)

  #    item = self.ui.t_Ventas.currentItem()
  #    a = item.row()
  #    b = item.column()

  #    print ("renglon " + str(a))
  #    print ("columna " + str(b))



    #self.ui.t_Ventas.celledi

  #  self.ui.t_Ventas.currentCellChanged.connect(self.fn_Prueba)
  
  #def fn_Prueba(self):
  #  seleccion = self.ui.t_Ventas.selectedItems()
  #  if seleccion:
  #    spin = QtWidgets.QSpinBox()
  #    a = spin.value()
  #    b = self.spin
  #    print("OK")
  #    print(a)
    #dat = selec[0].dat[0]


  
    
    #self.ui.t_Ventas.cellChanged.connect(self.on_cell_changed)
    #self.ui.t_Ventas.itemChanged.connect(self.on_item_changed)
  #def fn_Cambio(self, row: int, col: int):
  #  print(f"cambio spinbox ({row}, {col})")

  #def on_cell_changed(self, row: int, col: int) -> None:
  #      print(f"Se modificó la celda ({row}, {col})")

  #def on_item_changed(self, item: QtWidgets.QTableWidgetItem) -> None:
  #      print(f"Se modificó el item en posición ({item.row()}, {item.column()})")


  



  #Función para verificar que se haya seleccion en la tabla
  def fn_Seleccion_Existente(self):
    seleccion = self.ui.t_Ventas.selectedItems()
    if seleccion:
      return "Si"
    else:
      return "No"
  
   



# --------- Funciones para Administrar acciones en SQLite --------- #

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
      Importe REAL(6),
      Cupon REAL(4))
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
    miConexion.close()
    #spinbox = QtWidgets.QSpinBox()
    r = 0
    for valor in datos:
      #Agrega lista seleccionable para la cantidad
      spinbox = QtWidgets.QSpinBox()
      spinbox.setRange(1, 10000)
      spinbox.setStyleSheet('color: rgb(0, 160, 245);')
      spinbox.setFrame(False)
      fuente = QFont("Calibri", 11)
      spinbox.setFont(fuente)
      spinbox.setValue(valor[2])
      

      self.ui.t_Ventas.setRowCount(r + 1)
      self.ui.t_Ventas.setItem(r, 0, QTableWidgetItem(str(valor[0])))
      self.ui.t_Ventas.setItem(r, 1, QTableWidgetItem(str(valor[1])))
      #self.ui.t_Ventas.setCellWidget(r, 2, spinbox)
      self.ui.t_Ventas.setItem(r, 2, QTableWidgetItem(str(valor[2])))
      self.ui.t_Ventas.setItem(r, 3, QTableWidgetItem(f"{valor[3]:,}"))
      self.ui.t_Ventas.setItem(r, 4, QTableWidgetItem(str(valor[4])))
      self.ui.t_Ventas.setItem(r, 5, QTableWidgetItem(f"{valor[5]:,}"))
      #Pasar al siguiente renglón
      r = r + 1
    #Autoajustar renglon para que se muestre todo el texto
    #self.ui.t_Ventas.resizeRowsToContents()
    
    #Cargar montos en cajas de texto correspondientes
    self.fn_Cargar_Montos()
    
    ##miConexion.close()
  
  #Función para sumar los valores del importe de la Base Temporal
  def fn_Cargar_Montos(self):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Productos")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT Importe FROM TEMP")
    datos_importe = miCursor.fetchall()

    importes = []
    for valor in datos_importe:
      importes.append(valor[0])

    miCursor.execute("SELECT Cantidad, Precio FROM TEMP")
    datos_precio = miCursor.fetchall()

    precios = []
    for valor in datos_precio:
      precios.append(valor[0] * valor[1])

    Descuento_Cupon = self.fn_Cupon()

    #Cálculo de montos
    Total = round(sum(importes), 2)
    Cupon = round((Descuento_Cupon/100) * Total, 2)
    Calculo_Descuento = round(sum(precios)- Total, 2)
    Calculo_Importe = round(sum(precios), 2)
    Calculo_Subtotal = round(Calculo_Importe - Calculo_Descuento - Cupon, 2)
    Calculo_IVA = round(Calculo_Subtotal - (Calculo_Subtotal / (1 + C.IVA)), 2)
    Calculo_Total = round(Calculo_Subtotal + Calculo_IVA)

    #Cargar datos a los cuadros de texto correspondientes
    self.ui.t_Importe.setText("$ " + f"{Calculo_Importe:,}")
    self.ui.t_Descuento.setText("- $ " + f"{Calculo_Descuento:,}")
    self.ui.t_Cupon.setText("- $ " + f"{Cupon:,}")
    self.ui.t_IVA.setText("$ " + f"{Calculo_IVA:,}")
    self.ui.t_Subtotal.setText("$ " + f"{Calculo_Subtotal:,}")
    self.ui.t_Total.setText("$ " + f"{Calculo_Total:,}")

    miConexion.close()

    #return Total
    
  def fn_Calcular_Total(self):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Productos")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT Importe FROM TEMP")
    datos_importe = miCursor.fetchall()

    importes = []
    for valor in datos_importe:
      importes.append(valor[0])

    Total = round(sum(importes), 2)

    return Total

  
  def fn_Eliminar_Producto(self):
    if self.fn_Seleccion_Existente() == "Si":
      #Obtener datos de la selección
      seleccion = self.ui.t_Ventas.selectedItems()
      sku = seleccion[0].data(0)

      #Mensaje de confirmación
      if self.msg_confirmacion("Confirmación", "¿Estas seguro que quieres "
                                + f"eliminar el producto {sku}?") == "Eliminar":
        
        #Abrir Base de Datos con SQLite3
        miConexion = sqlite3.connect("Productos")
        miCursor = miConexion.cursor()

        #Eliminar producto después de la confirmación
        miCursor.execute("DELETE FROM TEMP WHERE SKU = ?", [sku])
        
        #Confirmar y cerrar Base de Datos
        miConexion.commit()
        miConexion.close()

        #Limpiar tabla
        self.fn_Limpiar_Tabla()
        #Actualizar tabla
        self.fn_Leer_Datos_BDTemporal()

    elif self.fn_Seleccion_Existente() == "No":
      self.msg_info("Sin selección", "No has seleccionado ningún producto."
                    + '\n' + "Favor de seleccionar un producto.")

  def fn_Limpiar_BD(self):
    #Mensaje de confirmación
    if self.msg_confirmacion("Confirmación", "¿Estas seguro que quieres "
                              + f"eliminar TODOS los productos?") == "Eliminar":
      #Abrir Base de Datos con SQLite3
      miConexion = sqlite3.connect("Productos")
      miCursor = miConexion.cursor()

      #Eliminar todos los productos después de la confirmación
      miCursor.execute("DELETE FROM TEMP")
      
      #Confirmar y cerrar Base de Datos
      miConexion.commit()
      miConexion.close()

      #Limpiar tabla
      self.fn_Limpiar_Tabla()
      #Actualizar tabla
      self.fn_Leer_Datos_BDTemporal()

  def fn_Actualizar_Cantidad(self, sku, cantidad, importe):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Productos")
    miCursor = miConexion.cursor()

    #Actualizar la cantidad en el producto
    miCursor.execute("UPDATE TEMP SET Cantidad = ?, Importe = ? WHERE SKU = ?", 
                      [cantidad, importe, sku])
    miConexion.commit()
    miConexion.close()

  def fn_Limpiar_Tabla(self):
    self.ui.t_Ventas.clearContents()
    self.ui.t_Ventas.setRowCount(1)

  def fn_Consecutivo_Ticket(self):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Ventas")
    miCursor = miConexion.cursor()
    #Crear Base de Datos si no existe
    miCursor.execute('''
      CREATE TABLE IF NOT EXISTS Ticket (
      ID INTEGER PRIMARY KEY AUTOINCREMENT,
      TK VARCHAR(5),
      SKU VARCHAR(5),
      Producto VARCHAR(1000),
      Cantidad INTEGER(4),
      Precio REAL(4),
      Descuento REAL(4),
      Importe REAL(6),
      Estaus VARCHAR(9))
      ''')

    #Generar ID en la tabla Ticket
    miCursor.execute("INSERT INTO Ticket (ID) VALUES (NULL)")
    miConexion.commit()

    miCursor.execute("SELECT * FROM Ticket ORDER BY ID DESC LIMIT 1")
    Consecutivo = miCursor.fetchone()[0]

    return Consecutivo
  
  def fn_Cupon(self):
    #Abrir Base de Datos con SQLite3
    miConexion = sqlite3.connect("Productos")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT Cupon FROM TEMP")
    cupon = miCursor.fetchone()[0]

    return cupon

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
    self.close()
    ventana = m_Productos
    ventana.start()

  def Abrir_Cobro(self):
    self.close()
    ventana = m_Cobro
    ventana.start()

  def Abrir_Cupon(self):
    ventana = m_Cupon
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


  # ------------- Funciones para Eventos en la ventana  ------------- #
  #Evento para cuando la ventana se cierra
  def closeEvent(self, event):
    self.fn_Cerrar_Ventana()


  #Cerrar ventana
  def fn_Cerrar_Ventana(self):
    #self.destroy()
    #self.Abrir_Login()
    
    # == TEMPORAL == #
    self.close()

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


