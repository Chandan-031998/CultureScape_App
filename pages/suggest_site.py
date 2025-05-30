import streamlit as st
from datetime import datetime
from utils import execute_query, generate_id

def render():
    st.title("🌄 Suggest a Cultural Gem")
    st.markdown("Know a hidden cultural site or tradition? Help us discover it!")

    # Form Inputs
    title = st.text_input("📝 Title of the Site")
    location = st.text_input("📍 Location (City, District, or Coordinates)")
    description = st.text_area("💬 Describe its Cultural Significance", max_chars=500)

    # Submit Suggestion
    if st.button("📤 Submit Suggestion"):
        if title.strip() and location.strip() and description.strip():
            suggestion_id = generate_id()
            user_id = st.session_state.user_id
            suggestion_date = datetime.now()

            query = """
                INSERT INTO SUGGESTIONS (
                    suggestion_id, user_id, suggestion_title,
                    description, location, status, suggestion_date
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            params = (
                suggestion_id, user_id, title, description,
                location, 'pending', suggestion_date
            )
            execute_query(query, params)
            st.success("🎉 Thank you! Your suggestion has been submitted for review.")
        else:
            st.warning("⚠️ Please fill in all fields before submitting.")

    st.markdown("---")
    st.markdown("📌 Submitted suggestions will be reviewed by the tourism department before approval.")
