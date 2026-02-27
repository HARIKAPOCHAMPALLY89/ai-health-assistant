# 🏥 VitalShield AI

VitalShield AI is an AI-powered healthcare management system built using Streamlit and Machine Learning.

The system integrates hospital data management with predictive intelligence to assist in patient monitoring and readmission risk prediction.

---

## 🚀 Features

- Patient data management
- Doctor & appointment modules
- Readmission prediction using Machine Learning
- Interactive Streamlit dashboard
- Multi-page structured interface

---

## 🧠 Machine Learning

The system uses a trained model (`readmission_model.pkl`) to predict patient readmission risk based on clinical inputs.

Model training script: `train_model.py`

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- SQLite (if used)

---

## 📂 Project Structure

```
ai-health-assistant/
│
├── app.py
├── pages/
├── train_model.py
├── readmission_model.pkl
├── requirements.txt
└── .gitignore
```

---

## ▶️ How to Run Locally

1. Clone the repository:

```
git clone https://github.com/HARIKAPOCHAMPALLY89/ai-health-assistant.git
```

2. Navigate into the folder:

```
cd ai-health-assistant
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the app:

```
streamlit run app.py
```

---

## 📌 Future Enhancements

- Real-time hospital database integration
- Deployment on cloud
- Role-based authentication system
- Advanced predictive analytics

---

## 👩‍💻 Author

Harika Pochampally  
GitHub: https://github.com/HARIKAPOCHAMPALLY89
