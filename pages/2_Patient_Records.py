import streamlit as st
import pandas as pd
import sqlite3

# ---------------- SECURITY ----------------
if "role" not in st.session_state:
    st.error("Please login first.")
    st.stop()

if st.session_state.role not in ["Admin", "Staff", "Doctor"]:
    st.error("Access Denied 🚫")
    st.stop()

# ---------------- PAGE CONFIG ----------------
st.title("📋 Patient Records Dashboard")

# ---------------- DATABASE FUNCTION ----------------
def get_data():
    conn = sqlite3.connect("hospital.db")
    df = pd.read_sql("SELECT * FROM patients", conn)
    conn.close()
    return df

df = get_data()

# ---------------- METRICS ----------------
st.metric("Total Patients", len(df))

st.markdown("---")

# ---------------- TABLE ----------------
st.subheader("Patient Records")

st.dataframe(df, use_container_width=True)