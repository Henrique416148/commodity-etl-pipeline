#!/usr/bin/env python
"""
Script de teste para validar a estrutura do projeto ETL de commodities.
"""

import sys
import subprocess
from pathlib import Path

def verificar_importacoes():
    """Verifica se todas as bibliotecas necessárias estão disponíveis."""
    print("🔍 Verificando importações...")
    
    bibliotecas_necessarias = [
        'pandas',
        'yfinance',
        'sqlalchemy',
        'dotenv'
    ]
    
    for biblioteca in bibliotecas_necessarias:
        try:
            __import__(biblioteca)
            print(f"  ✅ {biblioteca} instalado")
        except ImportError:
            print(f"  ❌ {biblioteca} NÃO INSTALADO")
            return False
    
    return True

def verificar_arquivos():
    """Verifica se todos os arquivos necessários existem."""
    print("\n📁 Verificando arquivos do projeto...")
    
    arquivos_necessarios = [
        'main.py',
        'requirements.txt',
        '.env.example',
        'README.md'
    ]
    
    raiz = Path(__file__).parent
    
    for arquivo in arquivos_necessarios:
        caminho = raiz / arquivo
        if caminho.exists():
            print(f"  ✅ {arquivo} encontrado")
        else:
            print(f"  ❌ {arquivo} NÃO ENCONTRADO")
            return False
    
    return True

def verificar_sintaxe_python():
    """Verifica a sintaxe do arquivo main.py."""
    print("\n🐍 Verificando sintaxe Python...")
    
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            compile(f.read(), 'main.py', 'exec')
        print("  ✅ main.py tem sintaxe válida")
        return True
    except SyntaxError as e:
        print(f"  ❌ Erro de sintaxe: {e}")
        return False

def verificar_estrutura_codigo():
    """Verifica se as funções esperadas existem em main.py."""
    print("\n🏗️  Verificando estrutura do código...")
    
    funcoes_esperadas = [
        'conectar_banco',
        'extrair_dados_commodities',
        'main'
    ]
    
    with open('main.py', 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    for funcao in funcoes_esperadas:
        if f'def {funcao}' in conteudo:
            print(f"  ✅ Função '{funcao}' encontrada")
        else:
            print(f"  ❌ Função '{funcao}' NÃO ENCONTRADA")
            return False
    
    return True

def main():
    """Executa todos os testes."""
    print("=" * 60)
    print("🧪 Teste de Validação - Commodity ETL Pipeline")
    print("=" * 60)
    
    testes = [
        verificar_importacoes,
        verificar_arquivos,
        verificar_sintaxe_python,
        verificar_estrutura_codigo
    ]
    
    resultados = [teste() for teste in testes]
    
    print("\n" + "=" * 60)
    if all(resultados):
        print("✅ TODOS OS TESTES PASSARAM!")
        print("=" * 60)
        return 0
    else:
        print("❌ ALGUNS TESTES FALHARAM!")
        print("=" * 60)
        return 1

if __name__ == '__main__':
    sys.exit(main())
