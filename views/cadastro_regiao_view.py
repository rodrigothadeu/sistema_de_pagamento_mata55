import tkinter as tk
from tkinter import messagebox
from uuid import uuid4
from utils.arquivo import carregar_dados, salvar_dados
from data.caminhos import CAMINHO_REGIOES

class CadastroRegiaoView:
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Cadastrar Região")
        self.window.geometry("400x220")

        tk.Label(self.window, text="Nome da Região:").pack(pady=5)
        self.entry_nome = tk.Entry(self.window, width=40)
        self.entry_nome.pack()

        tk.Label(self.window, text="Taxa de Entrega (R$):").pack(pady=5)
        self.entry_taxa = tk.Entry(self.window, width=40)
        self.entry_taxa.pack()

        tk.Button(self.window, text="Cadastrar", command=self.cadastrar_regiao).pack(pady=15)

    def cadastrar_regiao(self):
        try:
            nome = self.entry_nome.get().strip()
            taxa = self.entry_taxa.get().strip()

            if not nome or not taxa:
                messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
                return

            taxa = float(taxa.replace(",", "."))

            nova_regiao = {
                "id": str(uuid4()),
                "nome": nome,
                "taxa_entrega": taxa
            }

            regioes = carregar_dados(CAMINHO_REGIOES)
            regioes.append(nova_regiao)
            salvar_dados(CAMINHO_REGIOES, regioes)

            messagebox.showinfo("Sucesso", "Região cadastrada com sucesso!")
            self.window.destroy()

        except ValueError:
            messagebox.showerror("Erro", "Insira um valor numérico válido para a taxa.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar região: {e}")
