import json
import os

ARQUIVO_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "coleta_dados.json")


class SistemaColeta:
    def __init__(self):
        self.dados = self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def salvar_dados(self):
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
            json.dump(self.dados, arquivo, ensure_ascii=False, indent=4)

    def consultar_informacoes_cep(self, cep):
        if cep in self.dados:
            info_cep = self.dados[cep]
            print("\n--- INFORMAÇÕES DE COLETA ---")
            print(f"CEP: {cep}")
            print(f"Número de casas: {info_cep['num_casas']}")
            print("\nProgramação de Coleta:")
            for dia, info_dia in info_cep["dias_coleta"].items():
                print(f"\n{dia}:")
                print(f"  Horário: {info_dia['horario_coleta']}")
                print("  Tipos de resíduos:")
                for residuo in info_dia["tipos_residuos"]:
                    print(f"  - {residuo}")
        else:
            print(f"Não há informações cadastradas para o CEP {cep}")

    def listar_ceps_disponiveis(self):
        if self.dados:
            print("\nCEPs disponíveis:")
            for cep in self.dados.keys():
                print(cep)
        else:
            print("Nenhum CEP cadastrado ainda.")
