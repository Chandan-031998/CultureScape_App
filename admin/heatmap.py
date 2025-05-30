import streamlit as st
import pandas as pd
import pydeck as pdk
from utils import execute_query

def render():
    st.title("🗺️ Tourism Heatmap")
    st.markdown("Visualize footfall across India’s cultural sites based on visitor counts.")

    # Fetch total visitors per site with location info
    query = """
        SELECT cs.site_id, cs.site_name, cs.latitude, cs.longitude,
               COALESCE(SUM(vc.visitor_count), 0) AS total_visitors
        FROM CULTURAL_SITES cs
        LEFT JOIN VISITOR_COUNTS vc ON cs.site_id = vc.site_id
        GROUP BY cs.site_id, cs.site_name, cs.latitude, cs.longitude
    """
    data = execute_query(query, fetch_all=True)

    if not data:
        st.warning("📭 No site or visitor data available.")
        return

    df = pd.DataFrame(data, columns=["Site ID", "Site Name", "Latitude", "Longitude", "Total Visitors"])
    if df.empty:
        st.warning("No data to show.")
        return

    # Display table of top/bottom sites
    st.markdown("### 🔝 Most Visited Sites")
    top_5 = df.sort_values(by="Total Visitors", ascending=False).head(5)[["Site Name", "Total Visitors"]]
    st.dataframe(top_5, use_container_width=True)

    st.markdown("### 🔻 Least Visited Sites")
    least_5 = df[df["Total Visitors"] > 0].sort_values(by="Total Visitors", ascending=True).head(5)[["Site Name", "Total Visitors"]]
    st.dataframe(least_5, use_container_width=True)

    # Render heatmap
    st.markdown("### 🔥 Visitor Heatmap")

    layer = pdk.Layer(
        "HeatmapLayer",
        data=df,
        get_position='[Longitude, Latitude]',
        get_weight="Total Visitors",
        radiusPixels=60
    )

    view_state = pdk.ViewState(
        latitude=df["Latitude"].mean(),
        longitude=df["Longitude"].mean(),
        zoom=4.5,
        pitch=40
    )

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=view_state,
        layers=[layer],
        tooltip={"text": "{Site Name}\n👥 {Total Visitors} visitors"}
    ))

    st.caption("📌 Heatmap powered by real-time data from Snowflake.")
