class banco:
    def __init__(self, saque, deposito, saldo):
        self.saque = saque
        self.deposito = deposito
        self.saldo = saldo

class contaCorente (banco):
    def __init_subclass__(self, saque, deposito, saldo):
        self.saque = saque
        self.deposito = deposito
        self.saldo = saldo

class poupança (banco):
    def __init_subclass__(self, saque, deposito, saldo):
        if self.saldo < 0 :
            print(f'Erro em saldo!')
        elif self.saldo > 0 :
            render = self.saldo * 0.95
            print(f"Saldo após rendimento: {render}")
        if self.saque > self.saldo:
            print("Erro: Saque maior que saldo!")
        else:
            retirada = self.saque - 2
            print(f"Novo saldo após retirada: {self.saldo}")    

user1 = poupança (saque=1400, deposito=2000, saldo=1500) 


