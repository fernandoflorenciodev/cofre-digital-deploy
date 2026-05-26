from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)

# Configuração de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Página inicial
@app.route('/')
def home():
    return jsonify({
        "message": "Cofre Digital Online!",
        "environment": os.getenv('ENVIRONMENT', 'unknown'),
        "version": os.getenv('APP_VERSION', '1.0.0')
    })

# Simulação de banco de dados
@app.route('/database')
def database_info():

    db_host = os.getenv('DB_HOST', 'localhost')
    db_user = os.getenv('DB_USER', 'user')
    db_password = os.getenv('DB_PASSWORD', 'SENHA_NAO_CONFIGURADA')

    # Nunca mostrar senha nos logs
    logger.info(f"Conectando ao banco: {db_host} com usuário: {db_user}")

    return jsonify({
        "status": "connected" if db_password != 'SENHA_NAO_CONFIGURADA' else "not_configured",
        "host": db_host,
        "user": db_user,
        "password_configured": db_password != 'SENHA_NAO_CONFIGURADA'
    })

# Simulação de API KEY
@app.route('/api-key')
def api_key_info():

    api_key = os.getenv('EXTERNAL_API_KEY', 'KEY_NAO_CONFIGURADA')

    # Máscara da chave
    if len(api_key) > 8:
        masked_key = (
            api_key[:4] +
            "*" * (len(api_key) - 8) +
            api_key[-4:]
        )
    else:
        masked_key = "****"

    logger.info(f"Usando API Key: {masked_key}")

    return jsonify({
        "api_configured": api_key != 'KEY_NAO_CONFIGURADA',
        "key_preview": masked_key
    })

# Inicialização da aplicação
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)