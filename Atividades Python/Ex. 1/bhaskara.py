import math
a = float(input('digite o valor de A: '))
b = float(input('digite o valor de B: '))
c = float(input('digite o valor de C: '))

delta = b**2 - 4*a*c

if delta < 0:
    resultado = 'Não existe raizes reais'
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    resultado = (x1, x2)

print('As raizes são:', resultado)