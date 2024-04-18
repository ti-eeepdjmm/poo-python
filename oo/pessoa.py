class Pessoa:
    def __init__(self, nome:str, idade:int, altura:float):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.cidade = "Carnaubal"

    def dizer_ola(self):
        print(f"Olá {self.nome}")
    
    def cozinhar(self, receita:str):
        print(f'{self.nome} está cozinhando {receita}.')
    
    def andar(self, distancia:float):
        print(f'Sai para andar {str(distancia).replace(".", ",")}m.')

    
   


    
