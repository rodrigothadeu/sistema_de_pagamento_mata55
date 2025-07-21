import tkinter as tk
from tkinter import ttk, messagebox
from utils.arquivo import carregar_dados
from data.caminhos import CAMINHO_REGIOES

class VisualizarRegioesView:
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Regiões Cadastradas")
        self.window.geometry("600x300")

        try:
            regioes = carregar_dados(CAMINHO_REGIOES)

            if not regioes:
                tk.Label(self.window, text="Nenhuma região cadastrada.").pack(pady=20)
                return

            self.tree = ttk.Treeview(self.window, columns=("id", "nome", "taxa"), show="headings")
            self.tree.heading("id", text="ID")
            self.tree.heading("nome", text="Nome da Região")
            self.tree.heading("taxa", text="Taxa de Entrega (R$)")

            for regiao in regioes:
                self.tree.insert("", "end", values=(
                    regiao["id"],
                    regiao["nome"],
                    f"R$ {regiao['taxa_entrega']:.2f}"
                ))

            self.tree.pack(expand=True, fill="both", padx=10, pady=10)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar regiões: {str(e)}")
