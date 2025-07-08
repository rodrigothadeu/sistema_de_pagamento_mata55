import json
import os

def carregar_dados(caminho_arquivo):
    """
    Carrega os dados de um arquivo JSON.
    Retorna uma lista vazia se o arquivo estiver vazio ou não existir.
    """
    if not os.path.exists(caminho_arquivo):
        return []
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_dados(caminho_arquivo, dados):
    """
    Salva os dados em um arquivo JSON.
    """
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)