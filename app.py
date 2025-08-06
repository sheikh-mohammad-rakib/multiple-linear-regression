from flask import Flask, request, render_template
import numpy as np
import pickle

# Load model and scaler
with open('model.pkl', 'rb') as f:
    data = pickle.load(f)
    model = data['model']
    scaler = data['scaler']

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        engine_size = float(request.form['engine_size'])
        fuel_mpg = float(request.form['fuel_mpg'])

        # Prepare input and scale it
        features = np.array([[engine_size, fuel_mpg]])
        scaled_features = scaler.transform(features)

        # Make prediction
        prediction = model.predict(scaled_features)
        result = f"Predicted CO2 Emission: {prediction[0][0]:.2f} g/km"

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
