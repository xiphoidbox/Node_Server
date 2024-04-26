from flask import Flask, request, jsonify
from PIL import Image
import io
import tensorflow as tf
import numpy as np
import os
from flask_cors import CORS

tf.get_logger().setLevel('INFO')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

app = Flask(__name__)
CORS(app, resources={r"/mask_detection": {"origins": "https://alejandrobermea.com"}})

model = tf.keras.models.load_model('maskModel.h5')

@app.route('/')
def home():
    return jsonify({"message": "Mask detection service is running"}), 200

@app.route('/mask_detection', methods=['POST'])
def analyze_image():
    try:
        file = request.files['image']
        image = Image.open(io.BytesIO(file.read()))
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image = image.resize((128, 128))
        image = np.array(image)
        image = np.expand_dims(image, axis=0) / 255.0
        prediction = model.predict(image)
        label = np.argmax(prediction)
        result = "The person in the image is wearing a covid mask" if label == 1 else "The person in the image is not wearing a covid mask"
        return jsonify({"result": result}), 200
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return jsonify({"error": "An error occurred processing the image"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
