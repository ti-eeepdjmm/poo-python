class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def set_nome(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome
    
    def set_idade(self,idade):
        self.__idade = idade
    
    def get_idade(self):
        return self.__idade

pessoa1 = Pessoa("João", 25)

print(pessoa1.get_nome())# mostra o nome

pessoa1.set_nome("Jararaca")

print(pessoa1.get_nome())#mostra o novo nome

