import sqlite3
from base_datos.conexion import Conexion
nombre_bd='base_datos/supermercado.db'
conexion=Conexion(nombre_bd)
conexion.crear_tabla()
error = 1
opcion = 0
while error != 0:
    try:
      opcion = int(
          input(
              "Ingrese opcion\n 1-Ingresar cliente \n 2-Mostrar\n 3-Editar cliente \n 4-Eliminar cliente \n 5-Cerrar \n"
          ))
    except ValueError:
      print("Selecciono mal la opcion \n")
      opcion = 0
    if opcion == 1:
      nombre = input("Ingresar nombre: ")
      apellido = input("Ingresar apellido: ")
      dni = input("Ingresar dni: ")
      conexion.insertar_cliente(nombre, apellido, dni)
    if opcion == 2:
      clientes = conexion.mostrar_clientes()
      print("Lista de clientes:")
      for cliente in clientes:
        print(f"nombre: {cliente[1]}, apellido: {cliente[2]}, dni: {cliente[3]} , id: {cliente[0]}"
          )
    if opcion == 3:
      nombre = input("Ingresar nombre: ")
      apellido = input("Ingresar apellido: ")
      dni = input("Ingresar dni: ")
      id = input("Ingrese el id a editar: ")
      conexion.editar_cliente(nombre, apellido, dni, id)
    if opcion == 4:
      id = input("Ingrese el id a eliminar: ")
      conexion.eliminar_cliente(id)
    if opcion == 5:
      print("Cerrar")
      conexion.cerrar_conexion()