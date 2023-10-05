from clases.vehiculo import Vehiculo


class Automovil(Vehiculo):
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
    