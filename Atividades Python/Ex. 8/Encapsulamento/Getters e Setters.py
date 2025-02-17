class Livro:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = None
        self.__autor = None
        self.__paginas = None

        # Validações iniciais 
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    #Get título
    @property
    def titulo(self):
        return self.__titulo

    #Set título
    @titulo.setter
    def titulo(self, novo_titulo):
        if isinstance(novo_titulo, str) and novo_titulo.strip():
            self.__titulo = novo_titulo.strip()
        else:
            raise ValueError("O título deve ser uma string não vazia.")

    #Get autor
    @property
    def autor(self):
        return self.__autor

    # Setter para autor
    @autor.setter
    def autor(self, novo_autor):
        if isinstance(novo_autor, str) and novo_autor.strip():
            self.__autor = novo_autor.strip()
        else:
            raise ValueError("O autor deve ser uma string não vazia.")

    #Get páginas
    @property
    def paginas(self):
        return self.__paginas

    #Set páginas
    @paginas.setter
    def paginas(self, novas_paginas):
        if isinstance(novas_paginas, int) and novas_paginas >= 0:
            self.__paginas = novas_paginas
        else:
            raise ValueError("O número de páginas deve ser um inteiro não negativo.")

#Exemplo
try:
    livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1178)
    print(f"Título: {livro.titulo}, Autor: {livro.autor}, Páginas: {livro.paginas}")

    livro.titulo = "O Hobbit"
    livro.autor = "J.R.R. Tolkien"
    livro.paginas = 310
    print(f"Título: {livro.titulo}, Autor: {livro.autor}, Páginas: {livro.paginas}")

    # Teste com valor inválido
    livro.paginas = -50  # Isso levantará uma exceção
except ValueError as e:
    print(e)
