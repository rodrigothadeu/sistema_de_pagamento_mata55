from models.pagamento import Pagamento

class PagamentoCartaoCredito(Pagamento):
    def __init__(self, pedido_id: str, cliente_id: str, valor: float, numero_cartao: str, validade: str, cvv: str):
        """
        Inicializa o pagamento com cartão de crédito.
        """
        super().__init__(pedido_id, cliente_id, valor, forma="Crédito")
        self.numero_cartao = numero_cartao
        self.validade = validade
        self.cvv = cvv

    def pagar(self) -> dict:
        """
        Simula o pagamento com cartão de crédito.
        """
        print(f"[Cartão Crédito] Finalizando pagamento com final {self.numero_cartao[-4:]}")
        return self.to_dict()


class PagamentoCartaoDebito(Pagamento):
    def __init__(self, pedido_id: str, cliente_id: str, valor: float, numero_cartao: str, validade: str, cvv: str):
        """
        Inicializa o pagamento com cartão de débito.
        """
        super().__init__(pedido_id, cliente_id, valor, forma="Débito")
        self.numero_cartao = numero_cartao
        self.validade = validade
        self.cvv = cvv

    def pagar(self) -> dict:
        """
        Simula o pagamento com cartão de débito.
        """
        print(f"[Cartão Débito] Finalizando pagamento com final {self.numero_cartao[-4:]}")
        return self.to_dict()