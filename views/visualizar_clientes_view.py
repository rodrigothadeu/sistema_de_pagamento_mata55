import tkinter as tk
from tkinter import ttk, messagebox
from utils.arquivo import carregar_dados
from data.caminhos import CAMINHO_CLIENTES, CAMINHO_REGIOES

class VisualizarClientesView:
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Clientes Cadastrados")
        self.window.geometry("750x400")

        try:
            clientes = carregar_dados(CAMINHO_CLIENTES)
            regioes = {r["id"]: r["nome"] for r in carregar_dados(CAMINHO_REGIOES)}

            if not clientes:
                tk.Label(self.window, text="Nenhum cliente cadastrado.").pack(pady=20)
                return

            self.tree = ttk.Treeview(self.window, columns=("id", "nome", "cpf", "telefone", "regiao"), show="headings")
            self.tree.heading("id", text="ID")
            self.tree.heading("nome", text="Nome")
            self.tree.heading("cpf", text="CPF")
            self.tree.heading("telefone", text="Telefone")
            self.tree.heading("regiao", text="Região")

            for cliente in clientes:
                regiao_nome = regioes.get(cliente["regiao_id"], "Desconhecida")
                self.tree.insert("", "end", values=(
                    cliente["id"],
                    cliente["nome"],
                    cliente["cpf"],
                    cliente["telefone"],
                    regiao_nome
                ))

            self.tree.pack(expand=True, fill="both", padx=10, pady=10)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar clientes: {str(e)}")
