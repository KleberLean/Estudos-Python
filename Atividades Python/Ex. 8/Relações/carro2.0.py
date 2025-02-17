class carro:
    def _init_ (self,nome):
        self.nome = nome
       
    def _str_(self):
        return f"{self.nome})"


class motor:
    def _init_(self,potencia, carro):
        self.potencia = potencia
        self.carro = carro
   
    def detalhes(self):
        return f"'{self.potencia}' do carro {self.carro}"


carro1 = carro ("Honda Civic")


potencia1 = motor("Motor 2,0", carro1)


print(potencia1.detalhes())