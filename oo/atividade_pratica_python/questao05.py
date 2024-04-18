class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def set_nome(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome
    
    def set_salario(self, salario):
        self.__salario = salario
    
    def get_salario(self):
        return self.__salario
    
class Gerente(Funcionario):
    def calcular_bonus(self):
        return (self.get_salario() * 0.15)

class Vendedor(Funcionario):
    def calcular_bonus(self):
        return (self.get_salario() * 0.10)

gerente1 = Gerente("Manu", 100000)
vendedor1 = Vendedor("Artur", 15000)

print(gerente1.calcular_bonus())#15000
print(vendedor1.calcular_bonus())#1500
    
