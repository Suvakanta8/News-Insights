import streamlit as st
from yt_text_main import get_yt_text , get_blog_text , get_summary
from urllib.parse import urlparse, parse_qs

def convert_mobile_to_browser_link(url):
    # Check if the URL is already in youtube.com format
    if "youtube.com" in url:
        return url

    # Parse the mobile link
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    # Extract the video ID
    video_id = parsed_url.path.lstrip('/')

    if video_id:
        # Construct the browser link
        browser_link = f"https://www.youtube.com/watch?v={video_id}"
        return browser_link
    else:
        return None
    
def main():
    st.title("Bull Trend 📈")

    url = st.text_input("Enter YouTube or Blog URL:")
    if url:
        if "youtube.com" in url or "youtu.be" in url:
            input_url = convert_mobile_to_browser_link(url)
            text = get_yt_text(input_url)
        else:
            text = get_blog_text(url)
        
        summary = get_summary(text)
        
        st.header("investment News Insights📰")
        st.write(summary)

if __name__ == "__main__":
    main()
