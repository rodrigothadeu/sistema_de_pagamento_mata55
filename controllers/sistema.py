from utils.erros import tratar_erro
from services.logger import logger

from models.cliente import Cliente
from utils.arquivo import carregar_dados, salvar_dados

CAMINHO_CLIENTES = 'data/clientes.json'

def cadastrar_cliente():
    print("\n--- Cadastro de Cliente ---")
    try:
        nome = input("Nome completo: ")
        cpf = input("CPF (somente números): ")
        telefone = input("Telefone com DDD: ")
        regiao_id = input("ID da região: ")

        cliente = Cliente(nome, cpf, telefone, regiao_id)

        clientes = carregar_dados(CAMINHO_CLIENTES)
        clientes.append(cliente.to_dict())
        salvar_dados(CAMINHO_CLIENTES, clientes)

        print(f"\n✅ Cliente {cliente.nome} cadastrado com sucesso!")
        logger.info(f"Cliente cadastrado: {cliente.nome} | CPF: {cliente.cpf} | Região: {regiao_id}")
    except Exception as e:
        tratar_erro("Falha ao cadastrar o cliente.", e)
    
    
from models.regiao import Regiao
from utils.arquivo import carregar_dados, salvar_dados

CAMINHO_REGIOES = 'data/regioes.json'

def cadastrar_regiao():
    print("\n--- Cadastro de Região ---")
    try:
        nome = input("Nome da região: ")
        taxa = input("Taxa de entrega (R$): ")

        taxa_float = float(taxa)
        regiao = Regiao(nome, taxa_float)

        regioes = carregar_dados(CAMINHO_REGIOES)
        regioes.append(regiao.to_dict())
        salvar_dados(CAMINHO_REGIOES, regioes)

        print(f"\n✅ Região '{regiao.nome}' cadastrada com sucesso!")
        logger.info(f"Região cadastrada: {regiao.nome} | Taxa: R$ {regiao.taxa_entrega:.2f}")
    except ValueError:
        tratar_erro("A taxa deve ser um número decimal.")
    except Exception as e:
        tratar_erro("Falha ao cadastrar a região.", e)
    
    
from models.pedido_mock import PedidoMock

CAMINHO_PEDIDOS = 'data/pedidos.json'

def gerar_pedido_mock():
    try:
        clientes = carregar_dados(CAMINHO_CLIENTES)
        if not clientes:
            print("❌ Nenhum cliente cadastrado.")
            return

        print("\n--- Gerar Pedido Mockado ---")
        for i, cliente in enumerate(clientes):
            print(f"{i + 1} - {cliente['nome']} (ID: {cliente['id']})")

        escolha = input("Escolha o número do cliente: ")
        indice = int(escolha) - 1
        cliente_escolhido = clientes[indice]

        pedido = PedidoMock(cliente_id=cliente_escolhido['id'])
        pedidos = carregar_dados(CAMINHO_PEDIDOS)
        pedidos.append(pedido.to_dict())
        salvar_dados(CAMINHO_PEDIDOS, pedidos)

        print("\n✅ Pedido gerado com sucesso!")
        print(f"Itens: {pedido.itens}")
        print(f"Valor total: R$ {pedido.valor_total:.2f}")
        logger.info(f"Pedido gerado para cliente {cliente_escolhido['nome']} | Valor: R$ {pedido.valor_total:.2f}")
    except (ValueError, IndexError):
        tratar_erro("Cliente inválido.")
    except Exception as e:
        tratar_erro("Erro ao gerar pedido.", e)
    
    
from services.pagamento_pix import PagamentoPix

CAMINHO_PAGAMENTOS = 'data/pagamentos.json'

def realizar_pagamento_pix():
    try:
        pedidos = carregar_dados(CAMINHO_PEDIDOS)
        if not pedidos:
            print("❌ Nenhum pedido disponível.")
            return

        print("\n--- Pagamento via PIX ---")
        for i, pedido in enumerate(pedidos):
            print(f"{i + 1} - Pedido ID: {pedido['id']}, Cliente: {pedido['cliente_id']}, Valor: R$ {pedido['valor_total']:.2f}")

        escolha = input("Escolha o número do pedido: ")
        indice = int(escolha) - 1
        pedido_selecionado = pedidos[indice]

        pagamento = PagamentoPix(
            pedido_id=pedido_selecionado['id'],
            cliente_id=pedido_selecionado['cliente_id'],
            valor=pedido_selecionado['valor_total']
        )

        pagamentos = carregar_dados(CAMINHO_PAGAMENTOS)
        pagamentos.append(pagamento.pagar())
        salvar_dados(CAMINHO_PAGAMENTOS, pagamentos)

        print(f"\n✅ Pagamento via PIX realizado com sucesso!")
        logger.info(f"Pagamento PIX realizado | Pedido ID: {pagamento.pedido_id} | Valor: R$ {pagamento.valor:.2f}")
    except (ValueError, IndexError):
        tratar_erro("Pedido inválido.")
    except Exception as e:
        tratar_erro("Erro ao processar pagamento via PIX.", e)
    
    
from services.pagamento_cartao import PagamentoCartaoCredito

def realizar_pagamento_credito():
    """
    Realiza pagamento via cartão de crédito.
    """
    pedidos = carregar_dados(CAMINHO_PEDIDOS)
    if not pedidos:
        print("❌ Nenhum pedido disponível.")
        return

    print("\n--- Pagamento via Cartão de Crédito ---")
    print("Pedidos disponíveis:")
    for i, pedido in enumerate(pedidos):
        print(f"{i + 1} - Pedido ID: {pedido['id']}, Cliente: {pedido['cliente_id']}, Valor: R$ {pedido['valor_total']:.2f}")

    escolha = input("Escolha o número do pedido: ")
    try:
        indice = int(escolha) - 1
        pedido_selecionado = pedidos[indice]
    except (ValueError, IndexError):
        print("❌ Pedido inválido.")
        return

    numero_cartao = input("Número do cartão (16 dígitos): ")
    validade = input("Validade (MM/AA): ")
    cvv = input("CVV (3 dígitos): ")

    pagamento = PagamentoCartaoCredito(
        pedido_id=pedido_selecionado['id'],
        cliente_id=pedido_selecionado['cliente_id'],
        valor=pedido_selecionado['valor_total'],
        numero_cartao=numero_cartao,
        validade=validade,
        cvv=cvv
    )

    pagamentos = carregar_dados(CAMINHO_PAGAMENTOS)
    pagamentos.append(pagamento.pagar())
    salvar_dados(CAMINHO_PAGAMENTOS, pagamentos)

    print(f"\n✅ Pagamento via Cartão de Crédito realizado com sucesso!")
    
    
from services.pagamento_cartao import PagamentoCartaoDebito

def realizar_pagamento_debito():
    """
    Realiza pagamento via cartão de débito.
    """
    pedidos = carregar_dados(CAMINHO_PEDIDOS)
    if not pedidos:
        print("❌ Nenhum pedido disponível.")
        return

    print("\n--- Pagamento via Cartão de Débito ---")
    print("Pedidos disponíveis:")
    for i, pedido in enumerate(pedidos):
        print(f"{i + 1} - Pedido ID: {pedido['id']}, Cliente: {pedido['cliente_id']}, Valor: R$ {pedido['valor_total']:.2f}")

    escolha = input("Escolha o número do pedido: ")
    try:
        indice = int(escolha) - 1
        pedido_selecionado = pedidos[indice]
    except (ValueError, IndexError):
        print("❌ Pedido inválido.")
        return

    numero_cartao = input("Número do cartão (16 dígitos): ")
    validade = input("Validade (MM/AA): ")
    cvv = input("CVV (3 dígitos): ")

    pagamento = PagamentoCartaoDebito(
        pedido_id=pedido_selecionado['id'],
        cliente_id=pedido_selecionado['cliente_id'],
        valor=pedido_selecionado['valor_total'],
        numero_cartao=numero_cartao,
        validade=validade,
        cvv=cvv
    )

    pagamentos = carregar_dados(CAMINHO_PAGAMENTOS)
    pagamentos.append(pagamento.pagar())
    salvar_dados(CAMINHO_PAGAMENTOS, pagamentos)

    print(f"\n✅ Pagamento via Cartão de Débito realizado com sucesso!")