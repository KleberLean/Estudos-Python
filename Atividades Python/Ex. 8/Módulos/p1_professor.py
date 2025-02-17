class Professor:
    def __init__(self,Professores):
        self.Professores = Professores
    def __str__(self):
        return f'Professores:{self.Professores}'
prof = Professor ('Maria Paula,Ramiro Jr')
print(prof)