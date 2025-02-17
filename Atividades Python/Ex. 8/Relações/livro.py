class Autor:
    def _init_ (self,nome):
        self.nome = nome
       
    def _str_(self):
        return f"{self.nome})"


class livro:
    def _init_(self,titulo, autor):
        self.titulo = titulo
        self.autor = autor
   
    def detalhes(self):
        return f"'{self.titulo}' por {self.autor}"


autor1 = Autor ("Machado de Assis")


livro1 = livro1 = livro("Dom Casmurro", autor1)


print(livro1.detalhes()