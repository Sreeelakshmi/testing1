import streamlit as st
import feedparser

# Define states in Northeast India
northeast_states = [
    "arunachal-pradesh", "assam", "manipur", "meghalaya", 
    "mizoram", "nagaland", "sikkim", "tripura"
]

# Generate RSS feed URLs for each state
rss_feeds = {
    f"https://indianexpress.com/section/north-east-india/{state}/feed/"
    for state in northeast_states
}

# Function to fetch and parse RSS feeds
def fetch_news(feed_url):
    return feedparser.parse(feed_url)

# Streamlit App Layout
st.set_page_config(page_title="📰 Northeast India News", layout="wide")
st.markdown(
    """
    <style>
        body {
            background-color: #f5f5f5;
        }
        .news-title {
            font-size: 28px;
            font-weight: bold;
            color: #ff4b4b;
        }
        .news-card {
            padding: 15px;
            border-radius: 10px;
            background-color: white;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        .news-link {
            color: #ff4b4b;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>📰 Northeast India News</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Stay updated with the latest headlines from each state in Northeast India.</p>", unsafe_allow_html=True)

# Sidebar for selecting states
st.sidebar.title("🌍 Select States")
selected_states = st.sidebar.multiselect(
    "Choose which states' news you want to see:",
    options=list(rss_feeds.keys()),
    default=["Assam", "Manipur", "Meghalaya"]  # Default selection
)

# Fetch and display headlines categorized by state
for state in selected_states:
    st.markdown(f"<h2 class='news-title'>📌 {state}</h2>", unsafe_allow_html=True)
    
    feed = fetch_news(rss_feeds[state])
    
    if not feed.entries:
        st.write("⚠️ No news available at the moment.")
    else:
        col1, col2 = st.columns(2)  # Two-column layout for better UX
        for i, entry in enumerate(feed.entries[:6]):  # Display top 6 headlines
            with col1 if i % 2 == 0 else col2:
                st.markdown(f"""
                    <div class='news-card'>
                        <h4>{entry.title}</h4>
                        <a class='news-link' href="{entry.link}" target="_blank">🔗 Read More</a>
                    </div>
                """, unsafe_allow_html=True)
        
    st.markdown("---")  # Divider for better readability
