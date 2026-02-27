
import streamlit as st

if "role" not in st.session_state:
    st.error("Please login first.")
    st.stop()

if st.session_state.role not in ["Admin", "Staff"]:
    st.error("Access Denied 🚫")
    st.stop()
import streamlit as st
import pandas as pd
import sqlite3

# ---------------- ACCESS CONTROL ----------------
if "role" not in st.session_state or st.session_state.role not in ["Admin", "Staff"]:
    st.error("Access Denied 🚫")
    st.stop()

st.title("📊 Hospital Command Center")
st.markdown("### Digital Hospital Record Management System")
st.markdown("---")

DB_NAME = "hospital.db"

def get_data():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql("SELECT * FROM patients", conn)
    conn.close()
    return df

df = get_data()

if df.empty:
    st.warning("No patient records found.")
    st.stop()

# ---------------- KPIs ----------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Patients", len(df))
col2.metric("Unique Diseases", df["disease"].nunique())
col3.metric("States Covered", df["state"].nunique())

st.markdown("---")

# ---------------- FILTER SECTION ----------------
st.subheader("🔎 Filter Patient Records")

search_term = st.text_input("Search by Patient ID")

filtered_df = df.copy()

if search_term:
    filtered_df = filtered_df[
        filtered_df["patient_id"].astype(str).str.contains(search_term)
    ]

st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")

# ---------------- ANALYTICS ----------------
st.subheader("📈 Admissions Trend")

filtered_df["admission_date"] = pd.to_datetime(
    filtered_df["admission_date"], errors="coerce"
)

admissions = filtered_df.groupby(
    filtered_df["admission_date"].dt.date
).size()

st.line_chart(admissions)

st.markdown("### 🦠 Disease Distribution")
st.bar_chart(filtered_df["disease"].value_counts())

st.markdown("### 🗺 State-wise Distribution")
st.bar_chart(filtered_df["state"].value_counts())

st.markdown("---")

# ---------------- PDF GENERATION ----------------
st.subheader("📄 Generate Patient Medical Report")

selected_patient = st.selectbox(
    "Select Patient ID",
    filtered_df["patient_id"].unique()
)

if st.button("Generate Report"):

    patient_data = filtered_df[
        filtered_df["patient_id"] == selected_patient
    ].iloc[0]

    st.success("Report Preview")

    st.write("**Patient ID:**", patient_data["patient_id"])
    st.write("**Age:**", patient_data["age"])
    st.write("**Gender:**", patient_data["gender"])
    st.write("**Disease:**", patient_data["disease"])
    st.write("**State:**", patient_data["state"])
    st.write("**Admission Date:**", patient_data["admission_date"])