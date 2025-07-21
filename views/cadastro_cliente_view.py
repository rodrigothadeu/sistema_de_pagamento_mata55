import tkinter as tk
from tkinter import messagebox
from uuid import uuid4
from utils.arquivo import carregar_dados, salvar_dados
from data.caminhos import CAMINHO_CLIENTES, CAMINHO_REGIOES

class CadastroClienteView:
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Cadastrar Cliente")
        self.window.geometry("400x300")

        tk.Label(self.window, text="Nome:").pack(pady=5)
        self.entry_nome = tk.Entry(self.window, width=40)
        self.entry_nome.pack()

        tk.Label(self.window, text="CPF:").pack(pady=5)
        self.entry_cpf = tk.Entry(self.window, width=40)
        self.entry_cpf.pack()

        tk.Label(self.window, text="Telefone:").pack(pady=5)
        self.entry_telefone = tk.Entry(self.window, width=40)
        self.entry_telefone.pack()

        tk.Label(self.window, text="Região:").pack(pady=5)
        self.regioes = carregar_dados(CAMINHO_REGIOES)
        self.regiao_var = tk.StringVar(self.window)
        if self.regioes:
            self.regiao_var.set(self.regioes[0]["id"])  # padrão
        options = [r["nome"] for r in self.regioes]
        self.dropdown = tk.OptionMenu(self.window, self.regiao_var, *options)
        self.dropdown.pack()

        tk.Button(self.window, text="Cadastrar", command=self.cadastrar_cliente).pack(pady=15)

    def cadastrar_cliente(self):
        try:
            nome = self.entry_nome.get()
            cpf = self.entry_cpf.get()
            telefone = self.entry_telefone.get()
            regiao_nome = self.regiao_var.get()

            if not nome or not cpf or not telefone:
                messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
                return

            regiao_id = next((r["id"] for r in self.regioes if r["nome"] == regiao_nome), None)
            if not regiao_id:
                raise ValueError("Região inválida")

            cliente = {
                "id": str(uuid4()),
                "nome": nome,
                "cpf": cpf,
                "telefone": telefone,
                "regiao_id": regiao_id
            }

            clientes = carregar_dados(CAMINHO_CLIENTES)
            clientes.append(cliente)
            salvar_dados(CAMINHO_CLIENTES, clientes)

            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            self.window.destroy()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar cliente: {e}")
