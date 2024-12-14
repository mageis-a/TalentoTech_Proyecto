from flask import Flask, render_template, request 
import pickle
import pandas as pd
import json

# Cargar el modelo y el encoder
with open('modelo_xgb.pkl', 'rb') as f:
    modelo = pickle.load(f)

with open('encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediccion', methods=['POST'])
def predict():
    prediccion = None  # Inicializamos la variable prediccion
    try:
        if request.method == 'POST':
            datos = pd.DataFrame({
                'MAQUINA': [request.form['maquina']],
                'LUGAR DE OPERACIÓN': [request.form['lugar_operacion']],
                'AÑO': [int(request.form['ano'])],
                'MES': [int(request.form['mes'])],
                'DÍA': [int(request.form['dia'])]
                
            })
            
            # Asegúrate de que el encoder pueda transformar estos datos correctamente
            nuevos_datos_encoded = encoder.transform(datos)
            print(datos)
            prediccion = modelo.predict(nuevos_datos_encoded)
            prediccion = float(prediccion[0])
    except Exception as e:
        print(f"Error: {e}")
        prediccion = "Error en la predicción"

    # Retornamos la predicción, aunque sea un mensaje de error
    return {"prediccion":prediccion}

if __name__ == '__main__':
    app.run(debug=True)
