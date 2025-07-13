import tkinter as tk
from tkinter import messagebox
from utils.arquivo import carregar_dados, salvar_dados
from data.caminhos import CAMINHO_CLIENTES, CAMINHO_REGIOES
import uuid

def abrir_tela_cadastro_cliente():
    janela = tk.Toplevel()
    janela.title("Cadastrar Cliente")

    tk.Label(janela, text="Nome:").pack()
    nome_entry = tk.Entry(janela)
    nome_entry.pack()

    tk.Label(janela, text="CPF:").pack()
    cpf_entry = tk.Entry(janela)
    cpf_entry.pack()

    tk.Label(janela, text="Telefone:").pack()
    telefone_entry = tk.Entry(janela)
    telefone_entry.pack()

    tk.Label(janela, text="Região:").pack()
    regioes = carregar_dados(CAMINHO_REGIOES)
    if not regioes:
        messagebox.showwarning("Atenção", "Nenhuma região cadastrada.")
        janela.destroy()
        return

    nomes_regioes = [f"{r['nome']} ({r['id']})" for r in regioes]
    regiao_var = tk.StringVar(janela)
    regiao_var.set(nomes_regioes[0])  # default

    regiao_menu = tk.OptionMenu(janela, regiao_var, *nomes_regioes)
    regiao_menu.pack()

    def salvar_cliente():
        nome = nome_entry.get()
        cpf = cpf_entry.get()
        telefone = telefone_entry.get()
        regiao_info = regiao_var.get()

        if not nome or not cpf or not telefone or not regiao_info:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        regiao_id = regiao_info.split("(")[-1].replace(")", "")

        novo_cliente = {
            "id": str(uuid.uuid4()),
            "nome": nome,
            "cpf": cpf,
            "telefone": telefone,
            "regiao_id": regiao_id
        }

        clientes = carregar_dados(CAMINHO_CLIENTES)
        clientes.append(novo_cliente)
        salvar_dados(CAMINHO_CLIENTES, clientes)

        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        janela.destroy()

    tk.Button(janela, text="Cadastrar", command=salvar_cliente).pack(pady=10)