#Tipos de dados no python

numeroInteiro = 1000
numeroReal = 15.4
texto = "Algum texto"
verdadeOuFalsidade = True

# print(numeroInteiro)

# if(numeroInteiro > 100):
#     print("número maior que 100")
# else:
#     print("número menor que 100")

# print("número maior que 100") if(numeroInteiro > 100) else print("número menor que 100")

# loops (repetições)
# parada = 1
# while(parada < 100):
#     print(parada)
#     parada = parada + 1

nomes = ["Rick", "Saulin", "Daniel", "Lucas"] #lista (list)
nomes.append("Rosa")#adiciona valores no final da lista

for nome in nomes:
    print(nome)

nomes.pop()#remove ultimo valor da lista
nomes.reverse()#inverte a ordem dos elementos
nomes.sort()#ordena de forma alfabética

for nome in nomes:
    print(nome)