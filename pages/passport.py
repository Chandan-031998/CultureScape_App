import streamlit as st
import pandas as pd
from utils import execute_query

def render():
    st.title("🏅 My Digital Passport")
    st.markdown("Your personal badge collection for exploring and learning about India's cultural heritage.")

    # Fetch passport data from DB
    query = """
        SELECT dp.site_id, cs.site_name, dp.earned_badge, dp.earn_type, dp.date_earned
        FROM DIGITAL_PASSPORT dp
        JOIN CULTURAL_SITES cs ON dp.site_id = cs.site_id
        WHERE dp.user_id = %s
        ORDER BY dp.date_earned DESC
    """
    user_id = st.session_state.user_id
    results = execute_query(query, (user_id,), fetch_all=True)

    if results:
        df = pd.DataFrame(results, columns=["Site ID", "Site Name", "Badge", "Type", "Date"])

        # Badge Summary
        total = len(df)
        visited = len(df[df["Type"] == "visited"])
        learned = total - visited

        col1, col2, col3 = st.columns(3)
        col1.metric("🏛️ Total Badges", total)
        col2.metric("✅ Visited", visited)
        col3.metric("📖 Learned", learned)

        # Badge Filter
        badge_type = st.selectbox("🔎 Filter by Badge Type", ["All", "visited", "learned"])
        if badge_type != "All":
            df = df[df["Type"] == badge_type]

        # Badge Cards
        st.markdown("### 🧭 My Badge Collection")
        for i in range(0, len(df), 2):
            col_a, col_b = st.columns(2)
            for idx, col in zip([i, i+1], [col_a, col_b]):
                if idx < len(df):
                    row = df.iloc[idx]
                    with col.expander(f"🏅 {row['Badge']} – {row['Site Name']}"):
                        st.write(f"📍 Type: {row['Type'].capitalize()}")
                        st.write(f"🗓️ Earned on: {row['Date']}")
                        st.progress(100)

    else:
        st.warning("📭 No badges yet. Start exploring or learning about cultural sites to earn your first stamp!")

    st.markdown("---")
    st.markdown("📌 Badges are earned when you mark a site as 'visited' or when you explore stories and facts about a place.")
