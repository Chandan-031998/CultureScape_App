import hashlib
import uuid
from datetime import datetime, date
import streamlit as st
from config import get_connection

# 🔐 Hash password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# 🆔 Generate a UUID for primary keys
def generate_id():
    return str(uuid.uuid4())

# 📅 Return today's date in YYYY-MM-DD format
def get_today():
    return date.today()

# 🔁 Execute Snowflake SQL with safe handling
def execute_query(query, params=None, fetch_one=False, fetch_all=False):
    conn = get_connection()
    cur = conn.cursor()
    result = None
    try:
        cur.execute(query, params)
        if fetch_one:
            result = cur.fetchone()
        elif fetch_all:
            result = cur.fetchall()
        conn.commit()
    except Exception as e:
        st.error(f"❌ Database error: {e}")
    finally:
        cur.close()
        conn.close()
    return result

# 🔓 Clear session state and logout
def logout_user():
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.user_role = None
    st.session_state.user_name = ""
    st.experimental_rerun()
