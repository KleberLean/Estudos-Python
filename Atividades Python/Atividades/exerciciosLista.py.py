'''lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

# Questao 2
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.append(11)
print(lista)

# Questão 3
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista[9]
print(lista)

# Questão 4
lista = [1, 2, 3, 4, 5, 6, 8, 9, 10]
lista.insert(2, 7)
print(lista)

# Questão 5
nomes = ['joao', 'kleber', 'vanessa', 'marcia', 'leandro']
nomes.sort()
print(nomes)

# Questão 6 
numeros = [1, 2, 3, 4, 5, 6]
fruta = ['maça', 'laranja', 'abacaxi']
resultado = numeros + fruta
print(resultado)

# Questão 7
numeros = [1, 2, 3, 4, 5, 6, 7]
resultado = sum(numeros) / 7
print(resultado)

# Questão 8
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(numeros))
print(max(numeros))

# Questão 9
frutas = ['maça', 'banana', 'laranja', 'uva', 'maça', 'abacaxi', 'maça']
count = frutas.count('maça')
print(count)'''

# Questão 10
lista = [1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 3, 7, 8, 9, 2]
sem_repeticao = sorted(set(lista))
print (sem_repeticao)