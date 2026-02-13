import logging
from typing import List
import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from dotenv import load_dotenv 
import os

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 1. Carregar variáveis de ambiente
load_dotenv()

def conectar_banco() -> Engine:
    """
    Conecta ao banco de dados PostgreSQL usando variáveis de ambiente.
    
    Returns:
        Engine: SQLAlchemy engine para conexão com banco de dados.
        
    Raises:
        ValueError: Se variáveis de ambiente obrigatórias não forem encontradas.
    """
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_port = os.getenv('DB_PORT', '5432')
    
    # Validar variáveis obrigatórias
    variaveis_obrigatorias = {'DB_USER': db_user, 'DB_PASS': db_pass, 
                              'DB_HOST': db_host, 'DB_NAME': db_name}
    
    for chave, valor in variaveis_obrigatorias.items():
        if not valor:
            raise ValueError(f"Variável de ambiente '{chave}' não foi configurada.")
    
    url = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    logger.info(f"Conectando ao banco de dados: {db_host}:{db_port}/{db_name}")
    
    return create_engine(url)

def extrair_dados_commodities(commodities: List[str]) -> pd.DataFrame:
    """
    Extrai dados de commodities do Yahoo Finance.
    
    Args:
        commodities: Lista de símbolos de commodities (ex: ['CL=F', 'GC=F']).
        
    Returns:
        DataFrame com dados históricos das commodities.
        
    Raises:
        ValueError: Se nenhum dado for extraído para as commodities.
    """
    todos_dados = []
    
    for simbolo in commodities:
        try:
            logger.info(f"Extraindo dados de: {simbolo}...")
            ticker = yf.Ticker(simbolo)
            dados = ticker.history(period='5d')
            
            if not dados.empty:
                dados['simbolo'] = simbolo
                todos_dados.append(dados)
                logger.info(f"Dados extraídos com sucesso para {simbolo}.")
            else:
                logger.warning(f"Nenhum dado encontrado para {simbolo}.")
        except Exception as e:
            logger.error(f"Erro ao extrair dados de {simbolo}: {str(e)}")
    
    if not todos_dados:
        raise ValueError("Nenhum dado de commodities foi extraído.")
    
    return pd.concat(todos_dados)

def main():
    """
    Função principal que orquestra o pipeline ETL.
    Extrai dados de commodities e armazena no banco de dados.
    """
    try:
        lista_commodities = ['CL=F', 'GC=F', 'SI=F']
        logger.info("Iniciando pipeline de commodities...")
        
        df_final = extrair_dados_commodities(lista_commodities)
        logger.info(f"Total de registros extraídos: {len(df_final)}")
        
        engine = conectar_banco()
        df_final.to_sql('commodities_raw', engine, if_exists='replace', index=True)
        logger.info("Dados armazenados com sucesso na tabela 'commodities_raw'.")
        
        print("\n✅ Sucesso! Dados guardados na tabela 'commodities_raw'.")
        
    except Exception as e:
        logger.error(f"Erro no pipeline: {str(e)}")
        print(f"\n❌ Erro ao executar o pipeline: {str(e)}")
        raise

if __name__ == "__main__":
    main()