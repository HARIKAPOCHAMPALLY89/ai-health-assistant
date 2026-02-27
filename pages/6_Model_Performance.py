import streamlit as st
import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_curve,
    auc
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# ---------------- SECURITY ----------------
if "role" not in st.session_state:
    st.error("Please login first.")
    st.stop()

if st.session_state.role not in ["Admin", "Staff", "Doctor"]:
    st.error("Access Denied 🚫")
    st.stop()

st.title("📊 AI Model Performance Dashboard")
st.markdown("Evaluation metrics for the Readmission Prediction Model.")
st.markdown("---")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("hospital_data.csv")

# Rename to match training model
df = df.rename(columns={
    "Age": "age",
    "Condition": "condition",
    "Patient_State": "patient_state",
    "Readmission": "readmission"
})

required_cols = ["age", "condition", "patient_state", "readmission"]

missing = [col for col in required_cols if col not in df.columns]

if missing:
    st.error(f"Missing columns in CSV: {missing}")
    st.stop()

df = df[required_cols]

# ---------------- ENCODING ----------------
le_condition = LabelEncoder()
le_state = LabelEncoder()
le_readmission = LabelEncoder()

df["condition"] = le_condition.fit_transform(df["condition"])
df["patient_state"] = le_state.fit_transform(df["patient_state"])
df["readmission"] = le_readmission.fit_transform(df["readmission"])

X = df[["age", "condition", "patient_state"]]
y = df["readmission"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- LOAD MODEL ----------------
with open("readmission_model.pkl", "rb") as f:
    model, _, _, _ = pickle.load(f)

# Ensure correct column order
X_test = X_test[["age", "condition", "patient_state"]]

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# ---------------- METRICS ----------------
accuracy = accuracy_score(y_test, y_pred)

st.subheader("📌 Model Accuracy")
st.success(f"Accuracy: {accuracy * 100:.2f}%")

st.markdown("---")

# ---------------- CONFUSION MATRIX ----------------
st.subheader("📈 Confusion Matrix")

cm = confusion_matrix(y_test, y_pred)

fig1, ax1 = plt.subplots()
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax1)
ax1.set_xlabel("Predicted")
ax1.set_ylabel("Actual")
st.pyplot(fig1)

st.markdown("---")

# ---------------- ROC CURVE ----------------
st.subheader("📉 ROC Curve & AUC Score")

fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

fig2, ax2 = plt.subplots()
ax2.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
ax2.plot([0, 1], [0, 1], linestyle="--")
ax2.set_xlabel("False Positive Rate")
ax2.set_ylabel("True Positive Rate")
ax2.set_title("Receiver Operating Characteristic")
ax2.legend()
st.pyplot(fig2)

st.info(f"AUC Score: {roc_auc:.2f}")

st.markdown("---")

# ---------------- CLASSIFICATION REPORT ----------------
st.subheader("📋 Classification Report")

report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()

st.dataframe(report_df)