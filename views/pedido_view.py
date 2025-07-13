import tkinter as tk
from tkinter import messagebox
import uuid
from data.caminhos import CAMINHO_PEDIDOS
from utils.arquivo import carregar_dados, salvar_dados

CARDAPIO = [
    {"nome": "Sushi de Salmão", "preco": 32.0},
    {"nome": "Combinado Simples", "preco": 40.0},
    {"nome": "Combinado Especial", "preco": 55.0},
    {"nome": "Uramaki", "preco": 20.0},
    {"nome": "Sashimi", "preco": 25.0},
    {"nome": "Sunomono", "preco": 15.0}
]

def abrir_tela_pedido_real():
    janela = tk.Toplevel()
    janela.title("Cadastrar Pedido Real")

    clientes = carregar_dados("data/cliente.json")
    if not clientes:
        messagebox.showwarning("Atenção", "Não há clientes cadastrados.")
        janela.destroy()
        return

    tk.Label(janela, text="Selecione o cliente:").pack()
    cliente_var = tk.StringVar(janela)
    cliente_var.set(clientes[0]['id'])
    menu_clientes = tk.OptionMenu(janela, cliente_var, *[cliente['id'] for cliente in clientes])
    menu_clientes.pack(pady=5)

    tk.Label(janela, text="Selecione os itens do pedido:").pack()
    itens_vars = []
    for item in CARDAPIO:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(janela, text=f"{item['nome']} - R$ {item['preco']:.2f}", variable=var)
        chk.pack(anchor="w")
        itens_vars.append((var, item))

    def cadastrar_pedido():
        cliente_id = cliente_var.get()
        itens_selecionados = [item for var, item in itens_vars if var.get()]

        if not itens_selecionados:
            messagebox.showwarning("Atenção", "Selecione ao menos um item.")
            return

        total = sum(item["preco"] for item in itens_selecionados)
        pedido = {
            "id": str(uuid.uuid4()),
            "cliente_id": cliente_id,
            "itens": itens_selecionados,
            "total": total
        }

        pedidos = carregar_dados(CAMINHO_PEDIDOS)
        pedidos.append(pedido)
        salvar_dados(CAMINHO_PEDIDOS, pedidos)

        messagebox.showinfo("Sucesso", "Pedido real cadastrado com sucesso!")
        janela.destroy()

    tk.Button(janela, text="Cadastrar Pedido", command=cadastrar_pedido).pack(pady=10)
