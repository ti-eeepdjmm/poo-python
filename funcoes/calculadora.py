def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    return a / b


num1 = int(input("Entre com o 1º numero:\n"))
num2 = int(input("Entre com o 2º numero:\n"))
operacao = input("Entre com a operação(soma, mult, div, sub):\n")

if(operacao == "soma"):
    print("O resultado da {} é {}".format(operacao, somar(num1, num2)))
elif(operacao == "mult"):
        print("O resultado da {} é {}".format(operacao, multiplicar(num1, num2)))
elif(operacao == "div"):
        print("O resultado da {} é {}".format(operacao, dividir(num1, num2)))
else:
    print("O resultado da {} é {}".format(operacao, subtrair(num1, num2)))





