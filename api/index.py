from flask import Flask, request, jsonify
import sys
import os

# Configuração simples para Vercel
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vercel-production-key-2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iss_temp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Dados simplificados para funcionar sem banco de dados complexo
SERVICOS_LC116 = {
    'desenvolvimento': {
        'item': '1.01',
        'descricao': 'Análise e desenvolvimento de sistemas',
        'regra': 'ISS devido no local do estabelecimento prestador'
    },
    'consultoria': {
        'item': '1.02', 
        'descricao': 'Programação',
        'regra': 'ISS devido no local do estabelecimento prestador'
    },
    'manutencao': {
        'item': '1.03',
        'descricao': 'Processamento, armazenamento ou hospedagem de dados',
        'regra': 'ISS devido no local do estabelecimento prestador'
    },
    'design': {
        'item': '13.02',
        'descricao': 'Elaboração de desenhos técnicos',
        'regra': 'ISS devido no local do estabelecimento prestador'
    },
    'marketing': {
        'item': '17.02',
        'descricao': 'Propaganda e publicidade',
        'regra': 'ISS devido no local do estabelecimento prestador'
    }
}

def buscar_servico(descricao):
    """Busca serviço baseado na descrição"""
    descricao_lower = descricao.lower()
    
    for palavra_chave, dados in SERVICOS_LC116.items():
        if palavra_chave in descricao_lower:
            return dados
    
    # Busca por palavras-chave específicas
    if any(palavra in descricao_lower for palavra in ['software', 'sistema', 'aplicativo', 'app']):
        return SERVICOS_LC116['desenvolvimento']
    elif any(palavra in descricao_lower for palavra in ['site', 'website', 'web']):
        return SERVICOS_LC116['desenvolvimento']
    elif any(palavra in descricao_lower for palavra in ['consultoria', 'assessoria']):
        return SERVICOS_LC116['consultoria']
    
    return None

@app.route('/')
def index():
    """Página inicial da aplicação"""
    return '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Busca Assertiva ISS - LC 116/2003</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c3e50;
                text-align: center;
                margin-bottom: 30px;
            }
            .form-group {
                margin-bottom: 20px;
            }
            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
                color: #34495e;
            }
            input, textarea {
                width: 100%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                font-size: 16px;
            }
            button {
                background-color: #3498db;
                color: white;
                padding: 12px 30px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                width: 100%;
            }
            button:hover {
                background-color: #2980b9;
            }
            .resultado {
                margin-top: 20px;
                padding: 15px;
                border-radius: 5px;
                display: none;
            }
            .sucesso {
                background-color: #d4edda;
                border: 1px solid #c3e6cb;
                color: #155724;
            }
            .erro {
                background-color: #f8d7da;
                border: 1px solid #f5c6cb;
                color: #721c24;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔍 Busca Assertiva ISS - LC 116/2003</h1>
            <form id="consultaForm">
                <div class="form-group">
                    <label for="servico">Descrição do Serviço:</label>
                    <textarea id="servico" name="servico" rows="3" placeholder="Descreva o serviço que deseja consultar..." required></textarea>
                </div>
                <div class="form-group">
                    <label for="municipio">Município:</label>
                    <input type="text" id="municipio" name="municipio" placeholder="Nome do município" required>
                </div>
                <button type="submit">Consultar ISS</button>
            </form>
            <div id="resultado" class="resultado"></div>
        </div>

        <script>
            document.getElementById('consultaForm').addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const formData = new FormData(this);
                const resultado = document.getElementById('resultado');
                
                try {
                    const response = await fetch('/consultar', {
                        method: 'POST',
                        body: formData
                    });
                    
                    const data = await response.json();
                    
                    if (data.sucesso) {
                        resultado.className = 'resultado sucesso';
                        resultado.innerHTML = `
                            <h3>✅ Resultado da Consulta</h3>
                            <p><strong>Município:</strong> ${data.municipio}</p>
                            <p><strong>Serviço:</strong> ${data.servico_encontrado}</p>
                            <p><strong>Item LC 116/2003:</strong> ${data.item_lc116}</p>
                            <p><strong>Descrição:</strong> ${data.descricao}</p>
                            <p><strong>Regra Aplicável:</strong> ${data.regra}</p>
                        `;
                    } else {
                        resultado.className = 'resultado erro';
                        resultado.innerHTML = `
                            <h3>❌ Erro na Consulta</h3>
                            <p>${data.erro}</p>
                        `;
                    }
                    
                    resultado.style.display = 'block';
                } catch (error) {
                    resultado.className = 'resultado erro';
                    resultado.innerHTML = `
                        <h3>❌ Erro de Conexão</h3>
                        <p>Erro ao processar a solicitação. Tente novamente.</p>
                    `;
                    resultado.style.display = 'block';
                }
            });
        </script>
    </body>
    </html>
    '''

@app.route('/consultar', methods=['POST'])
def consultar():
    """Endpoint para consulta de ISS"""
    try:
        servico = request.form.get('servico', '').strip()
        municipio = request.form.get('municipio', '').strip()
        
        if not servico or not municipio:
            return jsonify({
                'sucesso': False,
                'erro': 'Serviço e município são obrigatórios'
            })
        
        resultado = buscar_servico(servico)
        
        if resultado:
            return jsonify({
                'sucesso': True,
                'municipio': municipio,
                'servico_encontrado': servico,
                'item_lc116': resultado['item'],
                'descricao': resultado['descricao'],
                'regra': resultado['regra']
            })
        else:
            return jsonify({
                'sucesso': False,
                'erro': 'Serviço não encontrado na LC 116/2003. Tente palavras como: desenvolvimento, consultoria, design, marketing, manutenção'
            })
            
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': f'Erro interno: {str(e)}'
        })

@app.route('/api/servicos')
def listar_servicos():
    """API para listar todos os serviços"""
    try:
        servicos = []
        for chave, dados in SERVICOS_LC116.items():
            servicos.append({
                'palavra_chave': chave,
                'item': dados['item'],
                'descricao': dados['descricao'],
                'regra': dados['regra']
            })
        
        return jsonify({
            'sucesso': True,
            'total': len(servicos),
            'servicos': servicos
        })
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': f'Erro ao listar serviços: {str(e)}'
        })

# Para compatibilidade com Vercel
if __name__ == '__main__':
    app.run(debug=False)