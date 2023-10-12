# Implementa un sistema para un supermercado, que  le permita a los usuarios ingresar clientes(nombre, apellido, dni) a la base de datos sqlite3 por consola, editar, eliminar y mostrar todos clientes, de acuerdo a la opción seleccionada.

import sqlite3

class Conexion:
  def __init__(self,nombre_bd):
    self.nombre_bd=nombre_bd
    self.conexion=sqlite3.connect(nombre_bd)
    self.cursor=self.conexion.cursor()
  def crear_tabla(self):
    self.cursor.execute('''CREATE TABLE IF NOT EXISTS CLIENTE(
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    dni TEXT
    )''')
    self.conexion.commit()
  def insertar_cliente(self, nombre, apellido, dni):
    self.cursor.execute('''INSERT INTO cliente (nombre, apellido, dni) VALUES (?,?,?)''',(nombre, apellido, dni))
    self.conexion.commit()
  def editar_cliente(self,nombre,apellido,dni,id):
    self.cursor.execute('''UPDATE cliente SET nombre=?, apellido=?, dni=? WHERE id=?''',(nombre,apellido,dni,id))
    self.conexion.commit()
  def eliminar_cliente(self,id):
    self.cursor.execute('''DELETE FROM cliente WHERE id=?''',(id,))
    self.conexion.commit()
  def mostrar_clientes(self):
    clientes=self.cursor.execute('''SELECT * FROM cliente''')
    return clientes
  def cerrar_conexion(self):
    self.cursor.close()
    self.conexion.close()
