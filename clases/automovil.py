from clases.vehiculo import Vehiculo
from abc import ABC, abstractmethod


class Automovil(Vehiculo):
  ruedas=4
  def __init__(self,anno, modelo,color,marca,aceleracion):
    super().__init__(anno,modelo)
    self.color=color
    self.marca=marca
    self.aceleracion=aceleracion
    self.velocidad=0
  def acelera(self):
    self.velocidad=self.aceleracion+self.velocidad
  def frena(self):
    self.velocidad=self.velocidad-self.aceleracion
  @abstractmethod
  def conducir():
    return "Conduciendo el automovil"
    pass
  #Crear un método Datos() para saber el tipo de auto que es y la cantidad de ruedas que tiene en las clases Automovil y AutomovilVolador
  def datos(self):
    #return f" Es un {__class__.__name__} de {self.ruedas} "
    return f" Es un Automovil de {self.ruedas} "

  
    