import streamlit as st
import importlib
from components.navbar import render_navbar
from components.sidebar import render_sidebar
from pages import login, register

# 🚀 Set page configuration with theme
st.set_page_config(
    page_title="CultureScape India",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🎨 Inject custom CSS for background, theme, and responsiveness
st.markdown("""
    <style>
    body {
        background-image: url('https://images.unsplash.com/photo-1590490360182-df7f170d30d2');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }

    .stApp {
        background-color: rgba(255, 255, 255, 0.92);
        padding: 1rem;
        border-radius: 10px;
    }

    h1, h2, h3, h4 {
        color: #1A5276;
        font-family: 'Segoe UI', sans-serif;
    }

    .stButton > button {
        background-color: #154360;
        color: white;
        border-radius: 8px;
        padding: 6px 14px;
    }

    .stButton > button:hover {
        background-color: #21618C;
        color: #fff;
    }

    .css-1d391kg, .css-1v3fvcr {
        background-color: #F5F5F5 !important;
    }

    .responsive-img {
        max-width: 100%;
        height: auto;
        border-radius: 10px;
    }

    </style>
""", unsafe_allow_html=True)

# 🌄 Banner Image


# 🌐 Session State Initialization
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.user_role = None
    st.session_state.user_name = ""

# 🔝 Top Navbar
render_navbar()

# 🔐 Show login/register tabs if not logged in
if not st.session_state.logged_in:
    tabs = st.tabs(["🔐 Login", "📝 Register"])
    with tabs[0]:
        login.login_page()
    with tabs[1]:
        register.register_page()
    st.stop()

# 📚 Sidebar Navigation
selected_page = render_sidebar()

# 🧭 Route map
page_routes = {
    # User Pages
    "🎨 Explore Sites": "pages.explore_sites",
    "📆 Plan My Trip": "pages.plan_trip",
    "🗺️ Nearby Attractions": "pages.nearby_attractions",
    "🏅 My Passport": "pages.passport",
    "💬 Give Feedback": "pages.feedback",
    "🌄 Suggest a Site": "pages.suggest_site",
    "📚 Cultural Stories": "pages.cultural_stories",
    "🌱 Sustainable Tips": "pages.sustainable_tips",

    # Admin Pages
    "📊 Dashboard": "admin.dashboard",
    "🧮 Visitor Entry": "admin.visitor_entry",
    "🛕 Manage Sites": "admin.manage_sites",
    "📝 Review Suggestions": "admin.suggestions_review",
    "📄 Upload Docs": "admin.upload_docs",
    "📂 Government Schemes": "admin.gov_dashboard",
    "📈 Visitor Insights": "admin.visitor_dash",
    "🌐 Tourism Sanctions": "admin.tourism_dash",
    "🗺️ Heatmap": "admin.heatmap",
    "📈 Feedback Trends": "admin.feedback_trends",
}

# ▶️ Render selected page
if selected_page in page_routes:
    try:
        module = importlib.import_module(page_routes[selected_page])
        module.render()
    except Exception as e:
        st.error(f"⚠️ Error loading {selected_page}: {e}")
else:
    st.warning("⚠️ Page not found or not authorized.")

# 🚪 Logout Option
st.sidebar.markdown("---")
if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.user_role = None
    st.session_state.user_name = ""
    st.experimental_rerun()
