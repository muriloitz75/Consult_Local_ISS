from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Inicializar extensões
    db.init_app(app)
    
    # Registrar blueprints/rotas
    from .routes import main
    app.register_blueprint(main)
    
    # Criar tabelas do banco de dados
    with app.app_context():
        db.create_all()
    
    return app