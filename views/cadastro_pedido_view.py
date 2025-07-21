import tkinter as tk
from tkinter import ttk, messagebox
from uuid import uuid4
from utils.arquivo import carregar_dados, salvar_dados
from data.caminhos import CAMINHO_PEDIDOS, CAMINHO_CLIENTES

class GestaoPedidosView:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestão de Pedidos")

        self.frame_form = tk.Frame(master)
        self.frame_form.pack(pady=10)

        tk.Label(self.frame_form, text="Cliente:").grid(row=0, column=0)
        self.clientes = carregar_dados(CAMINHO_CLIENTES)
        self.cliente_var = tk.StringVar()
        self.combo_clientes = ttk.Combobox(self.frame_form, textvariable=self.cliente_var, width=40)
        self.combo_clientes['values'] = [f"{c['nome']} ({c['id']})" for c in self.clientes]
        self.combo_clientes.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(self.frame_form, text="Nome do Item:").grid(row=1, column=0)
        self.nome_item = tk.Entry(self.frame_form)
        self.nome_item.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(self.frame_form, text="Preço:").grid(row=2, column=0)
        self.preco_item = tk.Entry(self.frame_form)
        self.preco_item.grid(row=2, column=1, padx=5, pady=2)

        self.itens = []
        self.lista_itens = tk.Listbox(self.frame_form, width=50)
        self.lista_itens.grid(row=3, columnspan=2, pady=5)

        tk.Button(self.frame_form, text="Adicionar Item", command=self.adicionar_item).grid(row=4, columnspan=2, pady=5)
        tk.Button(self.frame_form, text="Cadastrar Pedido", command=self.cadastrar_pedido).grid(row=5, columnspan=2, pady=5)

        self.frame_lista = tk.Frame(master)
        self.frame_lista.pack(pady=10)
        self.tabela = ttk.Treeview(self.frame_lista, columns=("ID", "Cliente", "Total", "Itens"), show='headings', height=10)
        self.tabela.heading("ID", text="ID")
        self.tabela.heading("Cliente", text="Cliente")
        self.tabela.heading("Total", text="Total (R$)")
        self.tabela.heading("Itens", text="Itens")
        self.tabela.pack()

        self.carregar_pedidos()

    def adicionar_item(self):
        nome = self.nome_item.get().strip()
        preco = self.preco_item.get().strip()

        if not nome or not preco:
            messagebox.showwarning("Campos obrigatórios", "Preencha nome e preço do item.")
            return

        try:
            preco = float(preco)
        except ValueError:
            messagebox.showwarning("Preço inválido", "Digite um preço válido.")
            return

        self.itens.append({"nome": nome, "preco": preco})
        self.lista_itens.insert(tk.END, f"{nome} - R$ {preco:.2f}")
        self.nome_item.delete(0, tk.END)
        self.preco_item.delete(0, tk.END)

    def cadastrar_pedido(self):
        if not self.cliente_var.get():
            messagebox.showerror("Erro", "Selecione um cliente.")
            return

        if not self.itens:
            messagebox.showerror("Erro", "Adicione ao menos um item.")
            return

        cliente_id = self.cliente_var.get().split('(')[-1].replace(')', '')
        total = sum(item['preco'] for item in self.itens)
        pedido = {
            "id": str(uuid4()),
            "cliente_id": cliente_id,
            "itens": self.itens,
            "total": total
        }

        pedidos = carregar_dados(CAMINHO_PEDIDOS)
        pedidos.append(pedido)
        salvar_dados(CAMINHO_PEDIDOS, pedidos)

        messagebox.showinfo("Sucesso", "Pedido cadastrado com sucesso!")
        self.itens = []
        self.lista_itens.delete(0, tk.END)
        self.carregar_pedidos()

    def carregar_pedidos(self):
        for row in self.tabela.get_children():
            self.tabela.delete(row)

        pedidos = carregar_dados(CAMINHO_PEDIDOS)
        for p in pedidos:
            cliente_nome = next((c['nome'] for c in self.clientes if c['id'] == p['cliente_id']), "Desconhecido")
            itens_str = ", ".join(item['nome'] for item in p['itens'])
            self.tabela.insert('', tk.END, values=(p['id'], cliente_nome, f"{p['total']:.2f}", itens_str))