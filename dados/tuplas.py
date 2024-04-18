#estruras imutáveis e ordenadas(indexada)
semana = (
    "Domingo", 
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado" 
)

print(semana)#escreve todos os itens
print(semana[-1])#retorna o último item da tupla
for dia in semana:
    print(dia)

print(semana.index("Sábado"))#6

#manipular elementos(NÃO Dá!)

aluna = ("Ana Sara", 16, "Carnaubal", "29/05/2023")
print("Aniversário:", aluna[-1])
