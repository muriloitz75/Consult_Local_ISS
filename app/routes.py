from flask import Blueprint, render_template, request, jsonify
from app.engine import ISSEngine
from app.models import Servico

main = Blueprint('main', __name__)
engine = ISSEngine()

@main.route('/')
def index():
    """
    Página principal de consulta
    """
    servicos = engine.listar_servicos()
    return render_template('index.html', servicos=servicos)

@main.route('/consultar', methods=['POST'])
def consultar():
    """
    Endpoint para processar a consulta de ISS
    """
    try:
        # Obter dados do formulário
        servico_id = request.form.get('servico_id')
        municipio_prestador = request.form.get('municipio_prestador', '').strip()
        municipio_tomador = request.form.get('municipio_tomador', '').strip()
        municipio_execucao = request.form.get('municipio_execucao', '').strip()
        
        # Converter servico_id para int se não estiver vazio
        if servico_id:
            servico_id = int(servico_id)
        
        # Realizar consulta
        resultado = engine.consultar_iss(
            servico_id=servico_id,
            municipio_prestador=municipio_prestador,
            municipio_tomador=municipio_tomador,
            municipio_execucao=municipio_execucao
        )
        
        return jsonify(resultado)
        
    except ValueError as e:
        return jsonify({
            'sucesso': False,
            'erros': ['Dados inválidos fornecidos']
        }), 400
    
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erros': ['Erro interno do servidor']
        }), 500

@main.route('/api/servicos')
def api_servicos():
    """
    API para obter lista de serviços (para uso futuro)
    """
    servicos = engine.listar_servicos()
    return jsonify([
        {
            'id': s.id,
            'codigo': s.codigo,
            'descricao': s.descricao
        } for s in servicos
    ])