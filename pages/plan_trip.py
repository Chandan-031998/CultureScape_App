import streamlit as st
import pandas as pd
import plotly.express as px

def render():
    st.title("📆 Plan My Trip")
    st.markdown("Use insights and trends to visit cultural sites at the best time of year!")

    # 🎯 Demo states and sites (replace with dynamic DB values)
    states = {
        "Uttar Pradesh": ["Taj Mahal", "Fatehpur Sikri"],
        "Kerala": ["Kathakali Center", "Mattancherry Palace"],
        "Odisha": ["Konark Sun Temple", "Puri Jagannath Temple"]
    }

    selected_state = st.selectbox("📍 Select State", list(states.keys()))
    selected_site = st.selectbox("🛕 Select Cultural Site", states[selected_state])

    st.markdown("---")

    # 🗓️ Recommended Visit Times (static mapping)
    best_seasons = {
        "Taj Mahal": "October to March",
        "Fatehpur Sikri": "November to February",
        "Kathakali Center": "December to March",
        "Mattancherry Palace": "August to December",
        "Konark Sun Temple": "November to January",
        "Puri Jagannath Temple": "June (Rath Yatra), otherwise Oct–Feb"
    }

    if selected_site in best_seasons:
        st.success(f"✅ Best Time to Visit: {best_seasons[selected_site]}")

    # 📊 Dummy Visitor Trend Data (replace with real Snowflake query)
    trend_df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "Visitors": [5400, 4900, 5100, 4000, 3000, 2800, 2600, 2700, 3100, 4200, 4800, 5300]
    })

    fig = px.line(trend_df, x="Month", y="Visitors", title=f"📊 Monthly Visitor Trend – {selected_site}",
                  markers=True, line_shape="spline")
    fig.update_layout(xaxis_title="Month", yaxis_title="Visitors", height=400)
    st.plotly_chart(fig, use_container_width=True)

    # 🧳 Travel Tips
    st.markdown("### 🧳 Travel Tips")
    st.info("🚉 Book trains/flights early for peak months (Oct–Mar).")
    st.info("🧥 Carry warm clothes for northern sites during winter.")
    st.info("📸 Visit during golden hours (early morning/evening) for best photos.")

    # 💡 AI-style Suggestion
    st.markdown("### 🤖 Smart Suggestion")
    st.success(f"Since you're visiting {selected_site}, consider exploring other cultural gems in {selected_state}!")

    st.markdown("---")
    st.caption("📌 Trend data shown is based on historical patterns. For daily visitor updates, check the 'Explore Sites' page.")
