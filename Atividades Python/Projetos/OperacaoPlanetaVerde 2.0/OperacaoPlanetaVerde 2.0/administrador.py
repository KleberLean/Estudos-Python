class Administrador:
    def __init__(self, sistema_coleta):
        self.sistema_coleta = sistema_coleta
    

    def adicionar_informacoes_cep(self):
        cep = input("Digite o CEP (apenas números): ")
        dias_coleta = {}

        for dia in ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]:
            print(f"\nConfigurando coleta para {dia}")
            coletar_dia = input(f"Haverá coleta na {dia}? (S/N): ").strip().upper()

            if coletar_dia == "S":
                horario_coleta = input(f"Horário da coleta em {dia} (ex: 08:00): ")
                tipos_residuos_dia = []
                print(f"Selecione os tipos de resíduos para {dia}:")
                for residuo in ["Orgânico", "Metálico", "Papel", "Vidro", "Plástico"]:
                    resposta = input(f"Coletar {residuo} em {dia}? (S/N): ").strip().upper()
                    if resposta == "S":
                        tipos_residuos_dia.append(residuo)
                dias_coleta[dia] = {
                    "horario_coleta": horario_coleta,
                    "tipos_residuos": tipos_residuos_dia,
                }

        num_casas = int(input("\nNúmero de casas neste CEP: "))

        self.sistema_coleta.dados[cep] = {
            "dias_coleta": dias_coleta,
            "num_casas": num_casas,
        }
        self.sistema_coleta.salvar_dados()
        print(f"Informações para o CEP {cep} salvas com sucesso!")

    def menu_administrador(self):
        while True:
            print("\n--- MENU ADMINISTRADOR ---")
            print("1. Adicionar informações de CEP")
            print("2. Listar CEPs cadastrados")
            print("3. Sair")
            escolha = input("Escolha uma opção: ")
            if escolha == "1":
                self.adicionar_informacoes_cep()
            elif escolha == "2":
                self.sistema_coleta.listar_ceps_disponiveis()
            elif escolha == "3":
                break
            else:
                print("Opção inválida. Tente novamente.")

    @classmethod
    def verificar_admin(cls):
        while True:
            admin_id = input("Digite seu ID de administrador: ")
            if admin_id in ["admin123", "admin456", "admin789"]:
                print("Acesso concedido!")
                return True
            else:
                print("ID de administrador inválido. Tente novamente.")