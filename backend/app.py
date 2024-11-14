from flask import Flask, send_file, jsonify, request
from flask_cors import CORS
from routes.api import generate_heatmap

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "<h1>Welcome to the Goa River Monitoring API</h1>"

@app.route('/generate-heatmap', methods=['GET'])
def get_heatmap():
    river = request.args.get('river')
    if not river:
        return jsonify({'error': 'No river specified'}), 400
    try:
        image_path = generate_heatmap(river)  # Pass the river parameter
        return send_file(image_path, mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=3001)
