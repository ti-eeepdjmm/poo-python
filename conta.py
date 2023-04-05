class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.__saldo = saldo
    
    def __str__(self):
        return f"Numero:{self.numero}\nTitular:{self.titular}\nsaldo:R${self.__saldo}"
    
    def depositar(self, valor):
        self.__saldo += valor
        print(f"Deposito de R${valor} foi feito na conta {self.numero}...")
    
    def sacar(self, valor):
        self.__saldo -= valor
        print(f"Saque de R${valor} foi feito na conta {self.numero}...")
    
    def transferir(self, valor, contaDestino):
        self.sacar(valor)
        contaDestino.depositar(valor)




c1 = Conta(3456, "Rick", 1000.00)
c2 = Conta(6745, "Lara", 2000.00)


print(c1)
print(c2)
c2.transferir(1000, c1)
print(c1)
print(c2)  


