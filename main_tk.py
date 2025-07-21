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
from views.cadastro_cliente_view import CadastroClienteView
from views.cadastro_regiao_view import CadastroRegiaoView
from views.cadastro_pedido_view import CadastroPedidoView
from views.relatorio_pdf_view import RelatorioPDFView
from views.visualizar_pedidos_view import VisualizarPedidosView
from views.visualizar_pagamentos_view import VisualizarPagamentosView
from views.visualizar_clientes_view import VisualizarClientesView
from views.visualizar_regioes_view import VisualizarRegioesView


class AppGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Pagamento - UM Sushi")

        tk.Label(master, text="Selecione uma opção:", font=("Arial", 14)).pack(pady=10)

        botoes = [
            ("Cadastrar Cliente", lambda: CadastroClienteView(root)),
            ("Visualizar Clientes", lambda: VisualizarClientesView(root)),
            ("Cadastrar Região", lambda: CadastroRegiaoView(root)),
            ("Visualizar Regiões", lambda: VisualizarRegioesView(root)),
            ("Gerar Pedido Simulado", gerar_pedido_mock),
            ("Cadastrar Pedido Real", cadastrar_pedido),
            ("Visualizar Pedidos", lambda: VisualizarPedidosView(root)),
            ("Pagamento via PIX", realizar_pagamento_pix),
            ("Pagamento via Cartão de Crédito", realizar_pagamento_credito),
            ("Pagamento via Cartão de Débito", realizar_pagamento_debito),
            ("Visualizar Pagamentos", lambda: VisualizarPagamentosView(root)),
            ("Gerar Relatório PDF", lambda: RelatorioPDFView(root)),
            ("Pagamento via Interface Gráfica", lambda: CadastroPedidoView(root)),
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

    def abrir_pagamento_view(self):
        top = tk.Toplevel(self.master)
        PagamentoView(top)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x550")
    app = AppGUI(root)
    root.mainloop()