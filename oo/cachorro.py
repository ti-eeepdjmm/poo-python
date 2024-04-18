class Cachorro:
    def __init__(self, nome, raca, cor, altura, nascimento):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.altura = altura
        self.nascimento = nascimento
    
    def latir(self):
        print("Au au au!")
    
    def comer(self, comida):
        print(f'{self.nome} está comendo {comida}.')
    
    def andar(self, distancia):
        print(f'Sai para andar {str(distancia).replace(".", ",")}m.')
    
    def comando(self, comando):
        print(f'{self.nome} está {comando}...')
    
    def idade(self):
        pass


# Criando objetos do tipo Cachorro
cachorro1 = Cachorro("Lulu", "Vira-lata", "caramelo", 0.4, "09/02/2021")
cachorro1.latir()
cachorro1.comer("Ração")
