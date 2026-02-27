import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- SECURITY ----------------
if "role" not in st.session_state:
    st.error("Please login first.")
    st.stop()

if st.session_state.role not in ["Admin", "Staff", "Doctor"]:
    st.error("Access Denied 🚫")
    st.stop()

# ---------------- PAGE TITLE ----------------
st.title("🤖 AI Readmission Risk Predictor")
st.markdown("Predict whether a patient is likely to be readmitted based on historical data.")
st.markdown("---")

# ---------------- LOAD MODEL ----------------
try:
    with open("readmission_model.pkl", "rb") as f:
        model, le_condition, le_state, le_readmission = pickle.load(f)
except:
    st.error("Model file not found. Please train the model first.")
    st.stop()

# ---------------- USER INPUTS ----------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120)

with col2:
    condition = st.selectbox("Condition", le_condition.classes_)

state = st.selectbox("State", le_state.classes_)

st.markdown("---")

# ---------------- PREDICTION ----------------
if st.button("🔍 Predict Readmission Risk"):

    cond_encoded = le_condition.transform([condition])[0]
    state_encoded = le_state.transform([state])[0]

    input_data = pd.DataFrame(
        [[age, cond_encoded, state_encoded]],
        columns=["age", "condition", "patient_state"]
    )

    # Prediction + Probability
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0]
    confidence = max(proba) * 100

    result = le_readmission.inverse_transform([prediction])[0]

    st.subheader("📊 Prediction Result")

    if str(result).lower() in ["yes", "true", "1"]:
        st.error(f"🔴 High Risk of Readmission ({confidence:.2f}% confidence)")
    else:
        st.success(f"🟢 Low Risk of Readmission ({confidence:.2f}% confidence)")

    st.markdown("---")

    # ---------------- FEATURE IMPORTANCE ----------------
    st.subheader("📈 Feature Importance Analysis")

    features = ["Age", "Condition", "State"]
    importance = model.feature_importances_

    fig, ax = plt.subplots()
    ax.bar(features, importance)
    ax.set_ylabel("Importance Score")
    ax.set_title("Factors Influencing Readmission")
    st.pyplot(fig)

    st.markdown("---")

    st.info("This prediction is generated using a Random Forest Machine Learning model trained on historical hospital data.")