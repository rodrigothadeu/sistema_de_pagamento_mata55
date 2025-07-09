from fpdf import FPDF
from utils.arquivo import carregar_dados
from utils.erros import tratar_erro
from services.logger import logger
from datetime import datetime
import os

CAMINHO_PAGAMENTOS = "data/pagamentos.json"
CAMINHO_CLIENTES = "data/clientes.json"
CAMINHO_REGIOES = "data/regioes.json"
PASTA_RELATORIOS = "reports/"

def gerar_relatorio_pdf():
    try:
        pagamentos = carregar_dados(CAMINHO_PAGAMENTOS)
        clientes = carregar_dados(CAMINHO_CLIENTES)
        regioes = carregar_dados(CAMINHO_REGIOES)

        if not pagamentos:
            print("❌ Nenhum pagamento encontrado.")
            return

        cliente_por_id = {c["id"]: c for c in clientes}
        regiao_por_id = {r["id"]: r for r in regioes}

        total_por_forma = {}
        total_por_regiao = {}
        total_geral = 0.0

        for pagamento in pagamentos:
            forma = pagamento.get("forma", "Indefinida")
            valor = float(pagamento.get("valor", 0.0))
            cliente_id = pagamento.get("cliente_id")

            total_por_forma[forma] = total_por_forma.get(forma, 0.0) + valor

            regiao_id = cliente_por_id.get(cliente_id, {}).get("regiao_id")
            nome_regiao = regiao_por_id.get(regiao_id, {}).get("nome", "Desconhecida")
            total_por_regiao[nome_regiao] = total_por_regiao.get(nome_regiao, 0.0) + valor

            total_geral += valor

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=14)
        pdf.cell(200, 10, txt="Relatório de Pagamentos - UM Sushi", ln=True, align="C")
        pdf.ln(10)

        pdf.set_font("Arial", "B", size=12)
        pdf.cell(200, 10, txt="Total por Forma de Pagamento:", ln=True)
        pdf.set_font("Arial", size=12)
        for forma, valor in total_por_forma.items():
            pdf.cell(200, 8, txt=f"- {forma}: R$ {valor:.2f}", ln=True)

        pdf.ln(8)
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(200, 10, txt="Total por Região:", ln=True)
        pdf.set_font("Arial", size=12)
        for regiao, valor in total_por_regiao.items():
            pdf.cell(200, 8, txt=f"- {regiao}: R$ {valor:.2f}", ln=True)

        pdf.ln(8)
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(200, 10, txt=f"Total Geral Recebido: R$ {total_geral:.2f}", ln=True)

        if not os.path.exists(PASTA_RELATORIOS):
            os.makedirs(PASTA_RELATORIOS)

        nome_arquivo = f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        caminho_arquivo = os.path.join(PASTA_RELATORIOS, nome_arquivo)
        pdf.output(caminho_arquivo)

        print(f"\n✅ Relatório gerado com sucesso em: {caminho_arquivo}")
        logger.info(f"Relatório PDF gerado em: {caminho_arquivo}")

    except Exception as e:
        tratar_erro("Erro ao gerar o relatório em PDF.", e)