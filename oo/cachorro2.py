class Cachorro:
    def __init__(self, nome, raca, peso, dataNascimento):
        self.nome = nome
        self.raca = raca
        self.peso = str(peso) + "Kg"
        self.dataNascimento =dataNascimento

    def latir(self):
        print("Au au au!")
    
    def comer(self, comida):
        print(f"{self.nome} está comendo {comida}")
    
    def caminhar(self, distancia):
        print(f"{self.nome} caminhou {distancia}m")
    
    def idade(self):
        dataPartes = str(self.dataNascimento).split("/")
        anoData = int(dataPartes[2])
        idadeCachorro = 2023-anoData
        if(idadeCachorro > 14):
            print(f"{self.nome} morreu!")
        else:
            print(f"A idade do {self.nome} é {idadeCachorro} anos.")


        

# Criar objetos
cachorro = Cachorro("Rick", "Pitbull", 20.5, "20/02/200vb 1")

print(cachorro.nome)#Rick
print(cachorro.raca)#Pitbull
cachorro.idade()#escreve a idade