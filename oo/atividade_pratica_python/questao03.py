class Forma:
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura
    
    def calcular_area(self):
        return self.__base * self.__altura
    
class Circulo(Forma):
    def __init__(self, raio):
        self.__raio = raio

    def calcular_area(self):
        PI = 3.14
        return PI * (self.__raio ** 2)

#testando
circulo1 = Circulo(10)
retangulo1 = Retangulo(3, 5)

print(circulo1.calcular_area())
print(retangulo1.calcular_area())
    