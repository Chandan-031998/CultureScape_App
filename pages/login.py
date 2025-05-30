import streamlit as st
from utils import execute_query, hash_password

def login_page():
    st.subheader("🔐 Login to CultureScape")

    email = st.text_input("📧 Email", key="login_email")
    password = st.text_input("🔒 Password", type="password", key="login_password")

    if st.button("➡️ Login", key="login_button"):
        if not email or not password:
            st.warning("⚠️ Please enter both email and password.")
            return

        # Fetch user
        query = "SELECT user_id, name, role, password_hash FROM USERS WHERE email = %s AND status = 'active'"
        result = execute_query(query, (email,), fetch_one=True)

        if result:
            user_id, name, role, stored_hash = result
            if hash_password(password) == stored_hash:
                # Set session state
                st.session_state.logged_in = True
                st.session_state.user_id = user_id
                st.session_state.user_name = name
                st.session_state.user_role = role
                st.success(f"✅ Welcome, {name}!")
                st.experimental_rerun()
            else:
                st.error("❌ Incorrect password.")
        else:
            st.error("❌ No account found with that email.")
