import logging
import os

# Criar pasta de logs se não existir
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configuração do logger
logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("sistema_pagamento")