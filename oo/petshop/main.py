from Cachorro import Cachorro
from Gato import Gato

#cadastrar os pets
pet1 = Cachorro("Rex", 4, "Puddle")
pet2 = Cachorro("Lulu", 2, "Golden")
pet3 = Cachorro("Zeus", 2, "Pitbull")
pet4 = Cachorro("Totó", 2, "Caramelo")
pet5 = Gato("Garfield", 4, "Orange cat")
pet6 = Gato("Charlote", 3, "Siamês")
pet7 = Gato("Félix", 2, "Persa")
pet8 = Gato("Nerfário", 3, "Caramelo")

#lista de pets
pets = [
    pet1,
    pet2,
    pet3,
    pet4,
    pet5,
    pet6,
    pet7,
    pet8
]

#gerar relatório dos pets cadastrados
for pet in pets:
    print(
        f'\n--------Dados do Pet--------\n'
        f'Nome:{pet.nome}\n'
        f'Idade:{pet.idade}\n'
        f'Raça:{pet.raca}'
    )

#remove pet da lista

pets.pop(0)

#adicionar um novo pet
novopet = Gato("Novo pet", 4, "Qualquer")
pets.append(novopet)

for pet in pets:
    print(
        f'\n--------Dados do Pet--------\n'
        f'Nome:{pet.nome}\n'
        f'Idade:{pet.idade}\n'
        f'Raça:{pet.raca}'
    )
