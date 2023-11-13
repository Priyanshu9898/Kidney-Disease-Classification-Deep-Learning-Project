from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from kidneyDiseaseClassifier.utils.common import decodeImage
from kidneyDiseaseClassifier.pipeline.prediction import PredictionPipeline
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return "<h1>Hello world</h1>"


@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    # os.system("dvc repro")
    return "Training done successfully!"


@app.route("/predict", methods=['POST'])
def predictRoute():
    try:
        data = request.json
        if not data or 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400

        # Extract the image data
        image_data = data['image']
        if ',' in image_data:  # Check for base64 format
            image_data = image_data.split(',')[1]  # Remove the Base64 header
        image_data = base64.b64decode(image_data)  # Decode Base64

        with open("inputImage.jpg", 'wb') as f:
            f.write(image_data)
            f.close()
            
        # Convert to an image and process
        image = Image.open(BytesIO(image_data))

        # Prediction logic
        result = clApp.classifier.predict()
        
        
        print(jsonify(result))
        return jsonify(result)
    except Exception as e:
        print("An error occurred:", e)
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    clApp = ClientApp()

    app.run(host='0.0.0.0', port=8080)  # for AWS
