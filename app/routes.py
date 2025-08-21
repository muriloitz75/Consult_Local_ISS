import re
from flask import Blueprint, render_template, request, jsonify, current_app
from werkzeug.exceptions import BadRequest
from app.engine import ISSEngine
from app.models import Servico

main = Blueprint('main', __name__)
engine = ISSEngine()

# Headers de segurança
@main.after_request
def add_security_headers(response):
    """Adiciona headers de segurança a todas as respostas"""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'"
    return response

def sanitize_input(text):
    """Sanitiza entrada de texto removendo caracteres perigosos"""
    if not text:
        return ''
    # Remove caracteres especiais perigosos
    text = re.sub(r'[<>"\'\/\\]', '', str(text))
    # Limita o tamanho
    return text[:100].strip()

def validate_servico_id(servico_id):
    """Valida ID do serviço"""
    if not servico_id:
        return None
    try:
        id_val = int(servico_id)
        if id_val < 1 or id_val > 99999:  # Range válido
            raise ValueError("ID fora do range válido")
        return id_val
    except (ValueError, TypeError):
        raise BadRequest("ID do serviço inválido")

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
        # Log da requisição
        current_app.logger.info(f'Consulta ISS recebida de IP: {request.remote_addr}')
        
        # Obter e validar dados do formulário
        servico_id = validate_servico_id(request.form.get('servico_id'))
        municipio_prestador = sanitize_input(request.form.get('municipio_prestador', ''))
        municipio_tomador = sanitize_input(request.form.get('municipio_tomador', ''))
        municipio_execucao = sanitize_input(request.form.get('municipio_execucao', ''))
        
        # Validação adicional de comprimento
        if len(municipio_prestador) < 2 and municipio_prestador:
            raise BadRequest("Nome do município prestador muito curto")
        if len(municipio_tomador) < 2 and municipio_tomador:
            raise BadRequest("Nome do município tomador muito curto")
        if len(municipio_execucao) < 2 and municipio_execucao:
            raise BadRequest("Nome do município de execução muito curto")
        
        # Realizar consulta
        resultado = engine.consultar_iss(
            servico_id=servico_id,
            municipio_prestador=municipio_prestador,
            municipio_tomador=municipio_tomador,
            municipio_execucao=municipio_execucao
        )
        
        current_app.logger.info('Consulta ISS processada com sucesso')
        return jsonify(resultado)
        
    except BadRequest as e:
        current_app.logger.warning(f'Requisição inválida: {str(e)}')
        return jsonify({
            'sucesso': False,
            'erros': [str(e)]
        }), 400
    
    except ValueError as e:
        current_app.logger.warning(f'Dados inválidos: {str(e)}')
        return jsonify({
            'sucesso': False,
            'erros': ['Dados inválidos fornecidos']
        }), 400
    
    except Exception as e:
        current_app.logger.error(f'Erro interno: {str(e)}')
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