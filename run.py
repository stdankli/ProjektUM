import base64
from flask import Flask, request, jsonify, render_template
import numpy as np
from PIL import Image
from io import BytesIO
from tensorflow.keras.models import load_model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        data = request.json.get("image")
        model_name = request.json.get("model")
        if not data or not model_name:
            return jsonify({"status": "error", "error": "Brak danych obrazu lub nazwy modelu"}), 400

        image_data = base64.b64decode(data)
        image = Image.open(BytesIO(image_data)).convert('L') 

        image = image.resize((28, 28)) 
        image_array = np.array(image) / 255.0 
        image_array = image_array.reshape(1, 28, 28, 1)

        if model_name == 'M_Koloch':
            model = load_model('M_Koloch.h5')
        elif model_name == 'Klimeczek':
            model = load_model('M_Klimeczek2.h5')
        elif model_name == 'Dorosh':
            model = load_model('M_Dorosh.h5')
        else:
            return jsonify({"status": "error", "error": "Nieznany model"}), 400

        prediction = model.predict(image_array)
        digit = np.argmax(prediction)  

        return jsonify({"status": "success", "digit": int(digit)})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
