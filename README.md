# 🚢 Titanic Survival Prediction - Machine Learning App

> A Machine Learning web application that predicts whether a Titanic passenger would survive.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-red?style=for-the-badge)](https://agk7thkk6bnxeattlpmtmv.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)

### 🔗 Links
- **Live App:** https://agk7thkk6bnxeattlpmtmv.streamlit.app
- **GitHub Repo:** https://github.com/sivasankari-v/titanic-survival-ml-app

---

### 📌 Project Overview
This project uses the Titanic dataset to predict passenger survival. The model is trained on historical data like Ticket Class, Gender, Age, Fare, and Family Size.

**Model Accuracy: ~80%**

### ✨ Features
- Interactive Streamlit Web App
- Real-time survival prediction with balloons animation
- User-friendly sliders and dropdowns
- Trained Random Forest Classifier
- Fully deployed on Streamlit Cloud

### 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn, Streamlit
- **Model File:** titanic_model.pkl (1.78 MB)
- **Deployment:** Streamlit Cloud + GitHub

### 📂 Project Structure
titanic-survival-ml-app/
├── app.py                 # Streamlit web app
├── titanic_model.pkl      # Trained ML model
├── requirements.txt       # Dependencies
└── README.md              # Documentation

### 🚀 How to Run Locally
git clone https://github.com/sivasankari-v/titanic-survival-ml-app.git
pip install -r requirements.txt
streamlit run app.py

### 🎯 Model Inputs
- **Pclass:** Ticket Class (1=Rich, 3=Poor)
- **Sex:** Gender (female has higher survival)
- **Age:** Passenger age
- **SibSp:** Siblings/Spouses aboard
- **Parch:** Parents/Children aboard
- **Fare:** Ticket price

### 📊 Prediction Logic
- 1st Class + Female + Young Age = HIGH Survival Chance
- 3rd Class + Male + Low Fare = LOW Survival Chance
- Reflects real Titanic history - "Women and Children First"

### 👩‍💻 Author
**Sivasankari V**
GitHub: @sivasankari-v
Project for InternCircle ML Internship

### 📜 Submission
- **InternCircle Project Link:** https://github.com/sivasankari-v/titanic-survival-ml-app
- **Live Demo:** https://agk7thkk6bnxeattlpmtmv.streamlit.app
- Submitted on InternCircle portal under "Submit Project"

---
⭐ Star this repo if you like it!
