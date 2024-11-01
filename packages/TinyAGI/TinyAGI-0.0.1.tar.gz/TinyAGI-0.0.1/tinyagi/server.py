# tinyagi/server.py

from flask import Flask, request, jsonify, Response
from .config import ConfigManager
from .model import ModelLoader

def create_app():
    app = Flask(__name__)
    config_manager = ConfigManager()
    model_loader = ModelLoader(config_manager.get_config())

    @app.route('/chat', methods=['POST'])
    def chat():
        data = request.get_json()
        messages = data.get('messages')
        inference_params = data.get('inference_params', {})
        stream = data.get('stream', False)

        if not messages:
            return jsonify({'error': 'Messages are required'}), 400

        # Build prompt
        prompt = ''
        for msg in messages:
            role = msg.get('role', 'user')
            content = msg.get('content', '')
            prompt += f"{role.capitalize()}: {content}\n"
        prompt += "Assistant:"

        try:
            if stream:
                def generate():
                    for chunk in model_loader.generate(prompt, inference_params, stream=True):
                        yield chunk['choices'][0]['text']
                return Response(generate(), mimetype='text/plain')
            else:
                output = model_loader.generate(prompt, inference_params)
                text = output['choices'][0]['text']
                return jsonify({'response': text})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/generate', methods=['POST'])
    def generate():
        data = request.get_json()
        prompt = data.get('prompt')
        inference_params = data.get('inference_params', {})
        stream = data.get('stream', False)

        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400

        try:
            if stream:
                def generate():
                    for chunk in model_loader.generate(prompt, inference_params, stream=True):
                        yield chunk['choices'][0]['text']
                return Response(generate(), mimetype='text/plain')
            else:
                output = model_loader.generate(prompt, inference_params)
                text = output['choices'][0]['text']
                return jsonify({'response': text})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/embed', methods=['POST'])
    def embed():
        data = request.get_json()
        input_data = data.get('input')

        if not input_data:
            return jsonify({'error': 'Input text is required'}), 400

        try:
            embeddings = model_loader.embed(input_data)
            return jsonify({'embedding': embeddings})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/reload', methods=['POST'])
    def reload_model():
        data = request.get_json()
        config_file = data.get('config_file')
        try:
            config = config_manager.reload_config(config_file)
            model_loader.reload_model(config)
            return jsonify({'message': 'Model reloaded successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/config', methods=['GET'])
    def get_config():
        return jsonify(config_manager.get_config()), 200

    return app

def run_server():
    app = create_app()
    app.run(debug=True)
