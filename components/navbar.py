import streamlit as st

def render_navbar():
    user = st.session_state.get("user_name", "Guest")
    role = st.session_state.get("user_role", "Visitor")

    st.markdown("""
        <style>
            .top-navbar {{
                background-color: #003366;
                padding: 0.75rem 1.2rem;
                border-radius: 0.5rem;
                margin-bottom: 1rem;
                color: white;
                display: flex;
                justify-content: space-between;
                align-items: center;
                font-family: 'Segoe UI', sans-serif;
            }}
            .top-navbar .brand {{
                font-size: 1.5rem;
                font-weight: bold;
                letter-spacing: 0.5px;
            }}
            .top-navbar .user-info {{
                font-size: 1rem;
            }}
        </style>
        <div class="top-navbar">
            <div class="brand">🌍 CultureScape India</div>
            <div class="user-info">
                👋 Welcome, <strong>{user}</strong> | Role: <strong>{role}</strong>
            </div>
        </div>
    """.format(user=user, role=role), unsafe_allow_html=True)