# 🩺 Diabetes Prediction Web App

This is a **Flask-based** web application that predicts whether a person is diabetic or non-diabetic based on input medical parameters. The prediction is powered by a machine learning model trained on the Pima Indians Diabetes Dataset.

## ✨ Features

- 🖥️ User-friendly web interface for inputting medical data
- 🤖 Predicts diabetes status using a trained ML model
- 📊 Visual feedback and result display
- 🖼️ Reference images and design assets included

## 🚀 Deployment

**🌐 Deployed Project:**  
🔗 [https://diabetes-prediction-new-uyn8.onrender.com](https://diabetes-prediction-new-uyn8.onrender.com)

## 📁 Project Structure

```
app.py
dbpred.py
diabetes_model.pkl
scaler.pkl
requirements.txt
render.yaml
ML-MODEL/
static/
templates/
```

- `app.py`: Main Flask application.
- `dbpred.py`: Loads the ML model and scaler, and provides the prediction function.
- `diabetes_model.pkl`: Trained machine learning model.
- `scaler.pkl`: Scaler used for preprocessing input data.
- `requirements.txt`: Python dependencies.
- `render.yaml`: Deployment configuration for Render.com.
- `static/`: Static files (CSS, JS, images).
- `templates/`: HTML templates.

## 🛠️ Setup Instructions

1. **Clone the repository**

   ```sh
   git clone https://github.com/shivsharcode/Diabetes-Prediction-New.git
   cd Diabetes-Prediction-New/project
   ```

2. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

3. **Ensure model files are present**

   Make sure `diabetes_model.pkl` and `scaler.pkl` are in the project root.

4. **Run the application**

   ```sh
   python app.py
   ```

5. **Open in browser**

   Visit [http://localhost:5000](http://localhost:5000) to use the app.

## 📜 License

This project is for educational purposes.

---

**👤 Author:** [shivsharcode](https://github.com/shivsharcode)