import streamlit as st
from googlesearch import search
from blog_text import blogtext
from gen_content import get_content

def search_top_3(keyword):
    results = search(keyword, num=3, stop=3, pause=2)
    return list(results)

def check_domains(top_3_websites, domains =['twitter.com', 'instagram.com', 'youtube.com', 'linkedin.com']):
    for website in top_3_websites:
        for domain in domains:
            if domain in website:
                return None
    return top_3_websites

def content_main():
    st.title("Bull Trend 📈")
    # Radio buttons for selecting the section
    tweet = st.text_input("Enter trending tweet:")
    if tweet:
        all_content = []
        websites = search_top_3(tweet)
        print(websites)
        final_website = check_domains(websites)
        if final_website is None:
            st.write("Enter another keyword")
        else:
            print(final_website)
            for url in final_website:
                content = blogtext(url)
                all_content.append(content)
            final_content = get_content(all_content)
            st.write(final_content)

if __name__ == "__main__":
    content_main()
    