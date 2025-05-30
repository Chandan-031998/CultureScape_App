import streamlit as st
import pandas as pd
import plotly.express as px
from utils import execute_query

def render():
    st.title("📈 Feedback Trends")
    st.markdown("Understand user sentiment and feedback activity across cultural sites.")

    # 📊 Site-wise Average Ratings
    st.markdown("### 🌟 Average Ratings per Site")
    avg_rating_query = """
        SELECT cs.site_name, ROUND(AVG(uf.rating),2) AS avg_rating
        FROM USER_FEEDBACK uf
        JOIN CULTURAL_SITES cs ON uf.site_id = cs.site_id
        GROUP BY cs.site_name
        ORDER BY avg_rating DESC
    """
    rating_data = execute_query(avg_rating_query, fetch_all=True)

    if rating_data:
        rating_df = pd.DataFrame(rating_data, columns=["Site", "Average Rating"])
        fig = px.bar(rating_df, x="Average Rating", y="Site", orientation='h', height=400)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No feedback available for rating analysis.")

    # 📈 Monthly Rating Trend
    st.markdown("### 📆 Monthly Rating Trend")
    trend_query = """
        SELECT DATE_TRUNC('month', feedback_date) AS month, ROUND(AVG(rating),2) AS avg_rating
        FROM USER_FEEDBACK
        GROUP BY month
        ORDER BY month
    """
    trend_data = execute_query(trend_query, fetch_all=True)
    if trend_data:
        trend_df = pd.DataFrame(trend_data, columns=["Month", "Average Rating"])
        trend_df["Month"] = pd.to_datetime(trend_df["Month"])
        fig2 = px.line(trend_df, x="Month", y="Average Rating", markers=True)
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("No time-based feedback found.")

    # 📋 Most Reviewed Sites
    st.markdown("### 🔝 Most Reviewed Sites")
    review_query = """
        SELECT cs.site_name, COUNT(*) AS feedback_count
        FROM USER_FEEDBACK uf
        JOIN CULTURAL_SITES cs ON uf.site_id = cs.site_id
        GROUP BY cs.site_name
        ORDER BY feedback_count DESC
        LIMIT 5
    """
    review_data = execute_query(review_query, fetch_all=True)
    if review_data:
        review_df = pd.DataFrame(review_data, columns=["Site", "Feedback Count"])
        st.dataframe(review_df, use_container_width=True)

    # 💬 Most Recent Comments
    st.markdown("### 🗣️ Recent Feedback Comments")
    comment_query = """
        SELECT cs.site_name, uf.rating, uf.comment, uf.feedback_date
        FROM USER_FEEDBACK uf
        JOIN CULTURAL_SITES cs ON uf.site_id = cs.site_id
        ORDER BY uf.feedback_date DESC
        LIMIT 10
    """
    comments = execute_query(comment_query, fetch_all=True)
    if comments:
        for site, rating, comment, fdate in comments:
            with st.expander(f"{site} – ⭐ {rating}"):
                st.write(f"🗓️ {fdate.strftime('%Y-%m-%d')}")
                st.write(f"💬 {comment}")
    else:
        st.info("No feedback comments submitted yet.")
