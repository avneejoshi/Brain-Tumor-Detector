import os
import numpy as np
from PIL import Image
import cv2
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.applications.vgg19 import VGG19

# Initialize the VGG19 model with custom layers
base_model = VGG19(include_top=False, input_shape=(240, 240, 3))
x = base_model.output
flat = Flatten()(x)
class_1 = Dense(4608, activation='relu')(flat)
drop_out = Dropout(0.2)(class_1)
class_2 = Dense(1152, activation='relu')(drop_out)
output = Dense(2, activation='softmax')(class_2)
model_03 = Model(base_model.inputs, output)

# Load the model weights
model_03.load_weights('vgg_unfrozen.h5')

app = Flask(__name__)

print('Model loaded. Check http://127.0.0.1:5000/')

def get_className(classNo):
    if classNo == 0:
        return "Woo hoo!! Brain Tumor not detected. Have a good health."
    elif classNo == 1:
        return "Sorry. Brain Tumor Detected. Consult a Neurologist without further delay."

def getResult(img_path):
    try:
        # Preprocess the image
        image = cv2.imread(img_path)
        if image is None:
            raise ValueError("Error reading image. Make sure the file is a valid image.")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Convert to RGB
        image = Image.fromarray(image)
        image = image.resize((240, 240))
        image = np.array(image) / 255.0  # Normalize the image
        input_img = np.expand_dims(image, axis=0)
        
        # Predict
        result = model_03.predict(input_img)
        result01 = np.argmax(result, axis=1)
        return result01[0]
    except Exception as e:
        print(f"Error during image processing: {e}")
        return None

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    f = request.files['file']
    
    if f.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
    
    # Ensure the uploads directory exists
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    
    f.save(file_path)
    
    # Get prediction
    value = getResult(file_path)
    if value is None:
        return jsonify({"error": "Error processing the image"}), 500

    result = get_className(value)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
