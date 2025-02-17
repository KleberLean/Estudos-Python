# Dados de informação
dispositivo = input('Qual é o dispositivo eletronico: ')
watts = float(input('Qual a potência em watts? '))
horas = float(input('Qual a frequencia de uso do dispositivo em horas? '))
dias = int(input('Quantos dias do mês o dispositivo e usado? '))

#calculos

divisao = (watts * horas * dias)/1000

print('A economia de energia em Kwh por ano é: {:.2f} Kwh'.format(divisao))