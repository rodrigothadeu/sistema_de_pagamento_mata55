import uuid

from utils.erros import tratar_erro
from services.logger import logger

from models.cliente import Cliente
from models.regiao import Regiao
from models.pedido_mock import PedidoMock
from services.pagamento_pix import PagamentoPix
from services.pagamento_cartao import PagamentoCartaoCredito, PagamentoCartaoDebito
from utils.arquivo import carregar_dados, salvar_dados
from models.pedido import Pedido
from utils.arquivo import carregar_dados, salvar_dados

from services.pagamento_service import PagamentoService
from data.caminhos import CAMINHO_PEDIDOS, CAMINHO_PAGAMENTOS

from utils.formatador import (
    validar_numero_cartao,
    validar_validade_cartao,
    validar_cvv
)

CAMINHO_CLIENTES = 'data/clientes.json'
CAMINHO_REGIOES = 'data/regioes.json'
CAMINHO_PEDIDOS = 'data/pedidos.json'
CAMINHO_PAGAMENTOS = 'data/pagamentos.json'
CAMINHO_CLIENTES = "data/cliente.json"
CAMINHO_PEDIDOS = "data/pedidos.json"

# ------------------ CLIENTE ------------------
def cadastrar_cliente():
    print("\n--- Cadastro de Cliente ---")
    try:
        cliente = Cliente(
            nome=input("Nome completo: "),
            cpf=input("CPF (somente números): "),
            telefone=input("Telefone com DDD: "),
            regiao_id=input("ID da região: ")
        )
        clientes = carregar_dados(CAMINHO_CLIENTES)
        clientes.append(cliente.to_dict())
        salvar_dados(CAMINHO_CLIENTES, clientes)
        print(f"\n✅ Cliente {cliente.nome} cadastrado com sucesso!")
        logger.info(f"Cliente cadastrado: {cliente.nome} | CPF: {cliente.cpf} | Região: {cliente.regiao_id}")
    except Exception as e:
        tratar_erro("Falha ao cadastrar o cliente.", e)

# ------------------ REGIÃO ------------------
def cadastrar_regiao():
    print("\n--- Cadastro de Região ---")
    try:
        regiao = Regiao(
            nome=input("Nome da região: "),
            taxa_entrega=float(input("Taxa de entrega (R$): "))
        )
        regioes = carregar_dados(CAMINHO_REGIOES)
        regioes.append(regiao.to_dict())
        salvar_dados(CAMINHO_REGIOES, regioes)
        print(f"\n✅ Região '{regiao.nome}' cadastrada com sucesso!")
        logger.info(f"Região cadastrada: {regiao.nome} | Taxa: R$ {regiao.taxa_entrega:.2f}")
    except ValueError:
        tratar_erro("A taxa deve ser um número decimal.")
    except Exception as e:
        tratar_erro("Falha ao cadastrar a região.", e)

# ------------------ PEDIDO MOCK ------------------
def gerar_pedido_mock():
    try:
        clientes = carregar_dados(CAMINHO_CLIENTES)
        if not clientes:
            print("❌ Nenhum cliente cadastrado.")
            return

        print("\n--- Gerar Pedido Mockado ---")
        for i, cliente in enumerate(clientes):
            print(f"{i + 1} - {cliente['nome']} (ID: {cliente['id']})")

        cliente_escolhido = clientes[int(input("Escolha o número do cliente: ")) - 1]
        pedido = PedidoMock(cliente_id=cliente_escolhido['id'])

        pedidos = carregar_dados(CAMINHO_PEDIDOS)
        pedidos.append(pedido.to_dict())
        salvar_dados(CAMINHO_PEDIDOS, pedidos)

        print("\n✅ Pedido gerado com sucesso!")
        print(f"Itens: {pedido.itens}\nValor total: R$ {pedido.valor_total:.2f}")
        logger.info(f"Pedido gerado para cliente {cliente_escolhido['nome']} | Valor: R$ {pedido.valor_total:.2f}")
    except (ValueError, IndexError):
        tratar_erro("Cliente inválido.")
    except Exception as e:
        tratar_erro("Erro ao gerar pedido.", e)

# ------------------ PAGAMENTOS ------------------
def realizar_pagamento(pagamento_cls, descricao):
    try:
        pagamento_service = PagamentoService(pagamento_cls, descricao)
        pagamento_service.processar_pagamento()
    except (ValueError, IndexError):
        tratar_erro("Pedido inválido.")
    except Exception as e:
        tratar_erro(f"Erro ao processar pagamento via {descricao}.", e)

def realizar_pagamento_pix():
    realizar_pagamento(PagamentoPix, "PIX")

def realizar_pagamento_credito():
    realizar_pagamento(PagamentoCartaoCredito, "Cartão de Crédito")

def realizar_pagamento_debito():
    realizar_pagamento(PagamentoCartaoDebito, "Cartão de Débito")


# ------------------ CADASTRO DE PEDIDO ------------------

def cadastrar_pedido():
    clientes = carregar_dados(CAMINHO_CLIENTES)
    if not clientes:
        print("❌ Nenhum cliente cadastrado.")
        return

    print("\n📋 Clientes disponíveis:")
    for cliente in clientes:
        print(f"- ID: {cliente['id']} | Nome: {cliente['nome']}")

    cliente_id = input("Informe o ID do cliente: ").strip()

    if not any(c["id"] == cliente_id for c in clientes):
        print("❌ Cliente não encontrado.")
        return

    itens = []
    while True:
        nome = input("🍣 Nome do item: ")
        preco = float(input("💵 Preço do item (R$): "))
        itens.append({"nome": nome, "preco": preco})

        continuar = input("➕ Adicionar mais itens? (s/n): ").strip().lower()
        if continuar != "s":
            break

    pedidos = carregar_dados(CAMINHO_PEDIDOS)
    novo_id = str(uuid.uuid4())
    pedido = Pedido(novo_id, cliente_id, itens)
    pedidos.append(pedido.to_dict())
    salvar_dados(CAMINHO_PEDIDOS, pedidos)

    print(f"\n✅ Pedido registrado com sucesso! Total: R$ {pedido.to_dict()['total']:.2f}")