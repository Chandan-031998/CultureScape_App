import streamlit as st

def render():
    st.title("🌍 Welcome to CultureScape India")
    st.markdown("### Explore, Experience, and Preserve India's Cultural Legacy")

    st.markdown("---")

    # 🔔 Announcement or Highlight
    st.info("📢 Konark Dance Festival starts Dec 1 in Odisha — Plan your trip!")

    # 🔎 Quick Navigation Buttons
    st.markdown("### 🧭 Quick Access")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.page_link("pages/explore_sites.py", label="🎨 Explore Sites")
        st.page_link("pages/plan_trip.py", label="📆 Plan My Trip")
    with col2:
        st.page_link("pages/nearby_attractions.py", label="🗺️ Nearby Attractions")
        st.page_link("pages/passport.py", label="🏅 My Passport")
    with col3:
        st.page_link("pages/feedback.py", label="💬 Give Feedback")
        st.page_link("pages/cultural_stories.py", label="📚 Cultural Stories")

    st.markdown("---")

    # 🌟 Featured Cultural Highlights
    st.markdown("### 🌟 Featured Cultural Highlights")

    col_a, col_b = st.columns(2)
    with col_a:
        st.image("https://upload.wikimedia.org/wikipedia/commons/8/83/Konark_Sun_Temple_West_Side.jpg", use_column_width=True)
        st.markdown("**Konark Sun Temple (Odisha)**  \n13th-century chariot-shaped temple and UNESCO World Heritage Site.")

    with col_b:
        st.image("https://upload.wikimedia.org/wikipedia/commons/1/10/Bharatanatyam_Performance_DS.jpg", use_column_width=True)
        st.markdown("**Bharatanatyam (Tamil Nadu)**  \nClassical dance form that expresses mythological stories and devotion.")

    st.markdown("---")

    # 📊 Dummy Visitor Snapshot
    st.markdown("### 📊 Today's Visitor Snapshot (demo)")
    visitor_stats = {
        "Taj Mahal": 12450,
        "Konark Sun Temple": 3850,
        "Kathakali Center": 1220
    }

    for site, count in visitor_stats.items():
        st.write(f"📍 {site} — 👥 {count} visitors")

    st.markdown("---")

    # ♻️ Sustainable Travel Tip
    st.markdown("### 🌱 Sustainable Travel Tip of the Day")
    st.success("💧 Carry a refillable bottle and avoid single-use plastics at cultural sites.")

    st.markdown("📌 Start your journey through India's soul — one story, one site, one step at a time.")
