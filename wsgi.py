#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WSGI Configuration for Production Deployment

Este arquivo é usado por servidores WSGI como Gunicorn, uWSGI, ou Apache mod_wsgi
para servir a aplicação Flask em produção.

Exemplo de uso com Gunicorn:
    gunicorn --bind 0.0.0.0:5000 --workers 4 wsgi:application

Exemplo de uso com uWSGI:
    uwsgi --http :5000 --wsgi-file wsgi.py --callable application --processes 4 --threads 2
"""

import os
import sys
from pathlib import Path

# Adiciona o diretório do projeto ao Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

# Importa a aplicação Flask
from app import create_app

# Cria a instância da aplicação
application = create_app()

if __name__ == "__main__":
    # Para teste local do WSGI
    application.run()