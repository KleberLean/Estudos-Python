class Som:
    def __init__(self):
        self.som = None

    def emitir_som(self, som):
        self.som = som
        print(f"O som emitido é: {self.som}")

class Desenho:
    def __init__(self):
        pass

class Figma(Desenho):
    def __init__(self):
        super().__init__()

class Circulo(Figma):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio

    def get_raio(self):
        return self.raio

    def set_raio(self, raio):
        self.raio = raio

class Galinha(Som, Desenho):
    def __init__(self):
        super().__init__()
        self.nascimento = "Não nasceu ainda"

    def nasce(self):
        self.nascimento = "Galinha nasceu!"
        print(self.nascimento)

    def emitir_som(self):
        super().emitir_som("cacarejar")

galinha = Galinha()
galinha.nasce()  
galinha.emitir_som()  


 