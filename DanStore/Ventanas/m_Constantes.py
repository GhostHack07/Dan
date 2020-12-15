# ---------------       C O N S T A N T E S       ----------------- #
import sqlite3


## CATEGORIAS ##
def Constante_Categorias():
  #Abrir Base de Datos con SQLite3
  miConexion = sqlite3.connect("Productos")
  miCursor = miConexion.cursor()

  miCursor.execute("SELECT Categoria FROM Inventario")
  #Extraer todas las categorias de la Base de Datos
  datos = miCursor.fetchall()
  miConexion.close()
  #Extraer categorias diferentes como segmento
  grupo = set(datos)
  #Acomodar categorias diferentes
  categorias = []
  for valor in grupo:
    categorias.append(valor[0])
  
  return categorias

## CANTIDAD DE CARACTERES PARA SKU ##
caracteres_sku = 5


#### PRODUCTOS ##
##def Constante_Productos():
##  #Abrir Base de Datos con SQLite3
##  miConexion = sqlite3.connect("Productos")
##  miCursor = miConexion.cursor()

##  miCursor.execute("SELECT Producto FROM Inventario")
##  #Extraer todas las categorias de la Base de Datos
##  datos = miCursor.fetchall()
##  miConexion.close()
##  #Extraer categorias diferentes como segmento
##  grupo = set(datos)
##  #Acomodar categorias diferentes
##  productos = []
##  for valor in grupo:
##    productos.append(valor[0])
  
##  return productos
