from flask_sqlalchemy import SQLAlchemy
from app import db

class Servico(db.Model):
    __tablename__ = 'servicos'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigo = db.Column(db.String(10), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    
    # Relacionamento com regras
    regras = db.relationship('Regra', backref='servico', lazy=True)
    
    def __repr__(self):
        return f'<Servico {self.codigo}: {self.descricao[:50]}...>'

class Regra(db.Model):
    __tablename__ = 'regras'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    servico_id = db.Column(db.Integer, db.ForeignKey('servicos.id'), nullable=False)
    local_recolhimento = db.Column(db.String(50), nullable=False)
    justificativa_legal = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<Regra {self.id}: {self.local_recolhimento}>'