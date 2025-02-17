print("-" * 30)
print("Conta Bancária")
print("O que deseja realizar?")
print("1 - Saldo em conta\n2 - Depositar\n3 - Sacar")
ver1 = int(input())

class contaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Valor adicionado com sucesso, o saldo em conta é: {self._saldo}")

    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente!")
        else:
            self._saldo -= valor
            print(f"Valor retirado com sucesso, o saldo em conta é: {self._saldo}")

user = contaBancaria("Nome", 1500)

if ver1 == 3:
    quantia_do_saque = int(input("Digite o valor que deseja sacar: "))
    user.sacar(quantia_do_saque)

if ver1 == 2:
    quantia_deposito = int(input("Qual o valor que deseja depositar? "))
    user.depositar(quantia_deposito)

if ver1 == 1:
    print(user._saldo)
