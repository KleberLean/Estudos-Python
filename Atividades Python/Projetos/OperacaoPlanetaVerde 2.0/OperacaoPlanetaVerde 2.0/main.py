from sistema_coleta import SistemaColeta
from administrador import Administrador
from usuario import Usuario

if __name__ == "__main__":
    sistema = SistemaColeta()
    print("Escolha o modo: (1) Administrador, (2) Cliente")
    modo = input("Digite sua escolha: ")
    if modo == "1":
        admin = Administrador(sistema)
        admin.verificar_admin()
        admin.menu_administrador()
    elif modo == "2":
        cliente = Usuario(sistema)
        cliente.menu_cliente()
    else:
        print("Modo inválido.")
