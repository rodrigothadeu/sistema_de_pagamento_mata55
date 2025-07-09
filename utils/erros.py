from services.logger import logger

def tratar_erro(mensagem: str, excecao: Exception = None):
    """
    Exibe erro padronizado no terminal e registra log.
    """
    print(f"❌ Erro: {mensagem}")
    if excecao:
        print(f"🔍 Detalhes técnicos: {str(excecao)}")
        logger.error(f"{mensagem} | {str(excecao)}")
    else:
        logger.error(mensagem)