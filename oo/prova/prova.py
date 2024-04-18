class FormaGeometrica:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        pass

class Triangulo(FormaGeometrica):
    def calcular_area(self):
        return (self.altura * self.base) / 2
    
class Retangulo(FormaGeometrica):
    def calcular_area(self):
        return (self.altura * self.base)
    
    
retangulo = Retangulo(3, 4)
print(retangulo.calcular_area())

triangulo = Triangulo(3, 4)
print(triangulo.calcular_area())

print(type(triangulo))