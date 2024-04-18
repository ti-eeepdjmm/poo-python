class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_preco(self, salario):
        self.__preco = salario

    def get_preco(self):
        return self.__preco
    
class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.__autor = autor

    def detalhes(self):
        return f'Nome: {self.get_nome()} Preço: {self.get_preco()} Autor:{self.__autor}'
    

class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.__voltagem = voltagem

    def detalhes(self):
        return f'Nome: {self.get_nome()} Preço: {self.get_preco()} Voltagem: {self.__voltagem}'
    
livro1 = Livro("Bom livro", 15.6, "Eu mesmo")

print(livro1.detalhes())