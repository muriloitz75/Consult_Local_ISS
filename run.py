import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Configurações do servidor baseadas no ambiente
    host = os.getenv('HOST', '127.0.0.1')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(host=host, port=port, debug=debug, threaded=True)