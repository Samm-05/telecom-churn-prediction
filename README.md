# 🎓 AI Customer Churn SaaS Platform

## 📌 Internship Project Report

---

## 👨‍💻 Intern Details

* **Intern ID:** CITS2172
* **Full Name:** Samyak Prashant Mahatme
* **No. of Weeks:** 4 Weeks
* **Project Name:** AI Customer Churn SaaS Analytics Platform
* **Domain:** Machine Learning 

---

## 📊 Project Overview

The **AI Customer Churn SaaS Platform** is an end-to-end machine learning-based analytics system designed to predict customer churn probability and analyze customer behavior patterns using real-world telecom data.

The system evolves from a basic ML model into a **SaaS-style AI intelligence platform** with interactive dashboards, risk scoring engine, and API-ready backend architecture.

It helps businesses identify at-risk customers early and take data-driven retention actions using AI-powered insights.

---

## 🎯 Project Scope

The scope of this project includes:

* Building a machine learning model for customer churn prediction
* Performing exploratory data analysis (EDA) on telecom dataset
* Feature engineering for behavioral and billing data
* Developing a risk scoring system for customers
* Creating an AI-powered retention recommendation engine
* Designing an interactive Streamlit dashboard
* Building SaaS-ready backend architecture
* Preparing system for API + database integration
* Enabling real-time prediction capability

---

## 🧠 Key Features

* 📊 Predict customer churn probability
* ⚠️ AI-based risk scoring system (Low / Medium / High risk)
* 💰 Customer segmentation (Budget / Regular / Premium)
* 🤖 Intelligent retention recommendation engine
* 📈 Business KPI dashboard (Churn rate, tenure, charges)
* 📉 Customer behavior analytics & visualization
* 🔍 Explainable AI insights (feature-driven interpretation)
* 🧩 SaaS-ready modular architecture
* 🚀 API-ready prediction system design

---

## 🏗️ System Architecture

```text
Frontend (Streamlit Dashboard)
        ↓
AI Prediction Layer (Risk Scoring Engine)
        ↓
Machine Learning Model (Logistic Regression / XGBoost)
        ↓
Feature Engineering Layer
        ↓
Data Processing Layer
        ↓
Dataset (Telecom Customer Data CSV)
```

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas / NumPy
* Scikit-learn
* XGBoost
* Streamlit
* Plotly (Data Visualization)
* Joblib (Model Serialization)

---

## 📁 Project Structure

```
Customer-Churn-SaaS/
│
├── app.py                  # Streamlit Dashboard (Main App)
├── train.py               # Model Training Script
├── model/
│    ├── best_model.pkl    # Trained ML Model
│    ├── scaler.pkl        # Feature Scaler
│    └── feature_names.pkl # Feature Schema
│
├── data/
│    └── processed.csv     # Cleaned Dataset
│
├── ai_engine.py           # AI Prediction Logic Layer
├── analytics.py           # Business Insights Module
├── backend_ready/         # API-ready structure (FastAPI future)
├── requirements.txt       # Dependencies
├── README.md              # Project Documentation
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/customer-churn-saas.git
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Train Model (Optional)

```bash
python train.py
```

### 4️⃣ Run Application

```bash
streamlit run app.py
```

---

## 📊 Sample Output

```
Risk Score: 82.5%
Risk Level: HIGH RISK 🔴
Customer Segment: Premium

Retention Suggestions:
• Offer discount plan  
• Assign retention manager  
• Provide loyalty rewards  
• Recommend contract upgrade  
```

---

## 🧠 AI Intelligence System

The project includes an AI-driven decision engine that:

* Calculates churn probability using ML models
* Classifies customers into risk categories
* Generates automated retention strategies
* Performs customer segmentation
* Provides business insights for decision-making

---

## 📚 Documentation

### 🔹 Model Workflow

* Data Collection (Telecom dataset)
* Data Cleaning & Feature Engineering
* One-hot encoding & scaling
* Model training (Logistic Regression / XGBoost)
* Model evaluation & comparison
* Best model selection
* Deployment in Streamlit dashboard

---

### 🔹 SaaS-Level Enhancements

* API-ready backend architecture (FastAPI design)
* Scalable prediction pipeline
* Modular AI engine design
* Cloud deployment ready structure
* Multi-user SaaS architecture preparation

---

## 🏆 Project Outcome

This project demonstrates:

* End-to-end Machine Learning pipeline
* SaaS-level system design thinking
* AI-powered decision support system
* Business intelligence dashboard development
* Backend + frontend integration readiness
* Real-world production deployment mindset

---

## 🚀 Future Enhancements

* Add authentication system (JWT / OAuth)
* Convert backend to FastAPI microservice
* Integrate PostgreSQL database
* Add real-time prediction API
* Deploy on cloud (AWS / Render / GCP)
* Build React-based SaaS frontend
* Add Stripe subscription system (monetization)
* Add email/SMS churn alert system

---

## 👨‍💻 Developed By

**Samyak Prashant Mahatme**
Intern – Machine Learning / AI SaaS Developer

---

