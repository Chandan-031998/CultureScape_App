import streamlit as st
from datetime import datetime
from utils import execute_query

def render():
    st.title("📝 Review Suggested Cultural Gems")
    st.markdown("Moderate hidden cultural sites suggested by travellers.")

    # Fetch pending suggestions
    fetch_query = """
        SELECT suggestion_id, user_id, suggestion_title, description, location, suggestion_date
        FROM SUGGESTIONS
        WHERE status = 'pending'
        ORDER BY suggestion_date DESC
    """
    data = execute_query(fetch_query, fetch_all=True)

    if not data:
        st.info("📭 No pending suggestions to review.")
        return

    for row in data:
        suggestion_id, user_id, title, description, location, date_suggested = row
        with st.expander(f"📍 {title} – {location}"):
            st.write(f"🧑 Suggested By: `{user_id}`")
            st.write(f"🗓️ Date: {date_suggested}")
            st.write(f"💬 Description:\n\n{description}")

            admin_response = st.text_area(f"✏️ Admin Response for '{title}'", key=f"resp_{suggestion_id}")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Approve", key=f"approve_{suggestion_id}"):
                    query = """
                        UPDATE SUGGESTIONS
                        SET status = 'approved',
                            admin_response = %s,
                            action_date = %s
                        WHERE suggestion_id = %s
                    """
                    execute_query(query, (admin_response, datetime.now(), suggestion_id))
                    st.success(f"✅ '{title}' approved.")
                    st.experimental_rerun()

            with col2:
                if st.button("❌ Reject", key=f"reject_{suggestion_id}"):
                    query = """
                        UPDATE SUGGESTIONS
                        SET status = 'rejected',
                            admin_response = %s,
                            action_date = %s
                        WHERE suggestion_id = %s
                    """
                    execute_query(query, (admin_response, datetime.now(), suggestion_id))
                    st.warning(f"❌ '{title}' rejected.")
                    st.experimental_rerun()
