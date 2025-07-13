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

class AppGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Pagamento - UM Sushi")

        tk.Label(master, text="Selecione uma opção:", font=("Arial", 14)).pack(pady=10)

        botoes = [
            ("Cadastrar Cliente", cadastrar_cliente),
            ("Cadastrar Região", cadastrar_regiao),
            ("Gerar Pedido Simulado", gerar_pedido_mock),
            ("Cadastrar Pedido Real", cadastrar_pedido),
            ("Pagamento via PIX", realizar_pagamento_pix),
            ("Pagamento via Cartão de Crédito", realizar_pagamento_credito),
            ("Pagamento via Cartão de Débito", realizar_pagamento_debito),
            ("Gerar Relatório PDF", gerar_relatorio_pdf),
        ]

        for texto, comando in botoes:
            tk.Button(master, text=texto, width=30, command=self.executar(comando)).pack(pady=5)

        tk.Button(master, text="Sair", width=30, command=master.quit).pack(pady=10)

    def executar(self, func):
        def wrapper():
            try:
                func()
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        return wrapper

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500")
    app = AppGUI(root)
    root.mainloop()