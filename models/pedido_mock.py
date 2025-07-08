import uuid
import random

class PedidoMock:
    ITENS_DISPONIVEIS = {
        "Temaki": 22.0,
        "Sashimi": 28.0,
        "Hot Roll": 18.0,
        "Uramaki": 24.0,
        "Sunomono": 12.0,
        "Combinado Simples": 36.0,
        "Combinado Especial": 48.0
    }

    def __init__(self, cliente_id: str, qtd_itens: int = 3):
        """
        Cria um pedido simulado com itens aleatórios.
        """
        self.id = str(uuid.uuid4())
        self.cliente_id = cliente_id
        self.itens = random.sample(list(self.ITENS_DISPONIVEIS.keys()), qtd_itens)
        self.valor_total = sum([self.ITENS_DISPONIVEIS[item] for item in self.itens])

    def to_dict(self):
        """
        Retorna o pedido como dicionário (para salvar ou exibir).
        """
        return {
            "id": self.id,
            "cliente_id": self.cliente_id,
            "itens": self.itens,
            "valor_total": self.valor_total
        }
