import streamlit as st
from datetime import date, datetime
from utils import execute_query, generate_id

def render():
    st.title("🧮 Visitor Entry")
    st.markdown("Enter today's visitor count for any cultural site manually.")

    # Fetch site list
    site_query = "SELECT site_id, site_name FROM CULTURAL_SITES ORDER BY site_name"
    sites = execute_query(site_query, fetch_all=True)

    if not sites:
        st.warning("No cultural sites found. Please add sites in 'Manage Sites'.")
        return

    site_dict = {name: sid for sid, name in sites}
    selected_site = st.selectbox("🛕 Select Cultural Site", list(site_dict.keys()))
    visitor_count = st.number_input("👥 Number of Visitors Today", min_value=0, step=1)
    is_festival_day = st.checkbox("🎉 Mark as Festival Day")
    note = st.text_area("📝 Notes (optional)", max_chars=200)

    if st.button("✅ Submit Entry"):
        visit_id = generate_id()
        site_id = site_dict[selected_site]
        admin_id = st.session_state.user_id
        today = date.today()
        timestamp = datetime.now()

        insert_query = """
            INSERT INTO VISITOR_COUNTS (
                visit_id, site_id, date, visitor_count,
                is_festival_day, note, entered_by_admin_id, entry_timestamp
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            visit_id, site_id, today, visitor_count,
            is_festival_day, note, admin_id, timestamp
        )
        execute_query(insert_query, params)
        st.success(f"✅ Visitor count recorded for {selected_site} on {today}")
