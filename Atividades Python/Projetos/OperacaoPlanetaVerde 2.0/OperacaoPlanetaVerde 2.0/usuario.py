from ajudas import (
    ajuda_manusear_vidro,
    ajuda_lixo_eletronico,
    ajuda_plasticos_reciclaveis,
    ajuda_comida_lixo,
    ajuda_remedio_vencidos,
    ajuda_papeis_reciclavel,
)

class Usuario:
    def __init__(self, sistema_coleta):
        self.sistema_coleta = sistema_coleta

    def perguntas_frequentes(self):
        while True:
            print("\n--- PERGUNTAS OU DÚVIDAS FREQUENTES ---")
            print("1. Como manusear o lixo de vidro?")
            print("2. Onde jogar lixo eletrônico?")
            print("3. Todos os plásticos são recicláveis?")
            print("4. Posso jogar restos de comida no lixo comum?")
            print("5. O que fazer com remédios vencidos?")
            print("6. Papéis molhados ou engordurados podem ser reciclados?")
            print("7. Sair")
            escolha = input("Escolha uma opção: ")
            if escolha == "1":
                print(ajuda_manusear_vidro)
            elif escolha == "2":
                print(ajuda_lixo_eletronico)
            elif escolha == "3":
                print(ajuda_plasticos_reciclaveis)
            elif escolha == "4":
                print(ajuda_comida_lixo)
            elif escolha == "5":
                print(ajuda_remedio_vencidos)
            elif escolha == "6":
                print(ajuda_papeis_reciclavel)
            elif escolha == "7":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def menu_cliente(self):
        while True:
            print("\n--- CONSULTA DE COLETA DE RESÍDUOS ---")
            print("1. Consultar informações por CEP")
            print("2. Listar CEPs disponíveis")
            print("3. Perguntas frequentes")
            print("4. Sair")
            escolha = input("Escolha uma opção: ")
            if escolha == "1":
                cep = input("Digite seu CEP (apenas números): ")
                self.sistema_coleta.consultar_informacoes_cep(cep)
            elif escolha == "2":
                self.sistema_coleta.listar_ceps_disponiveis()
            elif escolha == "3":
                self.perguntas_frequentes()
            elif escolha == "4":
                break
            else:
                print("Opção inválida. Tente novamente.")
