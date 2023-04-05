class Televisao:
    def __init__(self, marca, modelo, ligada):
        self.marca = marca
        self.modelo = modelo
        self.ligada = ligada


# Criando objeto do tipo Televisão
tv = Televisao("Samsung", "4k 60polegadas", False)
tv2 = Televisao("LG", "HDTV 50polegadas", True)

if(tv2.ligada):
    print("A TV está ligada")
else:
    print("A TV está desligada")

