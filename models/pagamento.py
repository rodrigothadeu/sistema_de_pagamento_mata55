from abc import ABC, abstractmethod
from datetime import datetime
import uuid

class Pagamento(ABC):
    def __init__(self, pedido_id: str, cliente_id: str, valor: float, forma: str):
        """
        Classe base para pagamentos.
        """
        self.id = str(uuid.uuid4())
        self.pedido_id = pedido_id
        self.cliente_id = cliente_id
        self.valor = valor
        self.forma = forma
        self.data_pagamento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @abstractmethod
    def pagar(self):
        """
        Método abstrato que deve ser implementado pelas subclasses.
        """
        pass

    def to_dict(self):
        """
        Converte o pagamento para dicionário.
        """
        return {
            "id": self.id,
            "pedido_id": self.pedido_id,
            "cliente_id": self.cliente_id,
            "valor": self.valor,
            "forma": self.forma,
            "data_pagamento": self.data_pagamento
        }
