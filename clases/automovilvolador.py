from clases.automovil import Automovil
class AutomovilVolador(Automovil):
  ruedas=6
  
#Agregar al constructor esta_volando=True
  def __init__(self,anno,modelo,color,marca,aceleracion,esta_volando=True):
    super().__init__(anno,modelo,color,marca,aceleracion)
    self.esta_volando=esta_volando
  #Agregar métodos vuela y aterriza(esta_volando)
  def vuela(self):
    self.esta_volando=True
  def aterriza(self):
    self.esta_volando=False
  #Crear un método Datos() para saber el tipo de auto que es y la cantidad de ruedas que tiene en las clases Automovil y AutomovilVolador
  def datos(self):
    return f" Es un Automovil Volador de {self.ruedas}"
