idade = int(input("Digite uma idade:\n"))

if idade >= 18 and idade < 65:
    print("Adulto")
elif idade < 18 and idade >= 12:
    print("Adolescente")
elif idade < 12:
    print("Criança")
elif idade >= 100:
    print("Ansiã")
else:
    print("Idosa")