# Commodity ETL Pipeline

Um pipeline ETL robusto para extrair dados de commodities do Yahoo Finance e armazená-los em um banco de dados PostgreSQL.

## 🎯 Objetivo

Este projeto automatiza a extração de dados históricos de commodities como petróleo (CL=F), ouro (GC=F) e prata (SI=F), armazenando os dados em um banco de dados PostgreSQL para análise posterior.

## 📋 Pré-requisitos

- Python 3.8+
- PostgreSQL 12+
- pip (gerenciador de pacotes Python)

## 🚀 Instalação

### 1. Clonar o repositório
```bash
git clone https://github.com/Henrique416148/commodity-etl-pipeline.git
cd commodity-etl-pipeline
```

### 2. Criar ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas credenciais do PostgreSQL:
```
DB_USER=seu_usuario
DB_PASS=sua_senha
DB_HOST=localhost
DB_PORT=5432
DB_NAME=commodities_db
```

## 📦 Dependências

- **pandas**: Manipulação e análise de dados
- **yfinance**: Extração de dados financeiros do Yahoo Finance
- **sqlalchemy**: ORM para interação com banco de dados
- **python-dotenv**: Gerenciamento de variáveis de ambiente
- **psycopg2-binary**: Driver PostgreSQL para Python

## 🏃 Executar o Pipeline

```bash
python main.py
```

### Saída esperada:
```
2024-02-13 10:30:45,123 - INFO - Iniciando pipeline de commodities...
2024-02-13 10:30:45,456 - INFO - Extraindo dados de: CL=F...
2024-02-13 10:30:46,789 - INFO - Dados extraídos com sucesso para CL=F.
...
✅ Sucesso! Dados guardados na tabela 'commodities_raw'.
```

## 🔧 Estrutura do Código

### `main.py`

- **`conectar_banco()`**: Estabelece conexão com o banco de dados PostgreSQL
- **`extrair_dados_commodities(commodities)`**: Extrai dados históricos de commodities
- **`main()`**: Orquestra o pipeline ETL completo

## 📊 Estrutura de Dados

A tabela `commodities_raw` contém os seguintes campos:
- `index`: Índice (data)
- `Open`: Preço de abertura
- `High`: Maior preço do dia
- `Low`: Menor preço do dia
- `Close`: Preço de fechamento
- `Volume`: Volume de negociação
- `Dividends`: Dividendos
- `Stock Splits`: Desdobramentos de ações
- `simbolo`: Símbolo da commodity

## 🛠️ Tratamento de Erros

O pipeline implementa tratamento robusto de erros:
- Validação de variáveis de ambiente obrigatórias
- Tratamento de falhas na extração de dados
- Logging detalhado de todas as operações
- Mensagens de erro descritivas

## 🔍 Logging

O pipeline gera logs detalhados de todas as operações:
- INFO: Eventos principais do pipeline
- WARNING: Avisos sobre dados não encontrados
- ERROR: Erros durante a execução

## 📝 Exemplos de Uso

### Adicionar novas commodities
Modifique a lista em `main.py`:
```python
lista_commodities = ['CL=F', 'GC=F', 'SI=F', 'NG=F']  # Adiciona gás natural
```

### Alterar período histórico
No arquivo `main.py`, função `extrair_dados_commodities`:
```python
dados = ticker.history(period='1y')  # Captura 1 ano de dados
```

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`) e envie um pull request.

## 📄 Licença

Este projeto está sob a licença MIT.

## ✉️ Contato

Henrique416148 - [GitHub Profile](https://github.com/Henrique416148)
