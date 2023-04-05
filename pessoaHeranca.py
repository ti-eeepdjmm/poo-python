class Pessoa:
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    def __str__(self):
        return f"Nome:{self._nome}\nCPF:{self._cpf}"


class PessoaCearense(Pessoa):
    def __init__(self, nome, cpf, cabecudo=True):
        super().__init__(nome, cpf)
        self._cabecudo=cabecudo
    
    def __str__(self):
        texto = super().__str__()
        return texto + f"\nCabecudo:{self._cabecudo}"

# p1 = Pessoa("Rick", "34132342342")

# print(p1.mostraInfo())

p2 = PessoaCearense("Maria", "234234232")

print(p2)