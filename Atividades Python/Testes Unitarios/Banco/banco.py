class Banco:
    def __init__(self):
        self.dados = {}

    def adicionar_cliente(self, nome, saldo):
        self.dados[nome] = saldo

    def obter_saldo(self, nome):
        return self.dados.get(nome, 0)