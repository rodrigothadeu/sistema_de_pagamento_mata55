import tkinter as tk
from tkinter import messagebox
from utils.arquivo import carregar_dados, salvar_dados
from data.caminhos import CAMINHO_PEDIDOS
import uuid
import random

CARDAPIO = [
    {"nome": "Sushi de Salmão", "preco": 32.0},
    {"nome": "Combinado Simples", "preco": 40.0},
    {"nome": "Combinado Especial", "preco": 55.0},
    {"nome": "Uramaki", "preco": 20.0},
    {"nome": "Sashimi", "preco": 25.0},
    {"nome": "Sunomono", "preco": 15.0}
]

def abrir_tela_pedido_simulado():
    janela = tk.Toplevel()
    janela.title("Gerar Pedido Simulado")

    clientes = carregar_dados("data/cliente.json")
    if not clientes:
        messagebox.showwarning("Atenção", "Não há clientes cadastrados.")
        janela.destroy()
        return

    tk.Label(janela, text="Selecione um cliente:").pack()
    cliente_var = tk.StringVar(janela)
    cliente_var.set(clientes[0]['id'])

    menu_clientes = tk.OptionMenu(
        janela,
        cliente_var,
        *[cliente['id'] for cliente in clientes]
    )
    menu_clientes.pack()

    def gerar_pedido():
        cliente_id = cliente_var.get()
        itens = random.sample(CARDAPIO, random.randint(1, 3))
        total = sum(item["preco"] for item in itens)

        pedido = {
            "id": str(uuid.uuid4()),
            "cliente_id": cliente_id,
            "itens": itens,
            "total": total
        }

        pedidos = carregar_dados(CAMINHO_PEDIDOS)
        pedidos.append(pedido)
        salvar_dados(CAMINHO_PEDIDOS, pedidos)

        messagebox.showinfo("Sucesso", "Pedido simulado gerado com sucesso!")
        janela.destroy()

    tk.Button(janela, text="Gerar Pedido", command=gerar_pedido).pack(pady=10)