from controllers.sistema import (
    cadastrar_cliente,
    cadastrar_regiao,
    gerar_pedido_mock,
    cadastrar_pedido,
    realizar_pagamento_pix,
    realizar_pagamento_credito,
    realizar_pagamento_debito
)
from services.relatorio_pdf import gerar_relatorio_pdf

from views.interface_view import iniciar_interface_grafica

def menu():
    while True:
        print("\n====== Sistema de Pagamento UM Sushi ======")
        print("1 - Cadastrar cliente")
        print("2 - Cadastrar região")
        print("3 - Gerar pedido simulado")
        print("4 - Realizar pagamento via PIX")
        print("5 - Realizar pagamento via Cartão de Crédito")
        print("6 - Realizar pagamento via Cartão de Débito")
        print("7 - Gerar relatório em PDF")
        print("8 - Cadastrar pedido com itens reais")
        print("9 - Abrir interface gráfica")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cadastrar_regiao()
        elif opcao == "3":
            gerar_pedido_mock()
        elif opcao == "4":
            realizar_pagamento_pix()
        elif opcao == "5":
            realizar_pagamento_credito()
        elif opcao == "6":
            realizar_pagamento_debito()
        elif opcao == "7":
            gerar_relatorio_pdf()
        elif opcao == "8":
            cadastrar_pedido()
        elif opcao == "9":
            iniciar_interface_grafica()
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()