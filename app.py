import streamlit as st
import feedparser
from googletrans import Translator

# Define RSS feed URLs for each Northeast Indian state
rss_feeds = {
    "Arunachal Pradesh": "https://nenow.in/category/north-east-news/arunachal-pradesh/feed",
    "Assam": "https://nenow.in/category/north-east-news/assam/feed",
    "Manipur": "https://nenow.in/category/north-east-news/manipur/feed",
    "Meghalaya": "https://nenow.in/category/north-east-news/meghalaya/feed",
    "Mizoram": "https://nenow.in/category/north-east-news/mizoram/feed",
    "Nagaland": "https://nenow.in/category/north-east-news/nagaland/feed",
    "Sikkim": "https://nenow.in/category/north-east-news/sikkim/feed",
    "Tripura": "https://nenow.in/category/north-east-news/tripura/feed"
}

# Function to fetch and parse RSS feeds
def fetch_news(feed_url):
    return feedparser.parse(feed_url)

# Function to translate text to Hindi
def translate_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, dest="hi")
    return translation.text

# Streamlit UI Layout
st.set_page_config(page_title="📰 Northeast India News", layout="wide")
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>📰 पूर्वोत्तर भारत समाचार</h1>", unsafe_allow_html=True)
st.write("नवीनतम समाचारों के लिए राज्य चुनें।")

# Sidebar for state selection
st.sidebar.title("🌍 राज्य चुनें")
selected_states = st.sidebar.multiselect(
    "उन राज्यों का चयन करें जिनकी खबरें आप देखना चाहते हैं:",
    options=list(rss_feeds.keys()),
    default=["Assam", "Manipur", "Meghalaya"]  # Default selection
)

# Display news for selected states
for state in selected_states:
    st.markdown(f"<h2 style='color: #ff4b4b;'>📌 {state}</h2>", unsafe_allow_html=True)
    
    feed = fetch_news(rss_feeds[state])
    
    if not feed.entries:
        st.write("⚠️ इस समय कोई समाचार उपलब्ध नहीं है।")
    else:
        col1, col2 = st.columns(2)  # Two-column layout
        for i, entry in enumerate(feed.entries[:6]):  # Display top 6 news
            title_hindi = translate_to_hindi(entry.title)
            with col1 if i % 2 == 0 else col2:
                st.markdown(f"""
                    <div style="padding: 10px; border-radius: 10px; background-color: white; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
                        <h4>{title_hindi}</h4>
                        <a style="color: #ff4b4b; font-weight: bold;" href="{entry.link}" target="_blank">🔗 अधिक पढ़ें</a>
                    </div>
                """, unsafe_allow_html=True)
        
    st.markdown("---")  # Divider for better readability
