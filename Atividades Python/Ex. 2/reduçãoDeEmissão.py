# Entrada dos dados
distancia_km = float(input('Qual a distancia Percorrida em km? '))
emissao_carro_g_km = float(input('Emissão de CO2 do carro em g/km. '))
emissao_transporte_publico_g_km = float(input('Emissão de CO2 do transporte público em g/km. '))

# Cálculo das emissões do carro
emissao_carro_total_g = distancia_km * emissao_carro_g_km
# Cálculo das emissões do transporte público
emissao_transporte_publico_total_g = distancia_km * emissao_transporte_publico_g_km
# Cálculo da redução de emissão
reducao_g = emissao_carro_total_g - emissao_transporte_publico_total_g

#saida de dados
print('Redução de emissão de CO2: {} g'.format(reducao_g))