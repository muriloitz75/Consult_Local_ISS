#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste para verificar a criação do banco SQLite
"""

import sqlite3
import os

def test_sqlite_creation():
    """Testa a criação de um banco SQLite simples"""
    
    # Caminho para o banco de dados
    basedir = os.path.abspath(os.path.dirname(__file__))
    instance_dir = os.path.join(basedir, 'instance')
    db_path = os.path.join(instance_dir, 'test_database.db')
    
    print(f"Diretório base: {basedir}")
    print(f"Diretório instance: {instance_dir}")
    print(f"Caminho do banco: {db_path}")
    
    # Criar diretório se não existir
    if not os.path.exists(instance_dir):
        os.makedirs(instance_dir)
        print(f"Diretório {instance_dir} criado.")
    else:
        print(f"Diretório {instance_dir} já existe.")
    
    try:
        # Tentar criar conexão com SQLite
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Criar uma tabela simples
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS test_table (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')
        
        # Inserir dados de teste
        cursor.execute("INSERT INTO test_table (name) VALUES (?)", ("Teste",))
        conn.commit()
        
        # Verificar se os dados foram inseridos
        cursor.execute("SELECT * FROM test_table")
        results = cursor.fetchall()
        print(f"Dados inseridos: {results}")
        
        conn.close()
        print("✅ Banco SQLite criado e testado com sucesso!")
        
        # Verificar se o arquivo foi criado
        if os.path.exists(db_path):
            file_size = os.path.getsize(db_path)
            print(f"✅ Arquivo do banco criado: {db_path} ({file_size} bytes)")
        else:
            print("❌ Arquivo do banco não foi criado")
            
    except Exception as e:
        print(f"❌ Erro ao criar banco SQLite: {e}")
        return False
    
    return True

if __name__ == '__main__':
    print("=== Teste de Criação do Banco SQLite ===")
    success = test_sqlite_creation()
    if success:
        print("\n✅ Teste concluído com sucesso!")
    else:
        print("\n❌ Teste falhou!")