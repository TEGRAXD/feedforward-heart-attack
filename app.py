from flask import Flask, request, render_template
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import pickle
import tensorflow as tf

# training only
# from tensorflow.keras.models import load_model
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Activation
# from tensorflow.keras.optimizers import Adam

app = Flask(__name__)

# membuat dataframe dengan membaca heart.csv
df = pd.read_csv('heart.csv')

# drop kolom yang tidak diperlukan
X = df.drop('output',axis=1).values

# output adalah kolom yang akan diprediksi
y = df['output'].values

# split data digunakan untuk membelah data menjadi data training dan data testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)

# normalisasi data
s_scaler = StandardScaler()
X_train = s_scaler.fit_transform(X_train.astype(np.float64))
X_test = s_scaler.transform(X_test.astype(np.float64))

# load model
model = tf.keras.models.load_model('heart_attack_model.keras')

@app.route('/')
def index():
    return render_template('index.html', output='')

@app.route('/predict_feedforward', methods=['POST'])
def predict_feedforward():
    d1, d2, d3, d4, d5, d6, d7 = [x for x in request.form.values()]

    # data yang diinputkan ditransformasikan ke np.ndarray
    input = np.array([[1.0, float(d1), float(d2), float(d3), float(d4), float(d5), float(d6), 1.0, float(d7), 0.0, 3.5, 0.0, 0.0, 2.0]])

    # s_scaler digunakan untuk menstandarisasi data input
    case = s_scaler.transform(input)

    # melakukan prediksi data
    predict_val = model.predict(case)

    return render_template('index.html', d1=d1, d2=konversi(d2, d=2), d3=konversi(d3, d=3), d4=d4, d5=d5, d6=konversi(d6, d=6), d7=d7, output=predict_val_to_percent(predict_val[0][0]))

def konversi(nilai, d = 0):
    if d == 2:
        if int(nilai) == 0:
            return 'Perempuan'
        if int(nilai) == 1:
            return 'Laki-laki'
    if d == 3:
        if int(nilai) == 0:
            return 'Typical Angina'
        if int(nilai) == 1:
            return 'Atypical Angina'
        if int(nilai) == 2:
            return 'Non-anginal Pain'
        if int(nilai) == 3:
            return 'Asymptomaic'
    if d == 6:
        if int(nilai) == 0:
            return '> 120 mg/dL'
        if int(nilai) == 1:
            return '< 120 mg/dL'


def predict_val_to_percent(nilai):
    if (nilai >= 1.0):
        nilai = 1.0
    elif (nilai <= 0.0):
        nilai = abs(nilai)
    
    nilai = nilai * 100

    if (nilai >= 50.0):
        return 'Terkena Penyakit Jantung'
    else:
        return 'Tidak Terkena Penyakit Jantung'

if __name__ == '__main__':
    app.run(debug=False)