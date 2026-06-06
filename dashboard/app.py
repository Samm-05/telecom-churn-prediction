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
# STYLE
# =====================================================
st.markdown("""
<style>

[data-testid="metric-container"]{
    background-color:#f8f9fa;
    border-radius:15px;
    padding:15px;
}

h1{
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

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
# LOAD MODEL + ARTIFACTS
# =====================================================
try:
    model = joblib.load(MODEL_DIR / "best_model.pkl")
    scaler = joblib.load(MODEL_DIR / "scaler.pkl")
    feature_names = joblib.load(MODEL_DIR / "feature_names.pkl")
except:
    model = None
    scaler = None
    feature_names = None

# =====================================================
# TITLE
# =====================================================
st.title("📊 AI-Powered Customer Churn Analytics Platform")

st.markdown("""
### Telecom Customer Churn Prediction System
Predict customer churn risk and analyze customer behavior using Machine Learning.
""")

# =====================================================
# KPI SECTION
# =====================================================
st.subheader("📈 Business KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", len(df))

if "Churn" in df.columns:
    churn_rate = (
        (df["Churn"] == 1).mean() * 100
        if df["Churn"].dtype != object
        else (df["Churn"] == "Yes").mean() * 100
    )
    col2.metric("Churn Rate", f"{churn_rate:.2f}%")
else:
    col2.metric("Churn Rate", "N/A")

col3.metric(
    "Avg Monthly Charges",
    f"${df['MonthlyCharges'].mean():.2f}" if "MonthlyCharges" in df.columns else "N/A"
)

col4.metric(
    "Avg Tenure",
    round(df["tenure"].mean(), 2) if "tenure" in df.columns else "N/A"
)

st.divider()

# =====================================================
# VISUALIZATIONS
# =====================================================
st.subheader("📊 Customer Analytics")

col1, col2 = st.columns(2)

with col1:
    if "MonthlyCharges" in df.columns:
        fig = px.histogram(df, x="MonthlyCharges", title="Monthly Charges Distribution")
        st.plotly_chart(fig, use_container_width=True)

with col2:
    if "tenure" in df.columns:
        fig2 = px.histogram(df, x="tenure", title="Customer Tenure Distribution")
        st.plotly_chart(fig2, use_container_width=True)

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

    st.plotly_chart(fig3, use_container_width=True)

st.divider()

# =====================================================
# ================= PREDICTION CENTER =================
# =====================================================
st.header("🎯 Customer Prediction Center")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])

with col2:
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment = st.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check", "Credit card (automatic)", "Bank transfer (automatic)"]
    )
    tenure = st.slider("Tenure (Months)", 0, 72, 12)
    monthly = st.slider("Monthly Charges", 0.0, 150.0, 70.0)

# =====================================================
# FEATURE ENGINEERING
# =====================================================
total = tenure * monthly

input_df = pd.DataFrame(columns=feature_names)
input_df.loc[0] = 0

input_df["SeniorCitizen"] = senior
input_df["tenure"] = tenure
input_df["MonthlyCharges"] = monthly
input_df["TotalCharges"] = total

input_df["gender_Male"] = 1 if gender == "Male" else 0
input_df["Partner_Yes"] = 1 if partner == "Yes" else 0
input_df["Dependents_Yes"] = 1 if dependents == "Yes" else 0
input_df["PhoneService_Yes"] = 1 if phone_service == "Yes" else 0

input_df["MultipleLines_Yes"] = 1 if multiple_lines == "Yes" else 0
input_df["MultipleLines_No phone service"] = 1 if multiple_lines == "No phone service" else 0

input_df["InternetService_Fiber optic"] = 1 if internet_service == "Fiber optic" else 0
input_df["InternetService_No"] = 1 if internet_service == "No" else 0

input_df["Contract_One year"] = 1 if contract == "One year" else 0
input_df["Contract_Two year"] = 1 if contract == "Two year" else 0

input_df["PaperlessBilling_Yes"] = 1 if paperless == "Yes" else 0

input_df["PaymentMethod_Credit card (automatic)"] = 1 if payment == "Credit card (automatic)" else 0
input_df["PaymentMethod_Electronic check"] = 1 if payment == "Electronic check" else 0
input_df["PaymentMethod_Mailed check"] = 1 if payment == "Mailed check" else 0

# =====================================================
# PREDICTION
# =====================================================
if st.button("🚀 Predict Customer Churn") and model is not None:

    scaled = scaler.transform(input_df)

    prediction = model.predict(scaled)[0]
    probability = model.predict_proba(scaled)[0][1]

    risk_score = round(probability * 100, 2)

    st.divider()

    c1, c2, c3 = st.columns(3)

    c1.metric("Risk Score", f"{risk_score}%")
    c2.metric("Monthly Charges", f"${monthly:.2f}")
    c3.metric("Tenure", tenure)

    # Risk Level
    if risk_score >= 80:
        st.error("🔴 HIGH RISK CUSTOMER")
    elif risk_score >= 50:
        st.warning("🟠 MEDIUM RISK CUSTOMER")
    else:
        st.success("🟢 LOW RISK CUSTOMER")

    # Segment
    if monthly >= 100:
        segment = "Premium"
    elif monthly >= 60:
        segment = "Regular"
    else:
        segment = "Budget"

    st.info(f"Customer Segment: {segment}")

    # Recommendation Engine
    st.subheader("💡 Retention Recommendation")

    if risk_score >= 80:
        st.warning("""
        • Offer Discount  
        • Assign Retention Agent  
        • Loyalty Rewards  
        • Contract Upgrade Plan  
        """)
    elif risk_score >= 50:
        st.info("""
        • Service Bundle  
        • Upgrade Internet Plan  
        • Customer Engagement Campaign  
        """)
    else:
        st.success("""
        • Customer Healthy  
        • Continue Regular Engagement  
        """)

# =====================================================
# MODEL INFO
# =====================================================
st.divider()
st.subheader("🤖 Model Information")

if model:
    st.success(f"Model Loaded: {type(model).__name__}")
else:
    st.warning("Model not found.")

# =====================================================
# DATA PREVIEW
# =====================================================
st.divider()
st.subheader("🗂 Dataset Preview")
st.dataframe(df.head(20), use_container_width=True)

# =====================================================
# INSIGHTS
# =====================================================
st.divider()
st.subheader("📌 Executive Insights")

st.success("""
• Month-to-month customers have highest churn risk  
• High monthly charges increase churn probability  
• Longer tenure improves retention  
• Electronic check users show higher churn  
• Contract upgrades reduce churn significantly  
""")

# =====================================================
# SUMMARY
# =====================================================
st.divider()
st.subheader("📌 Project Summary")

st.markdown("""
### Features
✅ EDA  
✅ Feature Engineering  
✅ ML Models (Logistic, RF, XGBoost)  
✅ Model Comparison  
✅ Risk Scoring  
✅ Retention System  
✅ Streamlit Dashboard  
""")