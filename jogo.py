# Jogo da adivinhação
numero = 22
chute = int(input("Entre com um número:\n"))

if chute == numero:
    print("Você acertou!")
elif chute > numero:
    print("Você errou! Chute maior que o número")
else:
    print("Você errou! Chute menor que o número")