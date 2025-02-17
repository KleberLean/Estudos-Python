papel_usado_kg = float(input('Quantidade de papel usado em kg? '))
porcentagem_reciclada = float(input('Porcentagem de papel reciclado. '))
# saida dos dados
print('Quantidade de papel reciclado economizado em kg é {}'.format((papel_usado_kg*porcentagem_reciclada)/100))