import tkinter as tk
from tkinter import ttk, messagebox
from utils.arquivo import carregar_dados
from data.caminhos import CAMINHO_PEDIDOS, CAMINHO_CLIENTES

class VisualizarPedidosView:
    def __init__(self, master):
        self.master = tk.Toplevel(master)
        self.master.title("Pedidos Cadastrados")
        self.master.geometry("600x400")

        self.tree = ttk.Treeview(self.master, columns=("ID", "Cliente", "Total", "Itens"), show="headings")
        self.tree.heading("ID", text="ID do Pedido")
        self.tree.heading("Cliente", text="Cliente")
        self.tree.heading("Total", text="Valor Total")
        self.tree.heading("Itens", text="Itens")

        self.tree.column("ID", width=120)
        self.tree.column("Cliente", width=120)
        self.tree.column("Total", width=100)
        self.tree.column("Itens", width=240)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.carregar_pedidos()

    def carregar_pedidos(self):
        try:
            pedidos = carregar_dados(CAMINHO_PEDIDOS)
            clientes = carregar_dados(CAMINHO_CLIENTES)

            clientes_dict = {cliente["id"]: cliente["nome"] for cliente in clientes}

            for pedido in pedidos:
                cliente_nome = clientes_dict.get(pedido["cliente_id"], "Desconhecido")
                total = f'R$ {pedido.get("total", 0):.2f}'

                itens = pedido.get("itens", [])
                lista_itens = []
                for item in itens:
                    if isinstance(item, dict):
                        lista_itens.append(f'{item.get("nome", "")} ({item.get("preco", 0):.2f})')
                    else:
                        lista_itens.append(str(item))

                itens_formatados = ", ".join(lista_itens)

                self.tree.insert("", tk.END, values=(pedido["id"], cliente_nome, total, itens_formatados))

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar pedidos: {e}")
