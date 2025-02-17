n1 = float(input('Primeira média: '))
n2 = float(input('Segunda média: '))
n3 = float(input('Terceira média: '))
#soma
s = (n1 + n2 + n3) / 3

if s >= 6:
    print(f'{s:.3} Você foi aprovado!!!')
else:
    print(f'{s:.3} Você foi reprovado!!!')
