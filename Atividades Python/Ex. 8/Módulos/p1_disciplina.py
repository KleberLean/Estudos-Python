class Disciplina:
    def __init__(self,Disciplina):
        self.Disciplina = Disciplina
    def __str__(self):
        return f'diciplina: {self.Disciplina}' 
       
dic = Disciplina ('gestao de projetos')
print(dic)