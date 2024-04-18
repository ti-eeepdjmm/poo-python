# Listas são mutáveis e ordenadas
cursos = ["ADM", "INFOR", "AGRO", "EDIF"]
print(cursos)#escreve todos os itens
print(cursos[-1])#último item da lista

# escreve itens da lista com um loop
for curso in cursos:
    print(curso)

# funções de listas
print(len(cursos))#quantidade de itens

# adicionar itens
cursos.append("REDES")#adiciona no final
print(cursos)
cursos.insert(2, "FLOR")#adiciona em uma posição específica
print(cursos)
cursos.insert(100, "ENFERMAGEM")#insere no final
print(cursos)
cursos[-1] = "TURISMO"#insere no final da lista
print(cursos)

# removendo itens da lista
print(cursos.pop())#retorna e remove do final
print(cursos)
cursos.pop(0)#remove o primeiro item da lista
print(cursos)
cursos.remove("INFOR")#busca e remove o item 
print(cursos)

cursos2 = ["MEDICINA", "COMPUTAÇÃO", "LETRAS"]

cursos.extend(cursos2)#adiciona uma lista em outra
print(cursos)

