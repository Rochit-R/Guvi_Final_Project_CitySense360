import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

def train_dummy_lstm():
    data = np.array([
    20, 22, 25, 30, 35,
    40, 45, 50, 55, 60,
    65, 70, 75, 80, 85, 90
]).reshape(-1, 1)

    data = scaler.fit_transform(data)

    X, y = [], []
    for i in range(len(data) - 3):
        X.append(data[i:i+3])
        y.append(data[i+3])

    X, y = np.array(X), np.array(y)

    model = Sequential([
        LSTM(32, activation="relu", input_shape=(3, 1)),
        Dense(1)
    ])

    model.compile(optimizer="adam", loss="mse")
    model.fit(X, y, epochs=100, verbose=0)

    return model

model = train_dummy_lstm()

def predict_traffic(next_values: list):
    values = np.array(next_values).reshape(-1, 1)
    values = scaler.transform(values)
    values = values.reshape(1, 3, 1)

    prediction = model.predict(values, verbose=0)
    return float(scaler.inverse_transform(prediction)[0][0])
