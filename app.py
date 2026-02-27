import streamlit as st

st.set_page_config(
    page_title="VitalShield AI",
    page_icon="🏥",
    layout="wide"
)

USERS = {
    "admin": {"password": "admin123", "role": "Admin"},
    "staff": {"password": "staff123", "role": "Staff"},
    "doctor": {"password": "doctor123", "role": "Doctor"},
    "patient": {"password": "patient123", "role": "Patient"}
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None

if not st.session_state.logged_in:

    st.title("🏥 VitalShield AI")
    st.subheader("Secure Hospital Login")
    st.markdown("---")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.role = USERS[username]["role"]
            st.rerun()
        else:
            st.error("Invalid credentials")

    st.stop()

st.sidebar.success(f"Logged in as {st.session_state.role}")

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.role = None
    st.rerun()

st.title("🏥 Welcome to VitalShield AI")
st.markdown("### Use the sidebar to navigate between modules.")
st.markdown("---")
st.info("Select a page from the left sidebar.")