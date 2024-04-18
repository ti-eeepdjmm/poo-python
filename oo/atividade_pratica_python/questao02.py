class Veiculo:
    def __init__(self, velocidade):
        self.__velocidade = velocidade
    
    def set_velocidade(self, velocidade):
        self.__velocidade = velocidade

    def get_velocidade(self):
        return self.__velocidade
    
class Carro(Veiculo):
    def acelerar(self, quantidade):
        self.set_velocidade(self.get_velocidade() + quantidade) 

class Moto(Veiculo):
    def acelerar(self, quantidade):
        self.set_velocidade(self.get_velocidade() + quantidade)


carro1 = Carro(300)
moto1 = Moto(400)


print(carro1.get_velocidade())#300
carro1.acelerar(100)
print(carro1.get_velocidade())#400





    
