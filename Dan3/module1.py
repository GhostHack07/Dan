# Ejemplo de exportacion de variables
def f_Casos(a):
  if a == 1:
    Caso = "Nuevo"
  if a == 2:
    Caso = "Actualizar"
  if a == 3:
    Caso = "Eliminar"
  return Caso

valor = int(input("Valor de a: "))
print(f_Casos(valor))
if f_Casos(valor) == "Nuevo":
  print("Buen trabajo")
