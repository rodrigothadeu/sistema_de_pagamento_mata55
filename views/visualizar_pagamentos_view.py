import tkinter as tk
from tkinter import ttk, messagebox
from utils.arquivo import carregar_dados
from data.caminhos import CAMINHO_PAGAMENTOS, CAMINHO_CLIENTES

class VisualizarPagamentosView:
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Pagamentos Realizados")
        self.window.geometry("750x400")

        try:
            pagamentos = carregar_dados(CAMINHO_PAGAMENTOS)
            clientes = {c["id"]: c["nome"] for c in carregar_dados(CAMINHO_CLIENTES)}

            if not pagamentos:
                tk.Label(self.window, text="Nenhum pagamento registrado.").pack(pady=20)
                return

            self.tree = ttk.Treeview(self.window, columns=("id", "cliente", "valor", "forma", "data"), show="headings")
            self.tree.heading("id", text="ID")
            self.tree.heading("cliente", text="Cliente")
            self.tree.heading("valor", text="Valor (R$)")
            self.tree.heading("forma", text="Forma de Pagamento")
            self.tree.heading("data", text="Data")

            for p in pagamentos:
                cliente_nome = clientes.get(p["cliente_id"], "Desconhecido")
                self.tree.insert("", "end", values=(
                    p["id"],
                    cliente_nome,
                    f"{p['valor']:.2f}",
                    p["forma"],
                    p["data_pagamento"]
                ))

            self.tree.pack(expand=True, fill="both", padx=10, pady=10)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar pagamentos: {str(e)}")
