import streamlit as st
from yt_text_main import get_yt_text , get_blog_text , get_summary

def main():
    st.title("Bull Trend 📈")

    url = st.text_input("Enter YouTube or Blog URL:")
    if url:
        if "youtube.com" in url:
            text = get_yt_text(url)
        else:
            text = get_blog_text(url)
        
        summary = get_summary(text)
        
        st.header("investment News Insights📰")
        st.write(summary)

if __name__ == "__main__":
    main()
