# Questão 1
soma_cumulativa = 0

while True:
    
    numero = float(input("Digite um número (ou 0 para sair): "))
    
    if numero == 0:
        break
    
    soma_cumulativa += numero
    
    print(f"Soma cumulativa até o momento: {soma_cumulativa}")

print("Programa encerrado.")

#Questão 2
# Valores iniciais
investimento_daphne = 100
investimento_cleo = 100

# Taxas de juros
juros_simples_daphne = 0.10
juros_compostos_cleo = 0.05

saldo_daphne = investimento_daphne
saldo_cleo = investimento_cleo

anos = 0

while saldo_cleo <= saldo_daphne:
    anos += 1
    # Juros simples para Daphne
    saldo_daphne += investimento_daphne * juros_simples_daphne
    # Juros compostos para Cleo
    saldo_cleo += saldo_cleo * juros_compostos_cleo

print(f"Anos necessários: {anos}")
print(f"Investimento de Daphne: ${saldo_daphne:.2f}")
print(f"Investimento de Cleo: ${saldo_cleo:.2f}")


#Questão 3

# Lista com os nomes dos meses
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Lista para armazenar as vendas de cada mês
vendas = []

# Loop para solicitar as vendas de cada mês
for mes in meses:
    while True:
        try:
            venda = int(input(f"Digite as vendas de {mes}: "))
            vendas.append(venda)
            break
        except ValueError:
            print("Por favor, insira um número válido.")

# Calcula a soma das vendas anuais
total_vendas = sum(vendas)

# Exibe o total anual de vendas
print(f"Vendas totais do ano: {total_vendas} livros")

# Questão 4

# Inicializa o contador de palavras
contador = 0

print("Digite palavras (para parar, digite a palavra 'done'): ")

# Loop para ler cada palavra
while True:
    palavra = input()  # Lê uma palavra do usuário
    
    # Verifica se a palavra digitada é "done"
    if palavra == "done":
        break  # Sai do loop se a palavra for "done"
    
    contador += 1

# Exibe o total de palavras digitadas
print(f"Você digitou um total de {contador} palavras.")


# Questão 5

# Solicita ao usuário o número de linhas
num_linhas = int(input("Digite o número de linhas: "))

# Loop para cada linha
for i in range(1, num_linhas + 1):
    pontos = num_linhas - i
    asteriscos = i

    print('.' * pontos + '*' * asteriscos)
