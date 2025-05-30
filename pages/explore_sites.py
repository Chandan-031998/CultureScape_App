import streamlit as st
import pandas as pd
from utils import execute_query

def render():
    st.title("🎨 Explore Cultural Sites")
    st.markdown("Browse and discover India's most fascinating cultural hotspots.")

    # 🔄 Fetch data from database
    query = """
        SELECT site_id, site_name, state, region, art_form, popularity_score,
               latitude, longitude, description, image_url
        FROM CULTURAL_SITES
        ORDER BY popularity_score DESC
    """
    data = execute_query(query, fetch_all=True)

    if not data:
        st.warning("No cultural sites found in the database.")
        return

    # Create DataFrame
    df = pd.DataFrame(data, columns=[
        "Site ID", "Site Name", "State", "Region", "Art Form",
        "Popularity", "Latitude", "Longitude", "Description", "Image URL"
    ])

    # 🔎 Filters
    with st.expander("🔍 Filter Options"):
        state_filter = st.selectbox("Filter by State", ["All"] + sorted(df["State"].unique()))
        art_filter = st.selectbox("Filter by Art Form", ["All"] + sorted(df["Art Form"].unique()))
        keyword = st.text_input("Search by Keyword")

    # 🔃 Apply filters
    filtered_df = df.copy()
    if state_filter != "All":
        filtered_df = filtered_df[filtered_df["State"] == state_filter]
    if art_filter != "All":
        filtered_df = filtered_df[filtered_df["Art Form"] == art_filter]
    if keyword:
        filtered_df = filtered_df[
            filtered_df["Site Name"].str.contains(keyword, case=False) |
            filtered_df["Description"].str.contains(keyword, case=False)
        ]

    # 🧾 Display Results
    st.markdown("### 📌 Results")

    if filtered_df.empty:
        st.info("No cultural sites match your filter criteria.")
    else:
        for _, row in filtered_df.iterrows():
            with st.container():
                col_img, col_info = st.columns([1, 2])
                with col_img:
                    if row["Image URL"]:
                        st.image(row["Image URL"], use_column_width=True)
                with col_info:
                    st.subheader(f"{row['Site Name']} ({row['State']})")
                    st.caption(f"🧭 Region: {row['Region']} | 🎭 Art: {row['Art Form']} | ⭐ Popularity: {row['Popularity']}")
                    st.write(row["Description"])
                    st.markdown(f"[📍 View on Google Maps](https://www.google.com/maps/search/?api=1&query={row['Latitude']},{row['Longitude']})")

                st.markdown("---")
