"""# 1º Mostrar o numero maior
x = int(input('Escolha um numero: '))
y = int(input('Escolha outro numero: '))

if x>y:
    print(f'o numero maior e: {x}')
else:
    print(f'o numero maior e: {y}')
# Fim.


# 2º Impar ou par
def verificar_par_impar(numero):
    if numero % 2 == 0:
        return 'O numero é par'
    else:
        return 'O numero é impar'
# exemplo de uso
numero = int(input('Digite o numero desejado: '))
resultado = verificar_par_impar(numero)
print(resultado)
# FIm.

# 3º Determinar o menor numero
a = int(input('Escolha o primeiro numero: '))
b = int(input('Escolha o segundo numero: '))
c = int(input('Escolha o terceiro numero: '))

if a<b and a<c: 
    print(f'O menor numero e: {a}')
elif b<a and b<c:
    print(f'O menor numero e: {b}')
else:
    print(f'O menor numero e: {c}')
# Fim

# 4º Identificaçao de idade
idade = int(input('Digite sua idade: ')) 

if idade > 17: 
    print(f'Sua idade é: {idade} Você é maior de idade!!!')
else:
    print(f'Sua idade é: {idade} Você é menor de idade')
# Fim.


# 5º Idade e nome 
nome = input('Qual é o seu nome? ')
idade = int(input('Qual sua idade? '))

print(f'Olá, {nome} você tem {idade} anos')
#fim


# 6º media do aluno
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print(f'A media do aluno é: {media :.1f}')
# Fim

# 7º Base e altura
base = float(input('Qual o tamanho da base: '))
altura = float(input('Qual a altura do seu triângulo: '))

area = (base * altura) /2

print (f'a area do seu triângulo é {area}')
# Fim.


# 8º Tabuada
print('Tabuada de Multiplicação')

a = int(input('Digite um numero: '))
for tabu in range(1,11):
    resultado = a * tabu
    print(f'{a} x {tabu} = {resultado}')
# Fim.


# 9º Salario
salario = float(input("Qual o seu salario: "))
resultado = salario * 0.10
valor_total = salario + resultado
print (f'O seu novo salário é {valor_total}')
# Fim."""

#10º
numero = int(input('Digite um numero: '))

if numero > 0:
    print('Seu numero e positivo')
elif numero == 0:
    print('Seu numero e neutro')
else :
    print ('seu numero e negativo')