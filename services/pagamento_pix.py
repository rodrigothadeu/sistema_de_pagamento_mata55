from models.pagamento import Pagamento
import random
import string

class PagamentoPix(Pagamento):
    def __init__(self, pedido_id: str, cliente_id: str, valor: float):
        """
        Inicializa o pagamento via PIX.
        """
        super().__init__(pedido_id, cliente_id, valor, forma="PIX")
        self.codigo_pix = self.gerar_codigo_pix()

    def gerar_codigo_pix(self) -> str:
        """
        Gera um código aleatório de pagamento PIX.
        """
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))

    def pagar(self) -> dict:
        """
        Simula o pagamento via PIX e retorna os dados do pagamento.
        """
        print(f"[PIX] Código gerado: {self.codigo_pix}")
        return self.to_dict()
