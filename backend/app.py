from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.predict import predict_image

app = Flask(__name__)
CORS(app)

@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    file = request.files['image']
    result = predict_image(file)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)