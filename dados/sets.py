"""
    - Estruturas multáveis
    - Não ordenadas
    - Não permitem valores duplicados
"""
cores = {"blue", "red", "green", "blue", "yellow"}
print(cores)
print(cores)

for cor in cores:
    print(cor)

#inserindo itens
cores.add("purple")
print(cores)

#removendo itens do conjunto
print(cores.pop())#remove um item qualquer

