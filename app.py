import streamlit as st

import feedparser

from datetime import datetime



# Define RSS feed URLs for Northeast India news

rss_feeds = {

    'The Indian Express': 'https://indianexpress.com/section/north-east-india/feed/',

    'Northeast Now': 'https://nenow.in/feed'

}



# Function to fetch and parse RSS feeds

def fetch_news(feed_url):

    return feedparser.parse(feed_url)



# Streamlit app layout

st.set_page_config(page_title="Northeast India News", layout="wide")

st.title("📰 Northeast India News")

st.markdown("Stay updated with the latest news and events from Northeast India.")



# Sidebar for selecting news source

st.sidebar.title("News Sources")

selected_sources = st.sidebar.multiselect(

    "Select news sources:",

    options=list(rss_feeds.keys()),

    default=list(rss_feeds.keys())

)



# Fetch and display news from selected sources

for source in selected_sources:

    st.header(f"News from {source}")

    feed = fetch_news(rss_feeds[source])

    for entry in feed.entries[:5]:  # Display the top 5 news articles from each source

        published_time = datetime(*entry.published_parsed[:6]).strftime('%Y-%m-%d %H:%M:%S')

        st.subheader(entry.title)

        st.markdown(f"Published on: {published_time}")

        st.write(entry.summary)

        st.markdown(f"[Read more...]({entry.link})")

        st.markdown("---")
