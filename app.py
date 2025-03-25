# app.py
import streamlit as st
import pandas as pd
from scraper import scrape_tweets
from database import store_in_mongo
import json
from datetime import datetime, timedelta

# Streamlit GUI
st.set_page_config(page_title="Twitter Scraping Tool", layout="wide")
st.title("Twitter Scraping Tool")

# User inputs in sidebar
st.sidebar.header("Search Parameters")
keyword = st.sidebar.text_input("Enter Keyword or Hashtag", "#elonmusk")
default_end = datetime.now()
default_start = default_end - timedelta(days=7)
start_date = st.sidebar.date_input("Start Date", value=default_start)
end_date = st.sidebar.date_input("End Date", value=default_end)
limit = st.sidebar.number_input("Tweet Limit", min_value=1, max_value=500, value=100)

# Scrape button
if st.button("Scrape Tweets"):
    if keyword and start_date and end_date:
        with st.spinner("Scraping tweets..."):
            try:
                df = scrape_tweets(keyword, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"), limit)
                st.session_state["df"] = df
                st.success(f"Scraping completed! Found {len(df)} tweets")
            except Exception as e:
                st.error(str(e))
    else:
        st.warning("Please fill all fields")

# Display data and download options
if "df" in st.session_state:
    st.write("Scraped Data:")
    st.dataframe(st.session_state["df"], height=400)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Upload to Database"):
            try:
                store_in_mongo(st.session_state["df"], keyword)
                st.success("Data uploaded to MongoDB!")
            except Exception as e:
                st.error(str(e))
    
    with col2:
        csv = st.session_state["df"].to_csv(index=False)
        st.download_button(
            "Download as CSV",
            csv,
            f"{keyword}_tweets.csv",
            "text/csv",
            key="download-csv"
        )
    
    with col3:
        json_data = st.session_state["df"].to_json(orient="records")
        st.download_button(
            "Download as JSON",
            json_data,
            f"{keyword}_tweets.json",
            "application/json",
            key="download-json"
        )

if __name__ == "__main__":
    pass
