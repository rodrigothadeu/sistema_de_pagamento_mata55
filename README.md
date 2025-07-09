# 🍣 Sistema de Pagamento — UM Sushi

Sistema desenvolvido como projeto da disciplina **MATA55 – Programação Orientada a Objetos**, com o objetivo de aplicar os princípios de POO na construção de um sistema funcional, modularizado, testável e orientado a boas práticas.

---

## 📌 Informações Gerais

- **Disciplina**: MATA55 – Programação Orientada a Objetos  
- **Semestre**: 2025.1  
- **Instituição**: Universidade Federal da Bahia (UFBA)  

---

## 👨‍🏫 Docente

- Prof. Gilberto de Souza Leite

---

## 👨‍🎓 Discentes

- Rodrigo Thadeu Santos  
- João Henrique Marinho

---

## ⚙️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/rodrigothadeu/sistema_de_pagamento_mata55.git
cd sistema_de_pagamento_mata55
```

### 2. Crie e ative o ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o sistema

```bash
python3 main.py
```

---

## 📂 Estrutura de Pastas

```bash
sistema_de_pagamento/
│
├── controllers/       # Controle principal do sistema
├── data/              # Arquivos JSON simulando o banco de dados
├── logs/              # Logs de execução
├── models/            # Modelos de entidade (Cliente, Região, Pagamento)
├── reports/           # Relatórios PDF gerados
├── services/          # Regras de negócio e integrações
├── utils/             # Utilitários (log, exceções, formatação)
├── main.py            # Arquivo de entrada principal
├── README.md          # Documentação do projeto
└── requirements.txt   # Dependências do projeto
```

---

## ✅ Boas Práticas de Versionamento

Este projeto segue o padrão [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):

| Tipo        | Quando Usar                          | Exemplo                             |
|-------------|--------------------------------------|-------------------------------------|
| `feat:`     | Nova funcionalidade                  | `feat: adicionar pedido mockado`    |
| `fix:`      | Correção de bug                      | `fix: corrigir erro no CPF`         |
| `refactor:` | Refatoração sem alterar comportamento| `refactor: modularizar sistema.py`  |
| `docs:`     | Alterações na documentação           | `docs: atualizar README`            |
| `chore:`    | Mudanças auxiliares (gitignore, etc) | `chore: adicionar .gitignore`       |

---

## 📝 Observações Finais

- Todos os dados são simulados e armazenados localmente em arquivos `.json`
- O sistema não depende de banco de dados externo
- Todas as funcionalidades seguem os princípios de POO, modularização e código limpo
- O projeto inclui logs, relatórios e tratamento de exceções
