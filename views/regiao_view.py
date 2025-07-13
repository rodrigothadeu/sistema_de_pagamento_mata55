import tkinter as tk
from tkinter import messagebox
from utils.arquivo import carregar_dados, salvar_dados
from data.caminhos import CAMINHO_REGIOES
import uuid

def abrir_tela_cadastro_regiao():
    janela = tk.Toplevel()
    janela.title("Cadastrar Região")

    # Nome da região
    tk.Label(janela, text="Nome da Região:").pack()
    nome_entry = tk.Entry(janela)
    nome_entry.pack()

    # Taxa de entrega
    tk.Label(janela, text="Taxa de Entrega (R$):").pack()
    taxa_entry = tk.Entry(janela)
    taxa_entry.pack()

    def salvar_regiao():
        nome = nome_entry.get()
        taxa = taxa_entry.get()

        if not nome or not taxa:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        try:
            taxa = float(taxa)
        except ValueError:
            messagebox.showwarning("Erro", "A taxa deve ser um número válido.")
            return

        nova_regiao = {
            "id": str(uuid.uuid4()),
            "nome": nome,
            "taxa_entrega": taxa
        }

        regioes = carregar_dados(CAMINHO_REGIOES)
        regioes.append(nova_regiao)
        salvar_dados(CAMINHO_REGIOES, regioes)

        messagebox.showinfo("Sucesso", "Região cadastrada com sucesso!")
        janela.destroy()

    tk.Button(janela, text="Cadastrar", command=salvar_regiao).pack(pady=10)