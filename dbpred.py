import numpy as np
import pandas as pd
import pickle

# Load the trained model and scaler from pickle files
with open('diabetes_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

def diabetes_predictor(form_data):
    row = pd.DataFrame(form_data)
    X_sample = scaler.transform(row)
    y_pred = model.predict(X_sample)
    print("Predicted Class : ", y_pred)
    if y_pred[0] == 0:
        return "Non-Diabetic"
    else:
        return "Diabetic"