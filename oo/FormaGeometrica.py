class FormaGeometrica:
    def __init__(self, nome, area, numeroLados, volume):
        self._nome = nome
        self._area = area
        self._numeroLados = numeroLados
        self._volume = volume
    
    # Métodos de acesso (getters e setters)

    # getter nome
    @property
    def nome(self):
        return self._nome

    @property
    def numeroLados(self):
        return self._numeroLados
    
    # setter nome
    @nome.setter
    def nome(self, nomeNovo):
        self._nome = nomeNovo

    
    def calcular_area(self):
        pass

class Triangulo(FormaGeometrica):
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
        super().__init__("Triangulo", 0, 3, 0)
    
    def calcular_area(self):
        return (self.base * self.altura)/2

trianguloA = Triangulo(4.5, 8.5)

print(trianguloA.calcular_area())
print(trianguloA.nome)
print(trianguloA.numeroLados)


