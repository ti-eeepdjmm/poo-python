from pessoa import Pessoa

pessoa = Pessoa("Lara", 16, 1.7)
# print(pessoa.nome)#atributo
# pessoa.cozinhar("Batata doce")#método
# pessoa.dizer_ola()#metodo

pessoa2 = Pessoa(nome="Lucas", idade=17, altura=1.73)

print(pessoa2.idade)
pessoa2.andar(distancia=10500.0)