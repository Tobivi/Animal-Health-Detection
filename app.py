from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

model = load_model("healthdetctionmodel.h5")

class_labels = ["Class1", "Class2", "Class3", "Class4"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        img_file = request.files['image']

        
        img = image.load_img(img_file, target_size=(image_size[0], image_size[1]))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  

        
        predictions = model.predict(img_array)

        
        predicted_class = class_labels[np.argmax(predictions)]

        return jsonify({'class': predicted_class})

if __name__ == '__main__':
    app.run(debug=True)
