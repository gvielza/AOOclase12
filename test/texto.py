
class Texto:
    def __init__(self, texto):
        self.texto = texto

    def tiene_mayusculas_y_minusculas(self):
      return self.texto != self.texto.lower() and self.texto != self.texto.upper()