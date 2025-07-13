import tkinter as tk
from tkinter import ttk, messagebox
from services.pagamento_service import PagamentoService
from services.pagamento_pix import PagamentoPix
from services.pagamento_cartao import PagamentoCartaoCredito, PagamentoCartaoDebito
from utils.arquivo import carregar_dados
from data.caminhos import CAMINHO_PEDIDOS

class PagamentoView:
    def __init__(self, master):
        self.master = tk.Toplevel(master)
        self.master.title("Realizar Pagamento")
        self.master.geometry("400x500")

        self.pedidos = carregar_dados(CAMINHO_PEDIDOS)
        if not self.pedidos:
            messagebox.showerror("Erro", "Nenhum pedido disponível.")
            self.master.destroy()
            return

        tk.Label(self.master, text="Selecione o Pedido:").pack(pady=5)
        self.combo_pedidos = ttk.Combobox(self.master, width=50)
        self.combo_pedidos["values"] = [
            f"{i+1} - ID: {p['id']} | Total: R$ {p['total']:.2f}"
            for i, p in enumerate(self.pedidos)
        ]
        self.combo_pedidos.pack(pady=5)

        tk.Label(self.master, text="Forma de Pagamento:").pack(pady=5)
        self.forma_pagamento = ttk.Combobox(self.master, values=["PIX", "Cartão de Crédito", "Cartão de Débito"])
        self.forma_pagamento.pack(pady=5)
        self.forma_pagamento.bind("<<ComboboxSelected>>", self.mostrar_campos_cartao)

        # Frame para campos de cartão
        self.frame_cartao = tk.Frame(self.master)
        self.frame_cartao.pack(pady=10)

        self.lbl_num = tk.Label(self.frame_cartao, text="Número do Cartão:")
        self.ent_num = tk.Entry(self.frame_cartao)
        self.lbl_val = tk.Label(self.frame_cartao, text="Validade (MM/AA):")
        self.ent_val = tk.Entry(self.frame_cartao)
        self.lbl_cvv = tk.Label(self.frame_cartao, text="CVV:")
        self.ent_cvv = tk.Entry(self.frame_cartao)

        self.btn_pagar = tk.Button(self.master, text="Confirmar Pagamento", command=self.realizar_pagamento)
        self.btn_pagar.pack(pady=20)

    def mostrar_campos_cartao(self, event=None):
        forma = self.forma_pagamento.get()
        if forma in ["Cartão de Crédito", "Cartão de Débito"]:
            self.lbl_num.pack(pady=2)
            self.ent_num.pack(pady=2)
            self.lbl_val.pack(pady=2)
            self.ent_val.pack(pady=2)
            self.lbl_cvv.pack(pady=2)
            self.ent_cvv.pack(pady=2)
        else:
            # Ocultar os campos se a forma não for cartão
            for widget in self.frame_cartao.winfo_children():
                widget.pack_forget()

    def realizar_pagamento(self):
        try:
            index = self.combo_pedidos.current()
            if index == -1:
                raise ValueError("Selecione um pedido.")
            
            pedido = self.pedidos[index]
            forma = self.forma_pagamento.get()

            match forma:
                case "PIX":
                    cls = PagamentoPix
                case "Cartão de Crédito":
                    cls = PagamentoCartaoCredito
                case "Cartão de Débito":
                    cls = PagamentoCartaoDebito
                case _:
                    raise ValueError("Forma de pagamento inválida.")

            service = PagamentoService(cls, forma)

            if cls.__name__.startswith("PagamentoCartao"):
                pagamento = service.processar_pagamento_manual(
                    pedido_id=pedido["id"],
                    cliente_id=pedido["cliente_id"],
                    valor=pedido["total"],
                    numero_cartao=self.ent_num.get(),
                    validade=self.ent_val.get(),
                    cvv=self.ent_cvv.get()
                )
            else:
                pagamento = service.processar_pagamento_manual(
                    pedido_id=pedido["id"],
                    cliente_id=pedido["cliente_id"],
                    valor=pedido["total"]
                )

            messagebox.showinfo("Sucesso", f"Pagamento via {forma} realizado com sucesso!")
            self.master.destroy()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao realizar pagamento: {e}")