from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Módulos
from openai_service import classify_message
from router import choose_recipient
from email_service import send_email

# Carregar .env
load_dotenv()

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def receive_message():
    data = request.get_json()

    # Validação
    if not data or 'message' not in data:
        return jsonify({'erro': 'Campo "mensagem" é obrigatório.'}), 400

    message = data['message']

    # Classificar com OpenAI
    try:
        category = classify_message(message)
    except Exception as e:
        return jsonify({'erro': f'Erro ao classificar mensagem: {str(e)}'}), 500

    # Escolher destinatário
    recipient = choose_recipient(category)
    if not recipient:
        return jsonify({'erro': 'Categoria não reconhecida.'}), 400

    # Enviar e-mail
    try:
        send_email(recipient, 'Nova solicitação de suporte', message)
    except Exception as e:
        return jsonify({'erro': f'Erro ao enviar e-mail: {str(e)}'}), 500

    return jsonify({
      'status': 'ok',
      'category': category
    }), 200

if __name__ == '__main__':
    app.run(debug=True)