def main():
    quantidade_itens = int(input("Quantos horarios você deseja registrar? "))
    
    # Criar uma lista para armazenar os horários
    horarios = []
    
    # Coletar os horários
    for i in range(1, quantidade_itens + 1):
        horario = input(f"Digite o horário {i} (formato HH:MM): ")
        horarios.append(horario)
    
    # Perguntar a quantidade de gramas
    gramas = float(input("\nDigite a quantidade de gramas por dia:  "))
    
    # Calcular a divisão e mostrar o resultado
    divisao = gramas / quantidade_itens
    
    # Variáveis para controlar a quantidade de gramas consumidas
    gramas_restantes = gramas
    gramas_por_item = []

    # Loop para calcular a distribuição das gramas
    for i in range(quantidade_itens):
        if gramas_restantes <= divisao:
            # Se as gramas restantes são menores ou iguais ao valor dividido
            gramas_por_item.append(gramas_restantes)
            gramas_restantes = 0  # Todas as gramas foram consumidas
        elif gramas_restantes > divisao:
            # Se ainda há gramas a serem consumidas
            gramas_por_item.append(divisao)
            gramas_restantes -= divisao
        else:
            # Caso final se não houver mais gramas a distribuir
            gramas_por_item.append(gramas_restantes)
            gramas_restantes = 0
    
    # Exibir os resultados
    print("\nResumo:")
    for i in range(quantidade_itens):
        print(f"Alarme {i + 1} - Horário: {horarios[i]} | Quantidade de gramas: {gramas_por_item[i]:.2f} gramas")
    
    print(f"\nTotal de gramas divididas: {sum(gramas_por_item):.2f} gramas")

# Executando a função principal
if __name__ == "__main__":
    main()
