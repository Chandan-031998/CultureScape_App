import streamlit as st
from datetime import date
from utils import execute_query, generate_id, hash_password

def register_page():
    st.subheader("📝 Register to CultureScape")

    name = st.text_input("👤 Full Name", key="register_name")
    email = st.text_input("📧 Email", key="register_email")
    password = st.text_input("🔒 Password", type="password", key="register_password")
    confirm = st.text_input("🔒 Confirm Password", type="password", key="register_confirm")
    role = st.selectbox("🎭 Register As", ["user", "admin"], key="register_role")

    if st.button("✅ Register", key="register_button"):
        if not all([name, email, password, confirm]):
            st.warning("⚠️ All fields are required.")
        elif password != confirm:
            st.error("❌ Passwords do not match.")
        else:
            # Check if email exists
            check_query = "SELECT COUNT(*) FROM USERS WHERE email = %s"
            exists = execute_query(check_query, (email,), fetch_one=True)[0]

            if exists > 0:
                st.error("❌ Email already registered.")
            else:
                user_id = generate_id()
                joined = date.today()
                hashed_pw = hash_password(password)

                insert_query = """
                    INSERT INTO USERS (user_id, name, email, password_hash, role, joined_date, status)
                    VALUES (%s, %s, %s, %s, %s, %s, 'active')
                """
                execute_query(insert_query, (user_id, name, email, hashed_pw, role, joined))
                st.success("🎉 Registration successful! Please log in.")
