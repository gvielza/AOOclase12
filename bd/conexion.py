import sqlite3
class Conexion:
  def __init__(self,nombre_base_datos):
    self.conexion=sqlite3.connect(nombre_base_datos)
    self.cursor=self.conexion.cursor()

  def crear_tabla(self):
    self.cursor.execute('''CREATE TABLE IF NOT EXISTS vehiculos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
anno INTEGER ,
modelo TEXT
)  ''')
    self.conexion.commit()
  def agregar_vehiculo(self,anno,modelo):
    self.cursor.execute('''INSERT INTO vehiculos(anno, modelo)VALUES(?,?)''',(anno,modelo))
    self.conexion.commit()
  def listar_clientes(self):
    self.cursor.execute(''' SELECT * from vehiculos''')
    vehiculos=self.cursor.fetchall()
    return vehiculos
  def cerrar_bd(self):
    self.cursor.close()
    self.conexion.close()
  def modificar_vehiculos(self,anno,modelo,id):
    self.cursor.execute('''UPDATE vehiculos set anno=?, modelo=? WHERE id=?''',(anno,modelo,id))
    self.conexion.commit()
  def eliminar(self,id):




    