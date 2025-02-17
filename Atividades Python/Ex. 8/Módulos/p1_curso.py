class Cursos:
    def __init__(self,Curso):
        self.Curso = Curso
    def __str__(self):
        return f'Cursos:{self.Curso}'
cu = Cursos ('Desenvolvimento de sistema')
print(cu)
