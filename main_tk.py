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
from views.pagamento_view import PagamentoView

class AppGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Pagamento - UM Sushi")

        tk.Label(master, text="Selecione uma opção:", font=("Arial", 14)).pack(pady=10)

        botoes = [
            ("Cadastrar Cliente", self.executar(cadastrar_cliente)),
            ("Cadastrar Região", self.executar(cadastrar_regiao)),
            ("Gerar Pedido Simulado", self.executar(gerar_pedido_mock)),
            ("Cadastrar Pedido Real", self.executar(cadastrar_pedido)),
            ("Pagamento via PIX", self.executar(realizar_pagamento_pix)),
            ("Pagamento via Cartão de Crédito", self.executar(realizar_pagamento_credito)),
            ("Pagamento via Cartão de Débito", self.executar(realizar_pagamento_debito)),
            ("Gerar Relatório PDF", self.executar(gerar_relatorio_pdf)),
            ("Pagamento (GUI)", self.executar(lambda: PagamentoView(master)))
        ]

        for texto, comando in botoes:
            tk.Button(master, text=texto, width=30, command=comando).pack(pady=5)

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
    root.geometry("400x600")
    app = AppGUI(root)
    root.mainloop()