#Crear clase Vehiculo con año(protegido) y modelo(privado)
class Vehiculo:
  def __ini__(self,anno,modelo):
    self._anno=anno
    self.__modelo=modelo
  #6-Realizar get y set
#7-Mostrar por consola año y modelo, modificarlos y mostrar nuevamente 8-Subir cambios al git y versión v1 (clase 8)
  def get_anno(self):
    return self._anno
  def get_modelo(self):
    return self.__modelo
  def set_anno(self,nuevo_anno):
    self._anno=nuevo_anno
  def set_modelo(self,nuevo_modelo):
    self.__modelo=nuevo_modelo
    