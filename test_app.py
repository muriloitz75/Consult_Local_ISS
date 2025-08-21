#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste simples da aplicação ISS para verificar se está funcionando
"""

import sys
import os
sys.path.append('api')

from index import app, buscar_servico, SERVICOS_LC116

def test_buscar_servico():
    """Testa a função de busca de serviços"""
    print("🧪 Testando função buscar_servico...")
    
    # Teste 1: Desenvolvimento
    resultado = buscar_servico("desenvolvimento de software")
    assert resultado is not None, "Deveria encontrar serviço de desenvolvimento"
    print(f"✅ Teste 1 passou: {resultado['item']} - {resultado['descricao']}")
    
    # Teste 2: Consultoria
    resultado = buscar_servico("consultoria em TI")
    assert resultado is not None, "Deveria encontrar serviço de consultoria"
    print(f"✅ Teste 2 passou: {resultado['item']} - {resultado['descricao']}")
    
    # Teste 3: Serviço não encontrado
    resultado = buscar_servico("serviço inexistente")
    assert resultado is None, "Não deveria encontrar serviço inexistente"
    print("✅ Teste 3 passou: Serviço inexistente não foi encontrado")
    
    print("\n🎉 Todos os testes passaram!")

def test_app_routes():
    """Testa as rotas da aplicação"""
    print("\n🧪 Testando rotas da aplicação...")
    
    with app.test_client() as client:
        # Teste da página inicial
        response = client.get('/')
        assert response.status_code == 200, "Página inicial deveria retornar 200"
        assert b'Busca Assertiva ISS' in response.data, "Página deveria conter título"
        print("✅ Rota / funcionando")
        
        # Teste da API de serviços
        response = client.get('/api/servicos')
        assert response.status_code == 200, "API de serviços deveria retornar 200"
        data = response.get_json()
        assert data['sucesso'] == True, "API deveria retornar sucesso"
        assert len(data['servicos']) > 0, "API deveria retornar serviços"
        print(f"✅ Rota /api/servicos funcionando - {data['total']} serviços encontrados")
        
        # Teste da consulta
        response = client.post('/consultar', data={
            'servico': 'desenvolvimento de software',
            'municipio': 'São Paulo'
        })
        assert response.status_code == 200, "Consulta deveria retornar 200"
        data = response.get_json()
        assert data['sucesso'] == True, "Consulta deveria ser bem-sucedida"
        print(f"✅ Rota /consultar funcionando - Item: {data['item_lc116']}")
    
    print("\n🎉 Todas as rotas estão funcionando!")

if __name__ == '__main__':
    print("🚀 Iniciando testes da aplicação ISS...\n")
    
    try:
        test_buscar_servico()
        test_app_routes()
        
        print("\n" + "="*50)
        print("✅ APLICAÇÃO ESTÁ FUNCIONANDO CORRETAMENTE!")
        print("✅ Pronta para deploy na Vercel")
        print("="*50)
        
        print("\n📋 Serviços disponíveis:")
        for chave, dados in SERVICOS_LC116.items():
            print(f"  • {chave}: {dados['item']} - {dados['descricao']}")
            
    except Exception as e:
        print(f"\n❌ ERRO nos testes: {str(e)}")
        sys.exit(1)