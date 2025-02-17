peso = float(input('qual o seu peso? '))
altura = float(input('qual a sua altura? '))

imc = peso/(altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print ("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")