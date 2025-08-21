#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Inicialização para Produção

Este script prepara e inicia a aplicação em modo de produção.
Ele verifica as configurações necessárias e inicializa o banco de dados se necessário.
"""

import os
import sys
import secrets
from pathlib import Path

def check_environment():
    """Verifica se o ambiente está configurado corretamente"""
    print("🔍 Verificando configurações do ambiente...")
    
    # Verifica se o arquivo .env existe
    if not os.path.exists('.env'):
        print("❌ Arquivo .env não encontrado!")
        print("📝 Criando arquivo .env com configurações padrão...")
        create_env_file()
    else:
        print("✅ Arquivo .env encontrado")
    
    # Verifica se o diretório de logs existe
    if not os.path.exists('logs'):
        print("📁 Criando diretório de logs...")
        os.makedirs('logs')
    else:
        print("✅ Diretório de logs existe")
    
    # Verifica se o banco de dados existe
    if not os.path.exists('instance/iss_database.db'):
        print("🗄️ Banco de dados não encontrado. Inicializando...")
        initialize_database()
    else:
        print("✅ Banco de dados encontrado")
    
    print("✅ Verificação do ambiente concluída!")

def create_env_file():
    """Cria um arquivo .env com configurações seguras"""
    secret_key = secrets.token_hex(32)
    
    env_content = f"""# Configurações de Produção
FLASK_CONFIG=production
FLASK_ENV=production
FLASK_DEBUG=False

# Chave secreta gerada automaticamente
SECRET_KEY={secret_key}

# Configuração do Banco de Dados
# Para MySQL em produção, descomente e configure:
# DATABASE_URL=mysql+pymysql://usuario:senha@localhost/iss_database
# Para SQLite (padrão):
DATABASE_URL=sqlite:///instance/iss_database.db

# Configurações de Segurança
SESSION_COOKIE_SECURE=True
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE=Lax

# Configurações de Logging
LOG_LEVEL=INFO
LOG_FILE=logs/app.log

# Configurações do Servidor
HOST=0.0.0.0
PORT=5000

# Configurações de Performance
THREADS=4
WORKERS=2
"""
    
    with open('.env', 'w', encoding='utf-8') as f:
        f.write(env_content)
    
    print(f"✅ Arquivo .env criado com SECRET_KEY segura")

def initialize_database():
    """Inicializa o banco de dados"""
    try:
        # Cria o diretório instance se não existir
        os.makedirs('instance', exist_ok=True)
        
        # Executa o script de inicialização do banco
        if os.path.exists('init_db.py'):
            print("🔄 Executando script de inicialização do banco...")
            os.system('python init_db.py')
            print("✅ Banco de dados inicializado com sucesso")
        else:
            print("⚠️ Script init_db.py não encontrado. Criando apenas as tabelas...")
            from app import create_app, db
            app = create_app('production')
            with app.app_context():
                db.create_all()
            print("✅ Tabelas do banco criadas")
    
    except Exception as e:
        print(f"❌ Erro ao inicializar banco de dados: {e}")
        sys.exit(1)

def check_dependencies():
    """Verifica se as dependências estão instaladas"""
    print("📦 Verificando dependências...")
    
    try:
        import flask
        import flask_sqlalchemy
        import pymysql
        import cryptography
        print("✅ Todas as dependências estão instaladas")
    except ImportError as e:
        print(f"❌ Dependência faltando: {e}")
        print("💡 Execute: pip install -r requirements.txt")
        sys.exit(1)

def start_production_server():
    """Inicia o servidor em modo de produção"""
    print("🚀 Iniciando servidor em modo de produção...")
    print("📋 Configurações:")
    print(f"   - Host: {os.getenv('HOST', '0.0.0.0')}")
    print(f"   - Porta: {os.getenv('PORT', '5000')}")
    print(f"   - Debug: {os.getenv('FLASK_DEBUG', 'False')}")
    print(f"   - Ambiente: {os.getenv('FLASK_ENV', 'production')}")
    print("")
    print("💡 Para produção real, considere usar Gunicorn:")
    print("   gunicorn --bind 0.0.0.0:5000 --workers 4 wsgi:application")
    print("")
    
    # Importa e executa a aplicação
    from wsgi import application
    application.run(
        host=os.getenv('HOST', '0.0.0.0'),
        port=int(os.getenv('PORT', 5000)),
        debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true',
        threaded=True
    )

def main():
    """Função principal"""
    print("🏭 Inicializador de Produção - Busca Assertiva ISS")
    print("=" * 50)
    
    # Carrega variáveis de ambiente
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("⚠️ python-dotenv não instalado. Variáveis de ambiente podem não ser carregadas.")
    
    # Executa verificações
    check_dependencies()
    check_environment()
    
    print("\n" + "=" * 50)
    print("✅ Ambiente preparado com sucesso!")
    print("=" * 50 + "\n")
    
    # Pergunta se deve iniciar o servidor
    response = input("🚀 Deseja iniciar o servidor agora? (s/N): ").lower().strip()
    if response in ['s', 'sim', 'y', 'yes']:
        start_production_server()
    else:
        print("\n📝 Para iniciar manualmente:")
        print("   python wsgi.py")
        print("   ou")
        print("   gunicorn --bind 0.0.0.0:5000 --workers 4 wsgi:application")

if __name__ == '__main__':
    main()