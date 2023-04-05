class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
    
    def __str__(self):
        return f"Nome:{self.nome}\nIdade:{self.idade}\nCidade:{self.cidade}"

    

p1 = Pessoa("Mary", 15, "Rj")
p2 = Pessoa("John", 17, "Sp")

print(p1)
print(p2)


