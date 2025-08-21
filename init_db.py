#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de inicialização do banco de dados
Cria as tabelas e popula com dados iniciais da LC 116/2003
"""

from app import create_app, db
from app.models import Servico, Regra
from config import config
import os

def init_database():
    """Inicializa o banco de dados com dados da LC 116/2003"""
    
    config_name = os.getenv('FLASK_CONFIG') or 'default'
    app = create_app(config_name)
    
    # Inicializar configurações específicas da aplicação
    config[config_name].init_app(app)
    
    with app.app_context():
        # Criar todas as tabelas
        db.create_all()
        
        # Limpar dados existentes e recriar
        db.drop_all()
        db.create_all()
        print("Banco de dados recriado. Iniciando população com dados ordenados...")
        
        # Lista completa de serviços da LC 116/2003 em ordem sequencial
        servicos_exemplo = [
            # 1 – Serviços de informática e congêneres
            {'codigo': '1.01', 'descricao': 'Análise e desenvolvimento de sistemas.'},
            {'codigo': '1.02', 'descricao': 'Programação.'},
            {'codigo': '1.03', 'descricao': 'Processamento, armazenamento ou hospedagem de dados, textos, imagens, vídeos, páginas eletrônicas, aplicativos e sistemas de informação, entre outros formatos, e congêneres.'},
            {'codigo': '1.04', 'descricao': 'Elaboração de programas de computadores, inclusive de jogos eletrônicos, independentemente da arquitetura construtiva da máquina em que o programa será executado, incluindo tablets, smartphones e congêneres.'},
            {'codigo': '1.05', 'descricao': 'Licenciamento ou cessão de direito de uso de programas de computação.'},
            {'codigo': '1.06', 'descricao': 'Assessoria e consultoria em informática.'},
            {'codigo': '1.07', 'descricao': 'Suporte técnico em informática, inclusive instalação, configuração e manutenção de programas de computação e bancos de dados.'},
            {'codigo': '1.08', 'descricao': 'Planejamento, confecção, manutenção e atualização de páginas eletrônicas.'},
            {'codigo': '1.09', 'descricao': 'Disponibilização, sem cessão definitiva, de conteúdos de áudio, vídeo, imagem e texto por meio da internet, respeitada a imunidade de livros, jornais e periódicos (exceto a distribuição de conteúdos pelas prestadoras de Serviço de Acesso Condicionado, de que trata a Lei no 12.485, de 12 de setembro de 2011, sujeita ao ICMS).'},
            
            # 2 – Serviços de pesquisas e desenvolvimento de qualquer natureza
            {'codigo': '2.01', 'descricao': 'Serviços de pesquisas e desenvolvimento de qualquer natureza.'},
            
            # 3 – Serviços prestados mediante locação, cessão de direito de uso e congêneres
             {'codigo': '3.01', 'descricao': 'Locação, cessão de direito de uso e congêneres.'},
             {'codigo': '3.02', 'descricao': 'Cessão de direito de uso de marcas e de sinais de propaganda.'},
            {'codigo': '3.03', 'descricao': 'Exploração de salões de festas, centro de convenções, escritórios virtuais, stands, quadras esportivas, estádios, ginásios, auditórios, casas de espetáculos, parques de diversões, canchas e congêneres, para realização de eventos ou negócios de qualquer natureza.'},
            {'codigo': '3.04', 'descricao': 'Locação, sublocação, arrendamento, direito de passagem ou permissão de uso, compartilhado ou não, de ferrovia, rodovia, postes, cabos, dutos e condutos de qualquer natureza.'},
            {'codigo': '3.05', 'descricao': 'Cessão de andaimes, palcos, coberturas e outras estruturas de uso temporário.'},
            
            # 4 – Serviços de saúde, assistência médica e congêneres
            {'codigo': '4.01', 'descricao': 'Medicina e biomedicina.'},
            {'codigo': '4.02', 'descricao': 'Análises clínicas, patologia, eletricidade médica, radioterapia, quimioterapia, ultra-sonografia, ressonância magnética, radiologia, tomografia e congêneres.'},
            {'codigo': '4.03', 'descricao': 'Hospitais, clínicas, laboratórios, sanatórios, manicômios, casas de saúde, prontos-socorros, ambulatórios e congêneres.'},
            {'codigo': '4.04', 'descricao': 'Instrumentação cirúrgica.'},
            {'codigo': '4.05', 'descricao': 'Acupuntura.'},
            {'codigo': '4.06', 'descricao': 'Enfermagem, inclusive serviços auxiliares.'},
            {'codigo': '4.07', 'descricao': 'Serviços farmacêuticos.'},
            {'codigo': '4.08', 'descricao': 'Terapia ocupacional, fisioterapia e fonoaudiologia.'},
            {'codigo': '4.09', 'descricao': 'Terapias de qualquer espécie destinadas ao tratamento físico, orgânico e mental.'},
            {'codigo': '4.10', 'descricao': 'Nutrição.'},
            {'codigo': '4.11', 'descricao': 'Obstetrícia.'},
            {'codigo': '4.12', 'descricao': 'Odontologia.'},
            {'codigo': '4.13', 'descricao': 'Ortóptica.'},
            {'codigo': '4.14', 'descricao': 'Próteses sob encomenda.'},
            {'codigo': '4.15', 'descricao': 'Psicanálise.'},
            {'codigo': '4.16', 'descricao': 'Psicologia.'},
            {'codigo': '4.17', 'descricao': 'Casas de repouso e de recuperação, creches, asilos e congêneres.'},
            {'codigo': '4.18', 'descricao': 'Inseminação artificial, fertilização in vitro e congêneres.'},
            {'codigo': '4.19', 'descricao': 'Bancos de sangue, leite, pele, olhos, óvulos, sêmen e congêneres.'},
            {'codigo': '4.20', 'descricao': 'Coleta de sangue, leite, tecidos, sêmen, órgãos e materiais biológicos de qualquer espécie.'},
            {'codigo': '4.21', 'descricao': 'Unidade de atendimento, assistência ou tratamento móvel e congêneres.'},
            {'codigo': '4.22', 'descricao': 'Planos de medicina de grupo ou individual e convênios para prestação de assistência médica, hospitalar, odontológica e congêneres.'},
            {'codigo': '4.23', 'descricao': 'Outros planos de saúde que se cumpram através de serviços de terceiros contratados, credenciados, cooperados ou apenas pagos pelo operador do plano mediante indicação do beneficiário.'},
            
            # 5 – Serviços de medicina e assistência veterinária e congêneres
            {'codigo': '5.01', 'descricao': 'Medicina veterinária e zootecnia.'},
            {'codigo': '5.02', 'descricao': 'Hospitais, clínicas, ambulatórios, prontos-socorros e congêneres, na área veterinária.'},
            {'codigo': '5.03', 'descricao': 'Laboratórios de análise na área veterinária.'},
            {'codigo': '5.04', 'descricao': 'Inseminação artificial, fertilização in vitro e congêneres.'},
            {'codigo': '5.05', 'descricao': 'Bancos de sangue e de órgãos e congêneres.'},
            {'codigo': '5.06', 'descricao': 'Coleta de sangue, leite, tecidos, sêmen, órgãos e materiais biológicos de qualquer espécie.'},
            {'codigo': '5.07', 'descricao': 'Unidade de atendimento, assistência ou tratamento móvel e congêneres.'},
            {'codigo': '5.08', 'descricao': 'Guarda, tratamento, amestramento, embelezamento, alojamento e congêneres.'},
            {'codigo': '5.09', 'descricao': 'Planos de atendimento e assistência médico-veterinária.'},
            
            # 6 – Serviços de cuidados pessoais, estética, atividades físicas e congêneres
             {'codigo': '6.01', 'descricao': 'Barbearia, cabeleireiros, manicuros, pedicuros e congêneres.'},
             {'codigo': '6.02', 'descricao': 'Esteticistas, tratamento de pele, depilação e congêneres.'},
             {'codigo': '6.03', 'descricao': 'Banhos, duchas, sauna, massagens e congêneres.'},
             {'codigo': '6.04', 'descricao': 'Ginástica, dança, esportes, natação, artes marciais e demais atividades físicas.'},
             {'codigo': '6.05', 'descricao': 'Centros de emagrecimento, spa e congêneres.'},
             {'codigo': '6.06', 'descricao': 'Aplicação de tatuagens, piercings e congêneres.'},
             
             # 7 – Serviços relativos a engenharia, arquitetura, geologia, urbanismo, construção civil, manutenção, limpeza, meio ambiente, saneamento e congêneres
             {'codigo': '7.01', 'descricao': 'Engenharia, agronomia, agrimensura, arquitetura, geologia, urbanismo, paisagismo e congêneres.'},
             {'codigo': '7.02', 'descricao': 'Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos.'},
             {'codigo': '7.03', 'descricao': 'Elaboração de planos diretores, estudos de viabilidade, estudos organizacionais e outros, relacionados com obras e serviços de engenharia; elaboração de anteprojetos, projetos básicos e projetos executivos para trabalhos de engenharia.'},
             {'codigo': '7.04', 'descricao': 'Demolição.'},
             {'codigo': '7.05', 'descricao': 'Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres.'},
             {'codigo': '7.06', 'descricao': 'Colocação e instalação de tapetes, carpetes, assoalhos, cortinas, revestimentos de parede, vidros, divisórias, placas de gesso e congêneres, com material fornecido pelo tomador do serviço.'},
             {'codigo': '7.07', 'descricao': 'Recuperação, raspagem, polimento e lustração de pisos e congêneres.'},
             {'codigo': '7.08', 'descricao': 'Calafetação.'},
             {'codigo': '7.09', 'descricao': 'Varrição, coleta, remoção, incineração, tratamento, reciclagem, separação e destinação final de lixo, rejeitos e outros resíduos quaisquer.'},
             {'codigo': '7.10', 'descricao': 'Limpeza, manutenção e conservação de vias e logradouros públicos, imóveis, chaminés, piscinas, parques, jardins e congêneres.'},
             {'codigo': '7.11', 'descricao': 'Decoração e jardinagem, inclusive corte e poda de árvores.'},
             {'codigo': '7.12', 'descricao': 'Controle e tratamento de efluentes de qualquer natureza e de agentes físicos, químicos e biológicos.'},
             {'codigo': '7.13', 'descricao': 'Dedetização, desinfecção, desinsetização, imunização, higienização, desratização, pulverização e congêneres.'},
             {'codigo': '7.14', 'descricao': 'Fornecimento de equipamentos para demolição e escavação com operadores.'},
             {'codigo': '7.15', 'descricao': 'Fornecimento de equipamentos para construção civil com operadores.'},
             {'codigo': '7.16', 'descricao': 'Florestamento, reflorestamento, semeadura, adubação e congêneres.'},
             {'codigo': '7.17', 'descricao': 'Escoramento, contenção de encostas e serviços congêneres.'},
             {'codigo': '7.18', 'descricao': 'Limpeza e dragagem de rios, portos, canais, baías, lagos, lagoas, represas, açudes e congêneres.'},
             {'codigo': '7.19', 'descricao': 'Acompanhamento e fiscalização da execução de obras de engenharia, arquitetura e urbanismo.'},
             {'codigo': '7.20', 'descricao': 'Aerofotogrametria (inclusive interpretação), cartografia, mapeamento, levantamentos topográficos, batimétricos, geográficos, geodésicos, geológicos, geofísicos e congêneres.'},
             {'codigo': '7.21', 'descricao': 'Pesquisa, perfuração, cimentação, mergulho, perfilagem, concretação, testemunhagem, pescaria, estimulação e outros serviços relacionados com a exploração e explotação de petróleo, gás natural e de outros recursos minerais.'},
             {'codigo': '7.22', 'descricao': 'Nucleação e bombardeamento de nuvens e congêneres.'},
             
             # 8 – Serviços de educação, ensino, orientação pedagógica e educacional, instrução, treinamento e avaliação pessoal de qualquer grau ou natureza
             {'codigo': '8.01', 'descricao': 'Ensino regular pré-escolar, fundamental, médio e superior.'},
             {'codigo': '8.02', 'descricao': 'Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza.'},
             
             # 9 – Serviços relativos a hospedagem, turismo, viagens e congêneres
             {'codigo': '9.01', 'descricao': 'Hospedagem de qualquer natureza em hotéis, apart-service condominiais, flat, apart-hotéis, hotéis residência, residence-service, suite service, hotelaria marítima, motéis, pensões e congêneres; ocupação por temporada com fornecimento de serviço.'},
             {'codigo': '9.02', 'descricao': 'Agenciamento, organização, promoção, intermediação e execução de programas de turismo, passeios, viagens, excursões, hospedagens e congêneres.'},
             {'codigo': '9.03', 'descricao': 'Guias de turismo.'},
             
             # 10 – Serviços de intermediação e congêneres
             {'codigo': '10.01', 'descricao': 'Agenciamento, corretagem ou intermediação de câmbio, de seguros, de cartões de crédito, de planos de saúde e de planos de previdência privada.'},
             {'codigo': '10.02', 'descricao': 'Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer.'},
             {'codigo': '10.03', 'descricao': 'Agenciamento, corretagem ou intermediação de direitos de propriedade industrial, artística ou literária.'},
             {'codigo': '10.04', 'descricao': 'Agenciamento, corretagem ou intermediação de contratos de arrendamento mercantil (leasing), de franquia (franchising) e de faturização (factoring).'},
             {'codigo': '10.05', 'descricao': 'Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios.'},
             {'codigo': '10.06', 'descricao': 'Agenciamento marítimo.'},
             {'codigo': '10.07', 'descricao': 'Agenciamento de notícias.'},
             {'codigo': '10.08', 'descricao': 'Agenciamento de publicidade e propaganda, inclusive o agenciamento de veiculação por qualquer meio.'},
             {'codigo': '10.09', 'descricao': 'Representação de qualquer natureza, inclusive comercial.'},
             {'codigo': '10.10', 'descricao': 'Distribuição de bens de terceiros.'},
             
             # 11 – Serviços de guarda, estacionamento, armazenamento, vigilância e congêneres
             {'codigo': '11.01', 'descricao': 'Guarda e estacionamento de veículos terrestres, aéreos e aquáticos.'},
             {'codigo': '11.02', 'descricao': 'Vigilância, segurança ou monitoramento de bens e pessoas.'},
             {'codigo': '11.03', 'descricao': 'Escolta, inclusive de veículos e cargas.'},
             {'codigo': '11.04', 'descricao': 'Armazenamento, depósito, carga, descarga, arrumação e guarda de bens de qualquer espécie.'},
             
             # 12 – Serviços de diversões, lazer, entretenimento e congêneres
             {'codigo': '12.01', 'descricao': 'Espetáculos teatrais, exibições cinematográficas, espetáculos circenses, programas de auditório, espetáculos de dança, bailes, óperas, concertos, recitais, festivais e congêneres.'},
             {'codigo': '12.02', 'descricao': 'Exibições desportivas e competições de qualquer natureza ou modalidade.'},
             {'codigo': '12.03', 'descricao': 'Parques de diversões, centros de lazer e congêneres.'},
             {'codigo': '12.04', 'descricao': 'Boates, taxi-dancing e congêneres.'},
             {'codigo': '12.05', 'descricao': 'Exploração de jogos de sinuca, bilhar, snooker, boliche, bocha, tênis de mesa, fliperamas e congêneres.'},
             {'codigo': '12.06', 'descricao': 'Discotecas, danceterias, salões de dança, bailes, clubes dançantes, gafieiras e congêneres.'},
             {'codigo': '12.07', 'descricao': 'Casas de jogos, bingos, cassinos e congêneres.'},
             {'codigo': '12.08', 'descricao': 'Corridas e competições de animais.'},
             {'codigo': '12.09', 'descricao': 'Exploração de apostas e jogos.'},
             {'codigo': '12.10', 'descricao': 'Golfe, inclusive aluguel de equipamentos.'},
             {'codigo': '12.11', 'descricao': 'Jogos eletrônicos ou não, inclusive locação de máquinas.'},
             {'codigo': '12.12', 'descricao': 'Corridas de veículos ou embarcações.'},
             {'codigo': '12.13', 'descricao': 'Outros jogos, apostas, loterias e congêneres.'},
             
             # 13 – Serviços relativos a fonografia, fotografia, cinematografia e reprografia
             {'codigo': '13.01', 'descricao': 'Serviços de fonografia e gravação de sons, inclusive trucagem, dublagem, mixagem e congêneres.'},
             {'codigo': '13.02', 'descricao': 'Fotografia e cinematografia, inclusive revelação, ampliação, cópia, reprodução, trucagem e congêneres.'},
             {'codigo': '13.03', 'descricao': 'Reprografia, microfilmagem e digitalização.'},
             {'codigo': '13.04', 'descricao': 'Composição gráfica, fotocomposição, clicheria, zincografia, litografia, fotolitografia.'},
             {'codigo': '13.05', 'descricao': 'Gravação de discos, fitas, filmes, cassetes, cartuchos, inclusive locação.'},
             
             # 14 – Serviços relativos a bens de terceiros
             {'codigo': '14.01', 'descricao': 'Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto.'},
             {'codigo': '14.02', 'descricao': 'Assistência técnica.'},
             {'codigo': '14.03', 'descricao': 'Recondicionamento de motores.'},
             {'codigo': '14.04', 'descricao': 'Recauchutagem ou regeneração de pneus.'},
             {'codigo': '14.05', 'descricao': 'Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, polimento, plastificação e congêneres, de objetos quaisquer.'},
             {'codigo': '14.06', 'descricao': 'Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido.'},
             {'codigo': '14.07', 'descricao': 'Colocação de molduras e congêneres.'},
             {'codigo': '14.08', 'descricao': 'Encadernação, gravação e douração de livros, revistas e congêneres.'},
             {'codigo': '14.09', 'descricao': 'Alfaiataria e costura, quando o material for fornecido pelo usuário final, exceto aviamento.'},
             {'codigo': '14.10', 'descricao': 'Tinturaria e lavanderia.'},
             {'codigo': '14.11', 'descricao': 'Tapeçaria e reforma de estofamentos em geral.'},
             {'codigo': '14.12', 'descricao': 'Funilaria e lanternagem.'},
             {'codigo': '14.13', 'descricao': 'Carpintaria e serralheria.'},
             
             # 15 – Serviços relacionados ao setor bancário ou financeiro
             {'codigo': '15.01', 'descricao': 'Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres.'},
             {'codigo': '15.02', 'descricao': 'Abertura de contas em geral, inclusive conta-corrente, conta de investimentos e aplicação e caderneta de poupança, no País e no exterior, bem como a manutenção das referidas contas ativas e inativas.'},
             {'codigo': '15.03', 'descricao': 'Locação e manutenção de cofres particulares, de terminais eletrônicos, de terminais de atendimento e de bens e equipamentos em geral.'},
             {'codigo': '15.04', 'descricao': 'Fornecimento ou emissão de atestados, certidões e congêneres.'},
             {'codigo': '15.05', 'descricao': 'Cadastro, elaboração de ficha cadastral, renovação cadastral e congêneres, inclusão ou exclusão no Cadastro de Emitentes de Cheques sem Fundos – CCF ou em quaisquer outros bancos cadastrais.'},
             {'codigo': '15.06', 'descricao': 'Emissão, reemissão e fornecimento de avisos, comprovantes e documentos em geral; abono de firmas; coleta e entrega de documentos, bens e valores; comunicação com outra agência ou com a administração central; licenciamento eletrônico de veículos; transferência de veículos; agenciamento fiduciário ou depositário; devolução de bens em custódia.'},
             {'codigo': '15.07', 'descricao': 'Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas; acesso a outro banco e a rede compartilhada; fornecimento de saldo, extrato e demais informações relativas a contas em geral, por qualquer meio ou processo.'},
             {'codigo': '15.08', 'descricao': 'Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito; estudo, análise e avaliação de operações de crédito; emissão, concessão, alteração ou contratação de aval, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins.'},
             {'codigo': '15.09', 'descricao': 'Arrendamento mercantil (leasing) de quaisquer bens, inclusive cessão de direitos e obrigações, substituição de garantia, alteração, cancelamento e registro de contrato, e demais serviços relacionados ao arrendamento mercantil (leasing).'},
             {'codigo': '15.10', 'descricao': 'Serviços relacionados a cobranças, recebimentos ou pagamentos em geral, de títulos quaisquer, de contas ou carnês, de câmbio, de tributos e por conta de terceiros, inclusive os efetuados por meio eletrônico, automático ou por máquinas de atendimento; fornecimento de posição de cobrança, recebimento ou pagamento; emissão de carnês, fichas de compensação, impressos e documentos em geral.'},
             {'codigo': '15.11', 'descricao': 'Devolução de títulos, protesto de títulos, sustação de protesto, manutenção de títulos, reapresentação de títulos, e demais serviços a eles relacionados.'},
             {'codigo': '15.12', 'descricao': 'Custódia em geral, inclusive de títulos e valores mobiliários.'},
             {'codigo': '15.13', 'descricao': 'Serviços relacionados a operações de câmbio em geral, edição, alteração, prorrogação, cancelamento e baixa de contratos de câmbio; emissão de registro de exportação ou de crédito; cobrança ou depósito no exterior; emissão, fornecimento e cancelamento de cheques de viagem; fornecimento, transferência, cancelamento e demais serviços relativos a carta de crédito de importação, exportação e garantias recebidas; envio e recebimento de mensagens em geral relacionadas a operações de câmbio.'},
             {'codigo': '15.14', 'descricao': 'Fornecimento, emissão, reemissão, renovação e manutenção de cartão magnético, cartão de crédito, cartão de débito, cartão salário e congêneres.'},
             {'codigo': '15.15', 'descricao': 'Compensação de cheques e títulos quaisquer; serviços relacionados a depósito, inclusive depósito identificado, a saque de contas quaisquer, por qualquer meio ou processo, inclusive em terminais eletrônicos e de atendimento.'},
             {'codigo': '15.16', 'descricao': 'Emissão, reemissão, liquidação, alteração, cancelamento e baixa de ordens de pagamento, ordens de crédito e similares, por qualquer meio ou processo; serviços relacionados à transferência de valores, dados, fundos, pagamentos e similares, inclusive entre contas em geral.'},
             {'codigo': '15.17', 'descricao': 'Emissão, fornecimento, devolução, sustação, cancelamento e oposição de cheques quaisquer, avulso ou por talão.'},
             {'codigo': '15.18', 'descricao': 'Serviços relacionados a crédito imobiliário, avaliação e vistoria de imóvel ou obra, análise técnica e jurídica, emissão, reemissão, alteração, transferência e renegociação de contrato, emissão e reemissão do termo de quitação e demais serviços relacionados a crédito imobiliário.'},
             
             # 16 – Serviços de transporte de natureza municipal
             {'codigo': '16.01', 'descricao': 'Serviços de transporte de natureza municipal.'},
             
             # 17 – Serviços de apoio técnico, administrativo, jurídico, contábil, comercial e congêneres
             {'codigo': '17.01', 'descricao': 'Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares.'},
             {'codigo': '17.02', 'descricao': 'Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infraestrutura administrativa e congêneres.'},
             {'codigo': '17.03', 'descricao': 'Planejamento, coordenação, programação ou organização técnica, financeira ou administrativa.'},
             {'codigo': '17.04', 'descricao': 'Recrutamento, agenciamento, seleção e colocação de mão-de-obra.'},
             {'codigo': '17.05', 'descricao': 'Fornecimento de mão-de-obra, mesmo em caráter temporário, inclusive de empregados ou trabalhadores, avulsos ou temporários, contratados pelo prestador de serviço.'},
             {'codigo': '17.06', 'descricao': 'Propaganda e publicidade, inclusive promoção de vendas, planejamento de campanhas ou sistemas de publicidade, elaboração de desenhos, textos e demais materiais publicitários.'},
             {'codigo': '17.07', 'descricao': 'Factoring.'},
             {'codigo': '17.08', 'descricao': 'Franquia (franchising).'},
             {'codigo': '17.09', 'descricao': 'Perícias, laudos, exames técnicos e análises técnicas.'},
             {'codigo': '17.10', 'descricao': 'Planejamento, organização e administração de feiras, exposições, congressos e congêneres.'},
             {'codigo': '17.11', 'descricao': 'Organização de festas e recepções; bufê (exceto o fornecimento de alimentação e bebidas, que fica sujeito ao ICMS).'},
             {'codigo': '17.12', 'descricao': 'Administração em geral, inclusive de bens e negócios de terceiros.'},
             {'codigo': '17.13', 'descricao': 'Leilão e congêneres.'},
             {'codigo': '17.14', 'descricao': 'Advocacia.'},
             {'codigo': '17.15', 'descricao': 'Arbitragem de qualquer espécie, inclusive jurídica.'},
             {'codigo': '17.16', 'descricao': 'Auditoria.'},
             {'codigo': '17.17', 'descricao': 'Análise de organização e métodos.'},
             {'codigo': '17.18', 'descricao': 'Atuária e cálculos técnicos de qualquer natureza.'},
             {'codigo': '17.19', 'descricao': 'Contabilidade, inclusive serviços técnicos e auxiliares.'},
             {'codigo': '17.20', 'descricao': 'Consultoria e assessoria econômica ou financeira.'},
             {'codigo': '17.21', 'descricao': 'Estatística.'},
             {'codigo': '17.22', 'descricao': 'Cobrança em geral.'},
             {'codigo': '17.23', 'descricao': 'Assessoria, análise, avaliação, atendimento, consulta, cadastro, seleção, gerenciamento de informações, administração de contas a receber ou a pagar e em geral, relacionados a operações de fatorização (factoring).'},
             {'codigo': '17.24', 'descricao': 'Apresentação de palestras, conferências, seminários e congêneres.'},
             {'codigo': '17.25', 'descricao': 'Inserção de textos, desenhos e outros materiais de propaganda e publicidade, em qualquer meio (exceto em livros, jornais, periódicos e nas modalidades de serviços de radiodifusão sonora e de sons e imagens de recepção livre e gratuita).'},
             
             # 18 – Serviços de regulação de sinistros vinculados a contratos de seguros; inspeção e avaliação de riscos para cobertura de contratos de seguros; prevenção e gerência de riscos seguráveis e congêneres
             {'codigo': '18.01', 'descricao': 'Serviços de regulação de sinistros vinculados a contratos de seguros; inspeção e avaliação de riscos para cobertura de contratos de seguros; prevenção e gerência de riscos seguráveis e congêneres.'},
             
             # 19 – Serviços de distribuição e venda de bilhetes e demais produtos de loteria, bingos, cartões, pules ou cupons de apostas, sorteios, prêmios, inclusive os decorrentes de títulos de capitalização e congêneres
             {'codigo': '19.01', 'descricao': 'Serviços de distribuição e venda de bilhetes e demais produtos de loteria, bingos, cartões, pules ou cupons de apostas, sorteios, prêmios, inclusive os decorrentes de títulos de capitalização e congêneres.'},
             
             # 20 – Serviços portuários, aeroportuários, ferroportuários, de terminais rodoviários, ferroviários e metroviários
             {'codigo': '20.01', 'descricao': 'Serviços portuários, ferroportuários, utilização de porto, movimentação de passageiros, reboque de embarcações, rebocador escoteiro, atracação, desatracação, serviços de praticagem, capatazia, armazenagem de qualquer natureza, serviços acessórios, movimentação de mercadorias, serviços de apoio marítimo, de movimentação ao largo, serviços de armadores, estiva, conferência, logística e congêneres.'},
             {'codigo': '20.02', 'descricao': 'Serviços aeroportuários, utilização de aeroporto, movimentação de passageiros, armazenagem de qualquer natureza, capatazia, movimentação de aeronaves, serviços de apoio aeroportuários, serviços acessórios, movimentação de mercadorias, logística e congêneres.'},
             {'codigo': '20.03', 'descricao': 'Serviços de terminais rodoviários, ferroviários, metroviários, movimentação de passageiros, mercadorias, inclusive suas operações, logística e congêneres.'},
             
             # 21 – Serviços de registros públicos, cartorários e notariais
             {'codigo': '21.01', 'descricao': 'Serviços de registros públicos, cartorários e notariais.'},
             
             # 22 – Serviços de exploração de rodovia
             {'codigo': '22.01', 'descricao': 'Serviços de exploração de rodovia mediante cobrança de preço ou pedágio dos usuários, envolvendo execução de serviços de conservação, manutenção, melhoramentos para adequação de capacidade e segurança de trânsito, operação, monitoração, assistência aos usuários e outros serviços definidos em contratos, atos de concessão ou de permissão ou em normas oficiais.'},
             
             # 23 – Serviços de programação e comunicação visual, desenho industrial e congêneres
             {'codigo': '23.01', 'descricao': 'Serviços de programação e comunicação visual, desenho industrial e congêneres.'},
             
             # 24 – Serviços de chaveiros, confecção de carimbos, placas, sinalização visual, banners, adesivos e congêneres
             {'codigo': '24.01', 'descricao': 'Serviços de chaveiros, confecção de carimbos, placas, sinalização visual, banners, adesivos e congêneres.'},
             
             # 25 – Serviços funerários
             {'codigo': '25.01', 'descricao': 'Funerais, inclusive fornecimento de caixão, urna ou esquifes; aluguel de capela; transporte do corpo cadavérico; fornecimento de flores, coroas e outros paramentos; desembaraço de certidão de óbito; fornecimento de véu, essa e outros adornos; embalsamento, embelezamento, conservação ou restauração de cadáveres.'},
             {'codigo': '25.02', 'descricao': 'Translado intramunicipal e cremação de corpos e partes de corpos cadavéricos.'},
             {'codigo': '25.03', 'descricao': 'Planos ou convênio funerários.'},
             {'codigo': '25.04', 'descricao': 'Manutenção e conservação de jazigos e cemitérios.'},
             {'codigo': '25.05', 'descricao': 'Cessão de uso de espaços em cemitérios para sepultamento.'},
             
             # 26 – Serviços de coleta, remessa ou entrega de correspondências, documentos, objetos, bens ou valores, inclusive pelos correios e suas agências franqueadas; courrier e congêneres
             {'codigo': '26.01', 'descricao': 'Serviços de coleta, remessa ou entrega de correspondências, documentos, objetos, bens ou valores, inclusive pelos correios e suas agências franqueadas; courrier e congêneres.'},
             
             # 27 – Serviços de assistência social
             {'codigo': '27.01', 'descricao': 'Serviços de assistência social.'},
             
             # 28 – Serviços de avaliação de bens e serviços de qualquer natureza
             {'codigo': '28.01', 'descricao': 'Serviços de avaliação de bens e serviços de qualquer natureza.'},
             
             # 29 – Serviços de biblioteconomia
             {'codigo': '29.01', 'descricao': 'Serviços de biblioteconomia.'},
             
             # 30 – Serviços de biologia, biotecnologia e química
             {'codigo': '30.01', 'descricao': 'Serviços de biologia, biotecnologia e química.'},
             
             # 31 – Serviços técnicos em edificações, eletrônica, eletrotécnica, mecânica, telecomunicações e congêneres
             {'codigo': '31.01', 'descricao': 'Serviços técnicos em edificações, eletrônica, eletrotécnica, mecânica, telecomunicações e congêneres.'},
             
             # 32 – Serviços de desenhos técnicos
             {'codigo': '32.01', 'descricao': 'Serviços de desenhos técnicos.'},
             
             # 33 – Serviços de desembaraço aduaneiro, comissários, despachantes e congêneres
             {'codigo': '33.01', 'descricao': 'Serviços de desembaraço aduaneiro, comissários, despachantes e congêneres.'},
             
             # 34 – Serviços de investigações particulares, detetives e congêneres
             {'codigo': '34.01', 'descricao': 'Serviços de investigações particulares, detetives e congêneres.'},
             
             # 35 – Serviços de reportagem, assessoria de imprensa, jornalismo e relações públicas
             {'codigo': '35.01', 'descricao': 'Serviços de reportagem, assessoria de imprensa, jornalismo e relações públicas.'},
             
             # 36 – Serviços de meteorologia
             {'codigo': '36.01', 'descricao': 'Serviços de meteorologia.'},
             
             # 37 – Serviços de artistas, atletas, modelos e manequins
             {'codigo': '37.01', 'descricao': 'Serviços de artistas, atletas, modelos e manequins.'},
             
             # 38 – Serviços de museologia
             {'codigo': '38.01', 'descricao': 'Serviços de museologia.'},
             
             # 39 – Serviços de ourivesaria, lapidação, gravação e congêneres
             {'codigo': '39.01', 'descricao': 'Serviços de ourivesaria, lapidação, gravação e congêneres.'},
             
             # 40 – Serviços relativos a obras de arte sob encomenda
             {'codigo': '40.01', 'descricao': 'Obras de arte sob encomenda.'}
         ]
        
        # Inserir serviços
        for servico_data in servicos_exemplo:
            servico = Servico(
                codigo=servico_data['codigo'],
                descricao=servico_data['descricao']
            )
            db.session.add(servico)
        
        # Commit dos serviços
        db.session.commit()
        
        # Regras específicas do Art. 3º da LC 116/2003
        regras_exemplo = [
            {
                'servico_codigo': '3.05',  # Instalação de andaimes
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso I da LC 116/2003 - Construção civil'
            },
            {
                'servico_codigo': '7.02',  # Execução, por administração, empreitada ou subempreitada, de obras de construção civil
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso III da LC 116/2003 - Execução da obra'
            },
            {
                'servico_codigo': '7.04',  # Demolição
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso IV da LC 116/2003 - Demolição'
            },
            {
                'servico_codigo': '7.05',  # Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso V da LC 116/2003 - Edificações em geral'
            },
            {
                'servico_codigo': '7.09',  # Varredura, coleta, remoção, incineração, tratamento, reciclagem, separação e destinação final de lixo, rejeitos e outros resíduos quaisquer
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso VI da LC 116/2003 - Limpeza, manutenção e conservação de vias e logradouros públicos'
            },
            {
                'servico_codigo': '7.10',  # Limpeza e dragagem de rios, portos, canais, baías, lagos, lagoas, represas, açudes e congêneres
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso VI da LC 116/2003 - Limpeza, manutenção e conservação de vias e logradouros públicos'
            },
            {
                'servico_codigo': '7.11',  # Decoração e jardinagem, inclusive corte e poda de árvores
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso VI da LC 116/2003 - Limpeza, manutenção e conservação de vias e logradouros públicos'
            },
            {
                'servico_codigo': '11.01',  # Guarda e estacionamento de veículos terrestres automotores, de aeronaves e de embarcações
                'local_recolhimento': 'Município onde o bem estiver guardado',
                'justificativa_legal': 'Art. 3º, inciso XV da LC 116/2003 - Guarda e depósito de bens'
            },
            {
                'servico_codigo': '11.02',  # Vigilância, segurança ou monitoramento de bens e pessoas
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XVI da LC 116/2003 - Vigilância, segurança ou monitoramento'
            },
            {
                'servico_codigo': '15.09',  # Arrendamento mercantil (leasing)
                'local_recolhimento': 'Município onde estiver o bem arrendado',
                'justificativa_legal': 'Art. 3º, inciso XVII da LC 116/2003 - Arrendamento mercantil'
            },
            {
                'servico_codigo': '16.01',  # Serviços de transporte de natureza municipal
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XVIII da LC 116/2003 - Transporte de natureza municipal'
            },
            {
                'servico_codigo': '12.01',  # Espetáculos teatrais
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.02',  # Exibições cinematográficas
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.03',  # Espetáculos circenses
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.04',  # Programas de auditório
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.05',  # Parques de diversões, centros de lazer e congêneres
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.06',  # Boates, taxi-dancing e congêneres
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.07',  # Shows, ballet, danças, desfiles, bailes, óperas, concertos, recitais, festivais e congêneres
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.08',  # Feiras, exposições, congressos e congêneres
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.09',  # Bilhares, boliches, diversões eletrônicas ou não
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.10',  # Corridas e competições de animais
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.11',  # Competições esportivas ou de destreza física ou intelectual
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.12',  # Execução de música
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.13',  # Produção, mediante ou sem encomenda prévia, de eventos, espetáculos, entrevistas, shows, ballet, danças, desfiles, bailes, teatros, óperas, concertos, recitais, festivais e congêneres
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.14',  # Fornecimento de música para ambientes fechados ou não, mediante transmissão por qualquer processo
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.15',  # Desfiles de blocos carnavalescos ou folclóricos, trios elétricos e congêneres
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.16',  # Exibição de filmes, entrevistas, musicais, espetáculos, shows, concertos, desfiles, óperas, competições esportivas, de destreza intelectual ou congêneres
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIX da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            {
                'servico_codigo': '12.17',  # Recreação e animação, inclusive em festas e eventos de qualquer natureza
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XVIII da LC 116/2003 - Diversões, lazer, entretenimento e congêneres'
            },
            # Regras adicionais baseadas na LC 116/2003 completa
            {
                'servico_codigo': '7.12',  # Controle e tratamento do efluente
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso IX da LC 116/2003 - Controle e tratamento do efluente'
            },
            {
                'servico_codigo': '7.16',  # Florestamento, reflorestamento, semeadura, adubação
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XII da LC 116/2003 - Florestamento e congêneres'
            },
            {
                'servico_codigo': '7.17',  # Escoramento, contenção de encostas
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIII da LC 116/2003 - Escoramento, contenção de encostas'
            },
            {
                'servico_codigo': '7.18',  # Limpeza e dragagem
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XIV da LC 116/2003 - Limpeza e dragagem'
            },
            {
                'servico_codigo': '7.19',  # Acompanhamento e fiscalização da execução de obras
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso III da LC 116/2003 - Execução da obra'
            },
            {
                'servico_codigo': '11.04',  # Armazenamento, depósito, carga, descarga, arrumação e guarda
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XVII da LC 116/2003 - Armazenamento, depósito e guarda'
            },
            {
                'servico_codigo': '17.05',  # Fornecimento de mão-de-obra
                'local_recolhimento': 'Município do estabelecimento tomador',
                'justificativa_legal': 'Art. 3º, inciso XX da LC 116/2003 - Fornecimento de mão-de-obra'
            },
            {
                'servico_codigo': '17.10',  # Planejamento, organização e administração de feiras, exposições, congressos
                'local_recolhimento': 'Município onde se efetuar a prestação',
                'justificativa_legal': 'Art. 3º, inciso XXI da LC 116/2003 - Planejamento de feiras e congressos'
            },
            {
                'servico_codigo': '20.01',  # Serviços portuários, aeroportuários, ferroportuários, de terminais rodoviários, ferroviários e metroviários
                'local_recolhimento': 'Município do porto, aeroporto ou terminal',
                'justificativa_legal': 'Art. 3º, inciso XXII da LC 116/2003 - Serviços portuários e aeroportuários'
            },
            {
                'servico_codigo': '4.22',  # Serviços de franquia (franchising)
                'local_recolhimento': 'Município do domicílio do tomador',
                'justificativa_legal': 'Art. 3º, inciso XXIII da LC 116/2003 - Franquia'
            },
            {
                'servico_codigo': '4.23',  # Serviços de intermediação e congêneres
                'local_recolhimento': 'Município do domicílio do tomador',
                'justificativa_legal': 'Art. 3º, inciso XXIII da LC 116/2003 - Intermediação'
            },
            {
                'servico_codigo': '5.09',  # Serviços relacionados a cobranças, recebimentos ou pagamentos
                'local_recolhimento': 'Município do domicílio do tomador',
                'justificativa_legal': 'Art. 3º, inciso XXIII da LC 116/2003 - Cobranças e pagamentos'
            },
            {
                'servico_codigo': '15.01',  # Administração de cartão de crédito ou débito
                'local_recolhimento': 'Município do domicílio do tomador',
                'justificativa_legal': 'Art. 3º, inciso XXIV da LC 116/2003 - Administração de cartão de crédito'
            }
        ]
        
        # Inserir regras
        for regra_data in regras_exemplo:
            # Buscar o serviço pelo código
            servico = Servico.query.filter_by(codigo=regra_data['servico_codigo']).first()
            if servico:
                regra = Regra(
                    servico_id=servico.id,
                    local_recolhimento=regra_data['local_recolhimento'],
                    justificativa_legal=regra_data['justificativa_legal']
                )
                db.session.add(regra)
        
        # Commit final
        db.session.commit()
        
        print(f"Banco de dados inicializado com sucesso!")
        print(f"- {len(servicos_exemplo)} serviços inseridos")
        print(f"- {len(regras_exemplo)} regras específicas inseridas")
        print("\nPara adicionar mais serviços da LC 116/2003, edite este arquivo e execute novamente.")

if __name__ == '__main__':
    init_database()