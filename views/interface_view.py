import tkinter as tk
from tkinter import messagebox
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
from views.cliente_view import abrir_tela_cadastro_cliente
from views.regiao_view import abrir_tela_cadastro_regiao
from views.pedido_mock_view import abrir_tela_pedido_simulado
from views.pedido_view import abrir_tela_pedido_real
from views.pagamento_view import abrir_tela_pagamento


def iniciar_interface_grafica():
    root = tk.Tk()
    root.title("Sistema de Pagamento - UM Sushi")
    root.geometry("400x550")

    tk.Label(root, text="Selecione uma opção:", font=("Arial", 14)).pack(pady=10)

    botoes = [
        ("Cadastrar Cliente", abrir_tela_cadastro_cliente),
        ("Cadastrar Região", abrir_tela_cadastro_regiao),
        ("Gerar Pedido Simulado", abrir_tela_pedido_simulado),
        ("Cadastrar Pedido Real", abrir_tela_pedido_real),
        ("Pagamento via PIX", lambda: abrir_tela_pagamento("PIX")),
        ("Pagamento via Cartão de Crédito", lambda: abrir_tela_pagamento("Cartão de Crédito")),
        ("Pagamento via Cartão de Débito", lambda: abrir_tela_pagamento("Cartão de Débito")),
        ("Gerar Relatório PDF", gerar_relatorio_pdf),
        ("Sair", root.quit),
    ]

    for texto, comando in botoes:
        tk.Button(root, text=texto, width=35, command=lambda cmd=comando: executar(cmd)).pack(pady=5)

    root.mainloop()

def executar(func):
    try:
        func()
    except Exception as e:
        messagebox.showerror("Erro", str(e))
