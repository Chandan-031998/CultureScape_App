import streamlit as st
from datetime import datetime
from utils import execute_query, generate_id

def render():
    st.title("💬 Share Your Feedback")
    st.markdown("We value your thoughts! Help us improve by sharing your experience.")

    # Fetch site names from database
    site_query = "SELECT site_id, site_name FROM CULTURAL_SITES ORDER BY site_name"
    site_data = execute_query(site_query, fetch_all=True)

    if site_data:
        site_dict = {name: sid for sid, name in site_data}
        selected_site = st.selectbox("🛕 Select Cultural Site", list(site_dict.keys()))

        rating = st.slider("⭐ Rate Your Experience", min_value=1, max_value=5, value=4)
        comment = st.text_area("💬 Your Feedback", max_chars=300, placeholder="What did you enjoy or suggest to improve?")

        if st.button("✅ Submit Feedback"):
            if comment.strip():
                feedback_id = generate_id()
                user_id = st.session_state.user_id
                site_id = site_dict[selected_site]
                today = datetime.now()

                query = """
                    INSERT INTO USER_FEEDBACK (feedback_id, user_id, site_id, rating, comment, feedback_date)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                execute_query(query, (
                    feedback_id, user_id, site_id, rating, comment, today
                ))

                st.success("🎉 Thank you! Your feedback has been recorded.")
            else:
                st.warning("⚠️ Please write a comment before submitting.")
    else:
        st.error("No cultural sites found in the database.")
