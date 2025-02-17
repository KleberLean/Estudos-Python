class curso:
    def _init_ (self,nome):
        self.nome = nome
       
    def _str_(self):
        return f"{self.nome})"

class estudante:
    def _init_(self,aluno, disciplina):
        self.aluno = aluno
        self.disciplina = disciplina
   
    def detalhes(self):
        return f"'{self.aluno}' faz curso de {self.disciplina}"

curso1 = curso ("Desv. de sistemas")

estudante1 = estudante("Alex", curso1)

print(estudante1.detalhes())