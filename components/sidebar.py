import streamlit as st

def render_sidebar():
    # Optional: Display app logo
    st.sidebar.image("assets/logo.png", use_column_width=True)

    st.sidebar.markdown("## 🧭 Navigation")

    role = st.session_state.get("user_role", "Visitor")

    if role == "admin":
        menu = [
            "📊 Dashboard",
            "🧮 Visitor Entry",
            "🛕 Manage Sites",
            "📝 Review Suggestions",
            "📄 Upload Docs",
            "🗺️ Heatmap",

            "📈 Feedback Trends",
           
        ]
    elif role == "user":
        menu = [
            "🎨 Explore Sites",
            "📆 Plan My Trip",
            "🗺️ Nearby Attractions",
            "🏅 My Passport",
            "💬 Give Feedback",
            "🌄 Suggest a Site",
            "📚 Cultural Stories",
            "🌱 Sustainable Tips"
        ]
    else:
        menu = ["🔐 Login", "📝 Register"]

    choice = st.sidebar.radio("Select a Page", menu)
    return choice
