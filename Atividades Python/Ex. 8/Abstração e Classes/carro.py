class Carro:
    def __init__(self, modelo, ano):
        self.__modelo = modelo  # Pv
        self.__ano = ano        # Pv

    # Get modelo
    @property
    def modelo(self):
        return self.__modelo

    # Set modelo
    @modelo.setter
    def modelo(self, novo_modelo):
        if isinstance(novo_modelo, str) and novo_modelo.strip():
            self.__modelo = novo_modelo
        else:
            raise ValueError("O modelo deve ser uma string válida.")

    # Get ano
    @property
    def ano(self):
        return self.__ano

    # Set ano
    @ano.setter
    def ano(self, novo_ano):
        if isinstance(novo_ano, int) and novo_ano > 1885:  
            self.__ano = novo_ano
        else:
            raise ValueError("O ano deve ser um número inteiro maior que 1885.")

# Exemplo de uso
try:
    carro = Carro("Fiat Uno", 2005)
    print(f"Modelo: {carro.modelo}, Ano: {carro.ano}")

    carro.modelo = "Ford Ka"
    carro.ano = 2015
    print(f"Modelo: {carro.modelo}, Ano: {carro.ano}")
except ValueError as e:
    print(e)
