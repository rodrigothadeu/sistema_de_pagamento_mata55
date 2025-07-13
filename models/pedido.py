from typing import List

class Pedido:
    def __init__(self, id: int, cliente_id: int, itens: List[dict]):
        self._id = id
        self._cliente_id = cliente_id
        self._itens = itens
        self._total = self._calcular_total()

    def _calcular_total(self):
        return sum(item.get("preco", 0) for item in self._itens)

    def to_dict(self):
        return {
            "id": self._id,
            "cliente_id": self._cliente_id,
            "itens": self._itens,
            "total": self._total
        }

    def __str__(self):
        return f"Pedido #{self._id} | Cliente: {self._cliente_id} | Total: R$ {self._total:.2f}"