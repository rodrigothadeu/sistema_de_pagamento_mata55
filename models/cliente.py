import uuid

class Cliente:
    def __init__(self, nome: str, cpf: str, telefone: str, regiao_id: str):
        """
        Inicializa um novo cliente com ID único.
        """
        self.id = str(uuid.uuid4())  # Gera um ID único
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.regiao_id = regiao_id

    def to_dict(self) -> dict:
        """
        Converte o cliente para um dicionário (usado para salvar em JSON).
        """
        return {
            "id": self.id,
            "nome": self.nome,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "regiao_id": self.regiao_id
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria um cliente a partir de um dicionário (carregado do JSON).
        """
        cliente = cls(
            nome=data["nome"],
            cpf=data["cpf"],
            telefone=data["telefone"],
            regiao_id=data["regiao_id"]
        )
        cliente.id = data["id"]
        return cliente
