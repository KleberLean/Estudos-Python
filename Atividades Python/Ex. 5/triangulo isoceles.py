# Solicita três lados ao usuário
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

# Verifica a condição de existência de um triângulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Os valores podem formar um triângulo.")
else:
    print("Os valores não podem formar um triângulo.")
