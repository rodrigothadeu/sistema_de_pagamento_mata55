import re

def validar_numero_cartao(numero: str) -> bool:
    return bool(re.fullmatch(r"\d{16}", numero))

def validar_validade_cartao(validade: str) -> bool:
    return bool(re.fullmatch(r"(0[1-9]|1[0-2])\/\d{2}", validade))

def validar_cvv(cvv: str) -> bool:
    return bool(re.fullmatch(r"\d{3}", cvv))

def formatar_valor(valor: float) -> str:
    return f"R$ {valor:.2f}".replace(".", ",")
