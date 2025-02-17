class Pessoa:
    def __init__(self, nome, rg):
        self.nome = nome
        self.rg = rg

class Contribuinte:
    def __init__(self, indentificador_fsc):
        self.indentificador_fsc = indentificador_fsc

class Funcionario(Pessoa, Contribuinte):
    def __init__(self, nome, rg, matricula, indentificador_fsc):
        
        Pessoa.__init__(self, nome, rg)
        Contribuinte.__init__(self, indentificador_fsc)
        
        self.matricula = matricula

    def veri(self):
        print(f"Funcionario: {self.nome}, RG: {self.rg}, Matricula: {self.matricula}, Identificador FSC: {self.indentificador_fsc}")

class Empresa:
    def __init__(self, nome_empresa):
        self.nome_empresa = nome_empresa

funcionario1 = Funcionario(nome="João", rg="123456789", matricula="12345", indentificador_fsc="98765")

funcionario1.veri()

empresa1 = Empresa(nome_empresa="Tech Solutions")
print(f"Nome da empresa: {empresa1.nome_empresa}")

