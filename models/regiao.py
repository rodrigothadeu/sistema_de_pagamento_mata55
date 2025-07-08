import uuid

class Regiao:
    def __init__(self, nome: str, taxa_entrega: float):
        """
        Inicializa uma nova região com um ID único.
        """
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.taxa_entrega = taxa_entrega

    def to_dict(self) -> dict:
        """
        Converte a região para um dicionário (para salvar em JSON).
        """
        return {
            "id": self.id,
            "nome": self.nome,
            "taxa_entrega": self.taxa_entrega
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma região a partir de um dicionário (carregado do JSON).
        """
        regiao = cls(
            nome=data["nome"],
            taxa_entrega=data["taxa_entrega"]
        )
        regiao.id = data["id"]
        return regiao
