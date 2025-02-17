class Estudante:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0.0  # Evita divisão por zero se a lista de notas estiver vazia.
        return sum(self.notas) / len(self.notas)

# Criando objetos da classe Estudante
estudante1 = Estudante("João", 20, [8.0, 7.5, 9.0, 6.0])
estudante2 = Estudante("Maria", 22, [9.5, 8.5, 10.0, 7.5])
estudante3 = Estudante("Carlos", 19, [5.5, 6.0, 7.0, 6.5])

# Exibindo as informações e a média de cada estudante
for estudante in [estudante1, estudante2, estudante3]:
    print(f"Estudante: {estudante.nome}")
    print(f"Idade: {estudante.idade}")
    print(f"Notas: {estudante.notas}")
    print(f"Média: {estudante.calcular_media():.2f}")
    print("-" * 20)