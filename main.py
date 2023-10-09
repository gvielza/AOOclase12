from clases.automovil import Automovil
from clases.automovilvolador import AutomovilVolador
from clases.vehiculo import Vehiculo
import sqlite3 as sql


print("Hola desde Replit")
#-Crear una clase Automóvil con tenga por defecto atributo ruedas inicializado en 4, con un constructor con los parámetros de color, marca, aceleracion y velocidad


  #Crear un coche, mostrar por consola las ruedas y la aceleración
coche1=Automovil(2020,"Etios","rojo","Toyota",20)
print(coche1.ruedas)
print(f'El coche tiene una aceleracion de {coche1.aceleracion}')
#Modificar la aceleración y mostrar por pantalla ambas aceleraciones
coche1.aceleracion=30
print(coche1.aceleracion)

#Crear método acelera() que aumentará la velocidad + aceleración
#7-Crear método frena() que restará a la velocidad la aceleración
print(f'El coche tiene una velocidad de {coche1.velocidad}')
coche1.acelera()
print(f'El coche tiene una velocidad de {coche1.velocidad}')
coche1.frena()
print(f'El coche tiene una velocidad de {coche1.velocidad}')

#1-Crear clase AutomovilVolador que herede de Automovil con atributo de 6 ruedas

#Crear un automovilvolador y muestre por consola comportamiento y características 
automoVolador1=AutomovilVolador(2020,"Focus","red","Ford",30,True)
automoVolador2=AutomovilVolador(2010,"A1","negro","Audi",50,False)



print("*********************clase 14 ************")
#creamos un vehiculo
vehiculo1=Vehiculo(2020,"ddd")
print(vehiculo1._anno)
#print(vehiculo1.__modelo)
auto1=Automovil(2020,"A3","red","Audi",20)
print(auto1._anno)
#print(auto1.__modelo)
print(auto1.get_modelo())
auto1.set_modelo("A4")
print(auto1.get_modelo())
print(auto1.datos())
print(automoVolador1.datos())

#-Cree un método en el raíz del proyecto que devuelva dado un vehículo sus datos 
def datos_vehiculo(auto):
  return auto.datos()
auto_prueba=Automovil(2020,"Se","black","Fiat",20)
print(datos_vehiculo(auto=auto_prueba))

#1-Crear una base de datos en carpeta bd Ej: “mi_bd.db”
#2-Crear conector y cursor
#3-Crear una tabla vehículo que contendrá los atributos correspondientes a la clase vehiculo
#4-Crear un vehículo e insertarlo en la base de datos
#5-Leer los vehículos de la base de datos y mostrarlo por pantalla

print("Conectar a sqlite3")
conexion=sql.connect("bd/mi_bd.db")
cursor=conexion.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS vehiculos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
anno INTEGER ,
modelo TEXT
)  ''')
conexion.commit()
vehiculo1=Vehiculo(2020,"ddd")
vehiculo1=Vehiculo(1999,"falcon")
cursor.execute('''INSERT INTO vehiculos(anno, modelo)VALUES(?,?)''',(vehiculo1.get_anno(),vehiculo1.get_modelo()))
cursor.execute('''INSERT INTO vehiculos(anno, modelo)VALUES(?,?)''',(vehiculo1.get_anno(),vehiculo1.get_modelo()))
conexion.commit()

cursor.execute('''SELECT * from vehiculos''')
resultados=cursor.fetchall()

for file in resultados:
  print(file)



cursor.close()
conexion.close()




