import os

from flask import Flask, render_template, redirect, url_for, request, jsonify
from dbpred import diabetes_predictor
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', result=None)

@app.route('/health', methods=['HEAD', 'GET', 'POST'])
def get_health():
    return {'msg': "API is healthy"}

@app.route('/submit', methods=['POST', 'GET'])
def data_entry():
    form_data = {}
    if request.method == 'POST':
        form_data = {
            'pregnancies': [int(request.form['pregnancies'])],
            'glucose': [int(request.form['glucose'])],
            'diastolic': [int(request.form['diastolic'])],
            'triceps': [int(request.form['triceps'])],
            'insulin': [int(request.form['insulin'])],
            'bmi': [float(request.form['bmi'])],
            'dpf': [float(request.form['dpf'])],
            'age': [int(request.form['age'])]
        }
        
        result = diabetes_predictor(form_data)
        return render_template('index.html',  result=result)
    return redirect(url_for('home'))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

