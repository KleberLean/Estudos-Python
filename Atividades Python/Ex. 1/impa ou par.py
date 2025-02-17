def verificar_par_impar(numero):
    if numero % 2 == 0:
        return 'O numero é par'
    else:
        return 'O numero é impar'
# exemplo de uso
numero = int(input('Digite o numero desejado: '))
resultado = verificar_par_impar(numero)
print(resultado)