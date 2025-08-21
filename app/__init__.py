import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG') or 'default'
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Configuração de Logging
    setup_logging(app)
    
    # Inicializar extensões
    db.init_app(app)
    
    # Registrar blueprints/rotas
    from .routes import main
    app.register_blueprint(main)
    
    # Criar tabelas do banco de dados
    with app.app_context():
        db.create_all()
    
    return app

def setup_logging(app):
    """Configura o sistema de logging para a aplicação"""
    if not app.debug and not app.testing:
        # Configuração para produção
        log_level = getattr(logging, os.getenv('LOG_LEVEL', 'INFO').upper())
        log_file = os.getenv('LOG_FILE', 'logs/app.log')
        
        # Cria o diretório de logs se não existir
        log_dir = os.path.dirname(log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # Configuração do handler de arquivo com rotação
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=10240000,  # 10MB
            backupCount=10
        )
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(log_level)
        app.logger.addHandler(file_handler)
        
        # Configuração do handler de console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s'
        ))
        console_handler.setLevel(log_level)
        app.logger.addHandler(console_handler)
        
        app.logger.setLevel(log_level)
        app.logger.info('Aplicação ISS iniciada em modo de produção')
    else:
        # Configuração para desenvolvimento
        app.logger.setLevel(logging.DEBUG)
        app.logger.info('Aplicação ISS iniciada em modo de desenvolvimento')