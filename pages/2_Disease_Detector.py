import streamlit as st
from datetime import datetime

# ---------------- SECURITY ----------------
if "role" not in st.session_state:
    st.error("Please login first.")
    st.stop()

# ---------------- PAGE ----------------
st.title("🧠 AI Disease Detector & Health Calculator")

st.markdown("---")

# ---------------- MASSIVE DISEASE DATABASE ----------------
diseases = {
    "fever": {"cause": "Viral or bacterial infection", "remedy": "Rest, hydration, paracetamol", "risk": "Normal"},
    "cold": {"cause": "Viral infection", "remedy": "Steam inhalation, fluids", "risk": "Normal"},
    "flu": {"cause": "Influenza virus", "remedy": "Rest, antiviral meds if severe", "risk": "Moderate"},
    "diabetes": {"cause": "Insulin resistance or deficiency", "remedy": "Blood sugar monitoring, insulin", "risk": "Chronic"},
    "hypertension": {"cause": "High blood pressure", "remedy": "Reduce salt, medication", "risk": "Chronic"},
    "heart attack": {"cause": "Blocked coronary artery", "remedy": "Emergency medical attention", "risk": "Severe"},
    "stroke": {"cause": "Blocked or burst blood vessel in brain", "remedy": "Immediate hospital care", "risk": "Severe"},
    "asthma": {"cause": "Airway inflammation", "remedy": "Inhalers, avoid triggers", "risk": "Moderate"},
    "pneumonia": {"cause": "Lung infection", "remedy": "Antibiotics if bacterial", "risk": "Severe"},
    "tuberculosis": {"cause": "Bacterial infection", "remedy": "Long-term antibiotics", "risk": "Severe"},
    "migraine": {"cause": "Neurological triggers", "remedy": "Pain relief medication", "risk": "Moderate"},
    "food poisoning": {"cause": "Contaminated food", "remedy": "Hydration, rest", "risk": "Normal"},
    "appendicitis": {"cause": "Inflamed appendix", "remedy": "Surgery", "risk": "Severe"},
    "covid": {"cause": "Coronavirus infection", "remedy": "Isolation, medical support", "risk": "Moderate"},
    "anemia": {"cause": "Low hemoglobin", "remedy": "Iron supplements", "risk": "Moderate"},
    "arthritis": {"cause": "Joint inflammation", "remedy": "Pain management", "risk": "Chronic"},
    "allergy": {"cause": "Immune reaction", "remedy": "Antihistamines", "risk": "Normal"},
    "ulcer": {"cause": "Stomach lining damage", "remedy": "Antacids, medication", "risk": "Moderate"},
    "thyroid": {"cause": "Hormonal imbalance", "remedy": "Hormone therapy", "risk": "Chronic"},
    "dehydration": {"cause": "Low fluid levels", "remedy": "Increase water intake", "risk": "Normal"},
}

# ---------------- DISEASE SEARCH ----------------
st.subheader("🔍 Check Your Symptoms")

issue = st.text_input("Enter condition or symptom")

if issue:
    issue = issue.lower()

    found = False

    for disease in diseases:
        if disease in issue:
            info = diseases[disease]
            st.success(f"Condition Detected: {disease.title()}")
            st.write("**Cause:**", info["cause"])
            st.write("**Recommended Action:**", info["remedy"])

            if info["risk"] == "Severe":
                st.error("🔴 Severe Risk – Seek immediate medical help!")
            elif info["risk"] == "Moderate":
                st.warning("🟡 Moderate Risk – Monitor and consult doctor.")
            elif info["risk"] == "Chronic":
                st.info("🟠 Chronic Condition – Requires long-term care.")
            else:
                st.success("🟢 Mild/Normal Condition – Basic care recommended.")

            found = True
            break

    if not found:
        st.warning("Condition not found. Please consult a doctor.")

st.markdown("---")

# ---------------- BMI CALCULATOR ----------------
st.subheader("📏 BMI Calculator")

weight = st.number_input("Weight (kg)", min_value=1.0)
height = st.number_input("Height (cm)", min_value=1.0)

if weight and height:
    bmi = weight / ((height/100) ** 2)
    st.write(f"Your BMI: {round(bmi, 2)}")

    if bmi < 18.5:
        st.warning("Underweight")
    elif 18.5 <= bmi < 25:
        st.success("Normal Weight")
    elif 25 <= bmi < 30:
        st.warning("Overweight")
    else:
        st.error("Obese")

st.markdown("---")

# ---------------- WATER INTAKE CALCULATOR ----------------
st.subheader("💧 Daily Water Intake")

if weight:
    water = weight * 0.033  # 33ml per kg
    st.write(f"Recommended Water Intake: {round(water,2)} Liters per day")