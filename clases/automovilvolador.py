from clases.automovil import Automovil
class AutomovilVolador(Automovil):
  ruedas=6
  
#Agregar al constructor esta_volando=True
  def __init__(self,color,marca,aceleracion,esta_volando=True):
    super().__init__(color,marca,aceleracion)
    self.esta_volando=esta_volando
  #Agregar métodos vuela y aterriza(esta_volando)
  def vuela(self):
    self.esta_volando=True
  def aterriza(self):
    self.esta_volando=False
