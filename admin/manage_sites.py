import streamlit as st
import pandas as pd
from datetime import datetime
from utils import execute_query, generate_id

def render():
    st.title("🛕 Manage Cultural Sites")
    st.markdown("Add new cultural sites or edit existing ones.")

    tab1, tab2 = st.tabs(["➕ Add Site", "📝 Manage Sites"])

    # ------------------------ TAB 1: Add Site ------------------------
    with tab1:
        st.subheader("➕ Add New Cultural Site")

        name = st.text_input("Site Name")
        state = st.text_input("State")
        region = st.selectbox("Region", ["North", "South", "East", "West", "Central", "North-East"])
        art_form = st.text_input("Cultural Art Form")
        popularity = st.slider("Popularity Score", 1, 100, 50)
        latitude = st.number_input("Latitude", format="%.6f")
        longitude = st.number_input("Longitude", format="%.6f")
        image_url = st.text_input("Image URL")
        description = st.text_area("Site Description", max_chars=500)

        if st.button("✅ Add Site"):
            if all([name.strip(), state.strip(), art_form.strip(), description.strip()]):
                site_id = generate_id()
                admin_id = st.session_state.user_id
                now = datetime.now()

                insert_query = """
                    INSERT INTO CULTURAL_SITES (
                        site_id, site_name, state, region, art_form, popularity_score,
                        latitude, longitude, description, image_url,
                        added_by_admin_id, date_added, last_modified
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                params = (
                    site_id, name, state, region, art_form, popularity,
                    latitude, longitude, description, image_url,
                    admin_id, now.date(), now
                )
                execute_query(insert_query, params)
                st.success(f"✅ Site '{name}' added successfully.")
            else:
                st.warning("⚠️ Please fill all required fields.")

    # ------------------------ TAB 2: Edit/Delete Site ------------------------
    with tab2:
        st.subheader("🛠️ Edit or Delete Sites")

        fetch_query = """
            SELECT site_id, site_name, state, region, art_form, popularity_score
            FROM CULTURAL_SITES
            ORDER BY site_name
        """
        data = execute_query(fetch_query, fetch_all=True)

        if not data:
            st.info("📭 No sites found.")
            return

        df = pd.DataFrame(data, columns=["ID", "Name", "State", "Region", "Art", "Popularity"])
        selected = st.selectbox("Select Site to Manage", df["Name"].tolist())
        site = df[df["Name"] == selected].iloc[0]

        name = st.text_input("Edit Name", value=site["Name"])
        state = st.text_input("Edit State", value=site["State"])
        region = st.selectbox("Edit Region", ["North", "South", "East", "West", "Central", "North-East"], index=["North", "South", "East", "West", "Central", "North-East"].index(site["Region"]))
        art = st.text_input("Edit Art Form", value=site["Art"])
        popularity = st.slider("Edit Popularity", 1, 100, int(site["Popularity"]))

        col1, col2 = st.columns(2)

        with col1:
            if st.button("💾 Update Site"):
                update_query = """
                    UPDATE CULTURAL_SITES
                    SET site_name = %s, state = %s, region = %s,
                        art_form = %s, popularity_score = %s, last_modified = %s
                    WHERE site_id = %s
                """
                execute_query(update_query, (
                    name, state, region, art, popularity, datetime.now(), site["ID"]
                ))
                st.success(f"✅ '{name}' updated successfully.")
                st.experimental_rerun()

        with col2:
            if st.button("🗑️ Delete Site"):
                delete_query = "DELETE FROM CULTURAL_SITES WHERE site_id = %s"
                execute_query(delete_query, (site["ID"],))
                st.warning(f"🗑️ '{site['Name']}' deleted successfully.")
                st.experimental_rerun()
