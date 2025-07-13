from data.caminhos import CAMINHO_PEDIDOS, CAMINHO_PAGAMENTOS
from utils.arquivo import carregar_dados, salvar_dados
from utils.erros import tratar_erro
from services.logger import logger

class PagamentoService:
    def __init__(self, pagamento_cls, descricao):
        self.pagamento_cls = pagamento_cls
        self.descricao = descricao

    def processar_pagamento(self):
        try:
            pedidos = carregar_dados(CAMINHO_PEDIDOS)
            if not pedidos:
                print("❌ Nenhum pedido disponível.")
                return

            print(f"\n--- Pagamento via {self.descricao} ---")
            for i, pedido in enumerate(pedidos):
                print(f"{i + 1} - Pedido ID: {pedido['id']}, Cliente: {pedido['cliente_id']}, Valor: R$ {pedido['total']:.2f}")

            pedido_selecionado = pedidos[int(input("Escolha o número do pedido: ")) - 1]

            if self.pagamento_cls.__name__.startswith("PagamentoCartao"):
                numero_cartao = input("Número do cartão (16 dígitos): ")
                validade = input("Validade (MM/AA): ")
                cvv = input("CVV (3 dígitos): ")
                pagamento = self.pagamento_cls(
                    pedido_id=pedido_selecionado['id'],
                    cliente_id=pedido_selecionado['cliente_id'],
                    valor=pedido_selecionado['total'],
                    numero_cartao=numero_cartao,
                    validade=validade,
                    cvv=cvv
                )
            else:
                pagamento = self.pagamento_cls(
                    pedido_id=pedido_selecionado['id'],
                    cliente_id=pedido_selecionado['cliente_id'],
                    valor=pedido_selecionado['total']
                )

            pagamentos = carregar_dados(CAMINHO_PAGAMENTOS)
            pagamentos.append(pagamento.pagar())
            salvar_dados(CAMINHO_PAGAMENTOS, pagamentos)

            print(f"\n✅ Pagamento via {self.descricao} realizado com sucesso!")
            logger.info(f"Pagamento {self.descricao} realizado | Pedido ID: {pagamento.pedido_id} | Valor: R$ {pagamento.valor:.2f}")

        except (ValueError, IndexError):
            tratar_erro("Pedido inválido.")
        except Exception as e:
            tratar_erro(f"Erro ao processar pagamento via {self.descricao}.", e)