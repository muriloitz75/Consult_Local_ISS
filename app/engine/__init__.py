from app.models import Servico, Regra
from app import db

class ISSEngine:
    """
    Motor de busca para determinar o local de recolhimento do ISS
    baseado na LC 116/2003 e suas exceções do Art. 3º
    """
    
    def __init__(self):
        self.municipios_validos = [
            'Município do Prestador',
            'Município do Tomador', 
            'Município da Execução'
        ]
    
    def validar_entrada(self, servico_id, municipio_prestador, municipio_tomador, municipio_execucao):
        """
        Valida se todos os campos obrigatórios foram preenchidos
        """
        erros = []
        
        if not servico_id:
            erros.append('Serviço deve ser selecionado')
        
        if not municipio_prestador or municipio_prestador.strip() == '':
            erros.append('Município do Prestador é obrigatório')
            
        if not municipio_tomador or municipio_tomador.strip() == '':
            erros.append('Município do Tomador é obrigatório')
            
        if not municipio_execucao or municipio_execucao.strip() == '':
            erros.append('Município da Execução é obrigatório')
        
        return erros
    
    def consultar_iss(self, servico_id, municipio_prestador, municipio_tomador, municipio_execucao):
        """
        Realiza a consulta principal para determinar o local de recolhimento do ISS
        """
        # Validar entrada
        erros = self.validar_entrada(servico_id, municipio_prestador, municipio_tomador, municipio_execucao)
        if erros:
            return {
                'sucesso': False,
                'erros': erros
            }
        
        # Buscar o serviço
        servico = Servico.query.get(servico_id)
        if not servico:
            return {
                'sucesso': False,
                'erros': ['Serviço não encontrado']
            }
        
        # Verificar se existe regra específica para este serviço
        regra = Regra.query.filter_by(servico_id=servico_id).first()
        
        if regra:
            # Aplicar regra específica do Art. 3º
            local_recolhimento = self._aplicar_regra_especifica(regra, municipio_prestador, municipio_tomador, municipio_execucao)
            justificativa = regra.justificativa_legal
        else:
            # Aplicar regra geral (Art. 3º caput - local do estabelecimento prestador)
            local_recolhimento = municipio_prestador
            justificativa = "Art. 3º, caput da LC 116/2003 - Local do estabelecimento prestador do serviço"
        
        return {
            'sucesso': True,
            'servico': servico.descricao,
            'local_recolhimento': local_recolhimento,
            'justificativa_legal': justificativa,
            'municipio_prestador': municipio_prestador,
            'municipio_tomador': municipio_tomador,
            'municipio_execucao': municipio_execucao
        }
    
    def _aplicar_regra_especifica(self, regra, municipio_prestador, municipio_tomador, municipio_execucao):
        """
        Aplica regras específicas baseadas no tipo de exceção do Art. 3º
        """
        local = regra.local_recolhimento.lower()
        
        # Regras específicas do Art. 3º da LC 116/2003
        if 'prestador' in local:
            return municipio_prestador
        elif any(termo in local for termo in ['domicílio do tomador', 'estabelecimento tomador']):
            return municipio_tomador
        elif any(termo in local for termo in ['porto, aeroporto ou terminal', 'porto', 'aeroporto', 'terminal']):
            return municipio_execucao  # Assumindo que porto/aeroporto/terminal está no município de execução
        elif 'execução' in local or 'execucao' in local or 'efetuar a prestação' in local or 'prestação' in local:
            return municipio_execucao
        elif 'bem estiver guardado' in local or 'guardado' in local:
            return municipio_execucao  # Local onde o bem está guardado
        elif 'bem arrendado' in local or 'arrendado' in local:
            return municipio_execucao  # Local onde está o bem arrendado
        elif 'tomador' in local:
            return municipio_tomador
        else:
            # Para casos não mapeados, usar município da execução como padrão
            return municipio_execucao
    
    def listar_servicos(self):
        """
        Retorna todos os serviços disponíveis para seleção ordenados numericamente
        """
        # Buscar todos os serviços
        servicos = Servico.query.all()
        
        # Ordenar numericamente considerando as partes antes e depois do ponto
        # Converte '1.01' -> (1, 1); '10.01' -> (10, 1) para ordenação correta
        def ordenar_codigo(servico):
            partes = servico.codigo.split('.')
            return (int(partes[0]), int(partes[1]))
        
        return sorted(servicos, key=ordenar_codigo)