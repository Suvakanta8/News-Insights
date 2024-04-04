from yt_text import generate_transcript
from blog_text import blogtext
import os
from urllib.parse import urlparse
import google.generativeai as genai
import streamlit as st

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'google_cred_gemini.json'
gemini_api_key = st.secrets['GEMINI_API_KEY']

genai.configure(api_key=gemini_api_key)

def get_yt_text(video_url):
    url_data = urlparse(video_url)
    id = url_data.query[2::]
    text = generate_transcript(id)
    return text

def get_blog_text(blog_url):
    text = blogtext(blog_url)
    return text

def get_summary(user_input):
    prompt = f'''You are an expert financial content writer with a deep understanding of investment and trading. Your task is to summarize the provided content, which may be in either English or Hindi, and offer valuable insights and suggestions to traders and investors
            Provided content is {user_input}
            # Instruction:
                            - Summarize the given content in simple terms.considering that it may be in English or Hindi.
                            - Create bullet points highlighting important topics.
                            - Provide valuable suggestions on market movement and necessary steps for traders and investors.

                            # Summary:
                            - 300 words overall paragraph summary
                            - Bullet point 1: [Important topic 1 in one senetnce]
                            - Bullet point 2: [Important topic 2 in one senetnce]
                            - Bullet point 3: [Important topic 3 in one senetnce]
                            - Bullet point 4: [Important topic 4 in one senetnce]
                            - Bullet point 5: [Important topic 5 in one senetnce]
                            - upto 10 points 

                            # Valuable Suggestions:
                            - Market Movement Prediction: [Brief prediction on how the market might react to this news]
                            - Necessary Steps for Traders: [Advice on actions traders should consider taking in response to this news]
                            - Necessary Steps for Investors: [Advice on actions investors should consider taking in response to this news]
                            - upto 5 valuable suggestions from above 3 points'''

    generation_config = {
    "temperature": 0.1,
    "top_p": 1,
    "max_output_tokens": 8596,
    }

    model = genai.GenerativeModel('gemini-1.0-pro',generation_config = generation_config)
    answer = model.generate_content(prompt)
    # print(answer.text)
    return(answer.text)
    
if __name__ == "__main__":
    # text = get_text("https://www.youtube.com/watch?v=8i0Lxcmq7rU")
    text = get_yt_text("https://www.youtube.com/watch?v=EQf8sk8krj4")
    # text = blogtext("https://www.businesstoday.in/markets/ipo-corner/story/ipo-alert-ecos-india-mobility-hospitality-files-drhp-with-sebi-to-launch-ipo-423409-2024-03-29")
    # print(text)
    print(get_summary(text))
