print("Hola desde Replit")
#-Crear una clase Automóvil con tenga por defecto atributo ruedas inicializado en 4, con un #constructor con los parámetros de color, marca, aceleracion y velocidad

class Automovil:
  ruedas=4
  def __init__(self,color,marca,aceleracion):
    self.color=color
    self.marca=marca
    self.aceleracion=aceleracion
    self.velocidad=0
  def acelera(self):
    self.velocidad=self.aceleracion+self.velocidad
  def frena(self):
    self.velocidad=self.velocidad-self.aceleracion
    
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
