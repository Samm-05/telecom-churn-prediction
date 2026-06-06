from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI-Powered Customer Churn Analytics",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# PATHS
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "processed"
MODEL_DIR = BASE_DIR / "models"

# =====================================================
# LOAD DATA
# =====================================================

try:
    csv_files = list(DATA_DIR.glob("*.csv"))

    if len(csv_files) == 0:
        st.error("No CSV file found inside data/processed/")
        st.stop()

    df = pd.read_csv(csv_files[0])

except Exception as e:
    st.error(f"Dataset Loading Error: {e}")
    st.stop()

# =====================================================
# LOAD MODEL
# =====================================================

try:
    model = joblib.load(MODEL_DIR / "best_model.pkl")
except:
    model = None

# =====================================================
# TITLE
# =====================================================

st.title("📊 AI-Powered Customer Churn Analytics Platform")

st.markdown(
"""
### Telecom Customer Churn Prediction System

Predict customer churn risk and analyze customer behavior
using Machine Learning.
"""
)

# =====================================================
# KPI SECTION
# =====================================================

st.subheader("📈 Business KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Customers",
    len(df)
)

if "Churn" in df.columns:

    churn_rate = (
        (df["Churn"] == 1).mean() * 100
        if df["Churn"].dtype != object
        else (df["Churn"] == "Yes").mean() * 100
    )

    col2.metric(
        "Churn Rate",
        f"{churn_rate:.2f}%"
    )

else:
    col2.metric("Churn Rate", "N/A")

if "MonthlyCharges" in df.columns:

    col3.metric(
        "Avg Monthly Charges",
        f"${df['MonthlyCharges'].mean():.2f}"
    )

else:
    col3.metric(
        "Avg Monthly Charges",
        "N/A"
    )

if "tenure" in df.columns:

    col4.metric(
        "Avg Tenure",
        round(df["tenure"].mean(), 2)
    )

else:
    col4.metric(
        "Avg Tenure",
        "N/A"
    )

st.divider()

# =====================================================
# VISUALIZATIONS
# =====================================================

st.subheader("📊 Customer Analytics")

col1, col2 = st.columns(2)

with col1:

    if "MonthlyCharges" in df.columns:

        fig = px.histogram(
            df,
            x="MonthlyCharges",
            title="Monthly Charges Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

with col2:

    if "tenure" in df.columns:

        fig2 = px.histogram(
            df,
            x="tenure",
            title="Customer Tenure Distribution"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

st.divider()

# =====================================================
# CHURN DISTRIBUTION
# =====================================================

if "Churn" in df.columns:

    st.subheader("📉 Churn Distribution")

    churn_counts = df["Churn"].value_counts()

    fig3 = px.pie(
        values=churn_counts.values,
        names=churn_counts.index,
        title="Customer Churn Breakdown"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

st.divider()

# =====================================================
# MODEL INFORMATION
# =====================================================

st.subheader("🤖 Model Information")

if model is not None:

    st.success("Best Model Loaded Successfully")

    st.write(
        f"Model Type: {type(model).__name__}"
    )

else:

    st.warning(
        "Model file not found."
    )

st.divider()

# =====================================================
# DATA PREVIEW
# =====================================================

st.subheader("🗂 Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

# =====================================================
# PROJECT SUMMARY
# =====================================================

st.divider()

st.subheader("📌 Project Summary")

st.markdown(
"""
### Features Implemented

✅ Data Cleaning

✅ Exploratory Data Analysis

✅ Feature Engineering

✅ Logistic Regression

✅ Decision Tree

✅ Random Forest

✅ XGBoost

✅ Model Comparison

✅ Feature Importance

✅ Risk Scoring

✅ Retention Recommendations

✅ Streamlit Dashboard

---

### Best Performing Model

**Logistic Regression**

Accuracy: **80.70%**

F1 Score: **0.609**
"""
)