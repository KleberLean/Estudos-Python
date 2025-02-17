import re

class Pessoa:
    def __init__(self, nome, idade, email):
        self.__nome = None
        self.__idade = None
        self.__email = None
        
        # Usando os setters para validar os valores durante a inicialização
        self.nome = nome
        self.idade = idade
        self.email = email

    # Get nome
    @property
    def nome(self):
        return self.__nome

    # Set nome
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self.__nome = novo_nome.strip()
        else:
            raise ValueError("O nome deve ser uma string não vazia.")

    # Get idade
    @property
    def idade(self):
        return self.__idade

    # Set idade
    @idade.setter
    def idade(self, nova_idade):
        if isinstance(nova_idade, int) and nova_idade > 0:
            self.__idade = nova_idade
        else:
            raise ValueError("A idade deve ser um número inteiro positivo.")

    # Get email
    @property
    def email(self):
        return self.__email

    # Set email
    @email.setter
    def email(self, novo_email):
        if self.__validar_email(novo_email):
            self.__email = novo_email
        else:
            raise ValueError("O email fornecido é inválido.")

    # Método privado para validar email
    def __validar_email(self, email):
        # Regex simples para validação de email
        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(padrao, email) is not None

# Exemplo de uso
try:
    pessoa = Pessoa("Maria Silva", 30, "maria.silva@gmail.com")
    print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Email: {pessoa.email}")

    pessoa.nome = "João Santos"
    pessoa.idade = 25
    pessoa.email = "joao.santos@example.com"
    print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Email: {pessoa.email}")
except ValueError as e:
    print(e)
