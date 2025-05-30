import streamlit as st
import pandas as pd
import plotly.express as px
from utils import execute_query

def render():
    st.title("📊 Admin Dashboard")
    st.markdown("Monitor visitor data, feedback, and site performance across CultureScape.")

    st.markdown("---")

    # 📌 Fetch Summary Metrics
    query_total_visitors = "SELECT SUM(visitor_count) FROM VISITOR_COUNTS"
    query_total_sites = "SELECT COUNT(*) FROM CULTURAL_SITES"
    query_total_feedback = "SELECT COUNT(*) FROM USER_FEEDBACK"
    query_pending_suggestions = "SELECT COUNT(*) FROM SUGGESTIONS WHERE status = 'pending'"

    total_visitors = execute_query(query_total_visitors, fetch_one=True)[0] or 0
    total_sites = execute_query(query_total_sites, fetch_one=True)[0] or 0
    total_feedback = execute_query(query_total_feedback, fetch_one=True)[0] or 0
    total_pending = execute_query(query_pending_suggestions, fetch_one=True)[0] or 0

    # 💡 KPI Display
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👣 Total Visitors", f"{total_visitors:,}")
    col2.metric("🛕 Sites", total_sites)
    col3.metric("💬 Feedback Received", total_feedback)
    col4.metric("📝 Pending Suggestions", total_pending)

    st.markdown("### 📈 Monthly Visitor Trends")
    trend_query = """
        SELECT DATE_TRUNC('month', date) AS month, SUM(visitor_count) AS visitors
        FROM VISITOR_COUNTS
        GROUP BY month
        ORDER BY month
    """
    trend_data = execute_query(trend_query, fetch_all=True)
    if trend_data:
        trend_df = pd.DataFrame(trend_data, columns=["Month", "Visitors"])
        trend_df["Month"] = pd.to_datetime(trend_df["Month"])
        fig1 = px.line(trend_df, x="Month", y="Visitors", title="Monthly Visitors", markers=True)
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.info("No visitor data found.")

    st.markdown("### 🌟 Site-wise Average Rating")
    rating_query = """
        SELECT cs.site_name, ROUND(AVG(uf.rating),2) AS avg_rating
        FROM USER_FEEDBACK uf
        JOIN CULTURAL_SITES cs ON uf.site_id = cs.site_id
        GROUP BY cs.site_name
        ORDER BY avg_rating DESC
        LIMIT 10
    """
    rating_data = execute_query(rating_query, fetch_all=True)
    if rating_data:
        rating_df = pd.DataFrame(rating_data, columns=["Site", "Average Rating"])
        fig2 = px.bar(rating_df, x="Average Rating", y="Site", orientation="h", title="Top Rated Sites")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("No feedback ratings available.")

    st.markdown("### 🔝 Top 5 Most Visited Sites")
    top_sites_query = """
        SELECT cs.site_name, SUM(vc.visitor_count) AS total_visitors
        FROM VISITOR_COUNTS vc
        JOIN CULTURAL_SITES cs ON vc.site_id = cs.site_id
        GROUP BY cs.site_name
        ORDER BY total_visitors DESC
        LIMIT 5
    """
    top_data = execute_query(top_sites_query, fetch_all=True)
    if top_data:
        top_df = pd.DataFrame(top_data, columns=["Site", "Visitors"])
        st.table(top_df)
    else:
        st.info("No site-wise visitor data available.")

    # 🔍 Integration of FUNDING_DATA
    st.markdown("### 💸 Top Funded States")
    funding_query = "SELECT STATE, SUM(VALUE) AS total_funding FROM FUNDING_DATA GROUP BY STATE ORDER BY total_funding DESC LIMIT 10"
    funding_data = execute_query(funding_query, fetch_all=True)
    if funding_data:
        funding_df = pd.DataFrame(funding_data, columns=["State", "Total Funding"])
        fig3 = px.bar(funding_df, x="Total Funding", y="State", orientation="h", title="Top Funded States", color="Total Funding")
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("No funding data available.")

    # 📅 Integration of MONTHLY_DATA
    st.markdown("### 🗓️ Monthly Grant Summary")
    monthly_query = "SELECT MONTH, SUM(VALUE) AS total_grants FROM MONTHLY_DATA GROUP BY MONTH ORDER BY MONTH"
    monthly_data = execute_query(monthly_query, fetch_all=True)
    if monthly_data:
        monthly_df = pd.DataFrame(monthly_data, columns=["Month", "Total Grants"])
        fig4 = px.line(monthly_df, x="Month", y="Total Grants", title="Monthly Grant Allocation", markers=True)
        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.info("No monthly grant data available.")

    # 📌 Integration of SANCTION_DATA
    st.markdown("### 🏛️ Sanctioned Projects by State")
    sanction_query = "SELECT STATE, SUM(COST) AS total_cost FROM SANCTION_DATA GROUP BY STATE ORDER BY total_cost DESC LIMIT 10"
    sanction_data = execute_query(sanction_query, fetch_all=True)
    if sanction_data:
        sanction_df = pd.DataFrame(sanction_data, columns=["State", "Total Sanctioned Cost"])
        fig5 = px.bar(sanction_df, x="Total Sanctioned Cost", y="State", orientation="h", title="Top Sanctioned States", color="Total Sanctioned Cost")
        st.plotly_chart(fig5, use_container_width=True)
    else:
        st.info("No sanction data available.")

    st.markdown("---")
    st.caption("📌 All insights are based on live data from Snowflake.")
