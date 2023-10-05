from clases.automovil import Automovil
from clases.automovilvolador import AutomovilVolador


print("Hola desde Replit")
#-Crear una clase Automóvil con tenga por defecto atributo ruedas inicializado en 4, con un constructor con los parámetros de color, marca, aceleracion y velocidad


  #Crear un coche, mostrar por consola las ruedas y la aceleración
coche1=Automovil("rojo","Toyota",20)
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
automoVolador1=AutomovilVolador("red","Ford",30,True)
automoVolador2=AutomovilVolador("negro","Audi",50,False)
print(automoVolador1.vuela())


print("*********************clase ************")





