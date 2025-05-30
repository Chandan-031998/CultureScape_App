import streamlit as st
import pandas as pd
import plotly.express as px
from components.navbar import render_navbar
from utils import execute_query

def render():
    st.set_page_config(layout="wide")
    render_navbar()
    st.title("📂 Government Schemes Dashboard")

# -------------------- Admin Dashboard ---------------------
def admin_dashboard():
    st.set_page_config(layout="wide")
    render_navbar()
    st.title("📊 Admin Analytics Dashboard")

    # Query Snowflake data using execute_query wrapper
    funding_query = "SELECT * FROM FUNDING_DATA"
    monthly_query = "SELECT * FROM MONTHLY_DATA"
    sanction_query = "SELECT * FROM SANCTION_DATA"

    funding_df = execute_query(funding_query)
    monthly_df = execute_query(monthly_query)
    sanction_df = execute_query(sanction_query)

    # -------- FUNDING DATA ANALYSIS --------
    st.subheader("💸 Top Funded States")
    top_funding = (
        funding_df.groupby("STATE")["VALUE"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .head(10)
    )
    fig1 = px.bar(
        top_funding,
        x="VALUE",
        y="STATE",
        orientation="h",
        title="Top 10 States by Total Funding",
        color="VALUE",
        color_continuous_scale="Blues"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # -------- GRANT TRENDS --------
    st.subheader("📅 Monthly Grant Trends")
    month_trend = (
        monthly_df.groupby("MONTH")["VALUE"]
        .sum()
        .reset_index()
        .sort_values(by="VALUE", ascending=False)
    )
    fig2 = px.line(
        month_trend,
        x="MONTH",
        y="VALUE",
        markers=True,
        title="Monthly Travel Grant Trends"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # -------- SANCTION ANALYSIS --------
    st.subheader("🗺️ Sanctioned Tourism Projects")
    top_sanction = (
        sanction_df.groupby("STATE")["COST"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .head(10)
    )
    fig3 = px.bar(
        top_sanction,
        x="COST",
        y="STATE",
        orientation="h",
        title="Top 10 States by Sanctioned Project Cost",
        color="COST",
        color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig3, use_container_width=True)

    # -------- CROSS-ANALYSIS: FUNDING vs SANCTION --------
    st.subheader("🔁 Comparison: Funding vs Sanction")
    funding_vs_sanction = (
        funding_df.groupby("STATE")["VALUE"].sum()
        .to_frame("Total Funding")
        .join(sanction_df.groupby("STATE")["COST"].sum().to_frame("Total Sanction"), how="outer")
        .fillna(0).reset_index()
    )
    fig4 = px.scatter(
        funding_vs_sanction,
        x="Total Funding",
        y="Total Sanction",
        text="STATE",
        size="Total Sanction",
        title="State-wise Funding vs Sanction Analysis",
        hover_name="STATE"
    )
    st.plotly_chart(fig4, use_container_width=True)

    # -------- INSIGHTS --------
    st.subheader("💡 Recommendations")
    with st.expander("🔎 Admin Suggestions"):
        st.markdown("""
        - 🚀 Increase promotion for high-funding, low-tourism states
        - 🧭 Prioritize states with high sanctions but low grants
        - 🌿 Align monthly trends with local festivals and tourism peaks
        - 📍 Target underrepresented regions with cultural potential
        - 📊 Use this data to design seasonal and regional grant strategies
        - 📌 Cross-verify states where high funding hasn't translated into high sanctioning or projects
        - 📈 Consider reallocating funds from low-impact states to emerging tourism zones
        - 📉 Monitor underperforming months for tourism and investigate causes (e.g., weather, holidays)
        - 🎯 Recommend targeted outreach in states like Tripura, Sikkim, and Jharkhand which show low metrics
        """)

    st.caption("Powered by Streamlit + Plotly | Backed by Snowflake")

# Call function if run as script
if __name__ == "__main__":
    admin_dashboard()
