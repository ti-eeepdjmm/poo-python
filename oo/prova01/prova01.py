class Corretor:
    def __init__(self, nome, comissao):
        self.__nome = nome
        self.__comissao = comissao

    def set_nome(self, nome):
        self.__nome = nome
    
    def set_comissao(self, comissao):
        self.__comissao = comissao
    
    def get_nome(self):
        return self.__nome

    def get_comissao(self):
        return self.__comissao


class CorretorVendas(Corretor):
    def calcular_salario(self, vendas):
        return 0.05 * vendas

class CorretorAlugueis(Corretor):
    def calcular_salario(self, alugueis):
        return 0.03 * alugueis

corretor1 = CorretorVendas(nome="Rick", comissao=0.05)
corretor2 = CorretorAlugueis(nome="Luri", comissao=0.03)

print(corretor1.calcular_salario(10000))
print(corretor2.calcular_salario(100000))