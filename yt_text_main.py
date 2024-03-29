from yt_text import generate_transcript
from blog_text import blogtext
import os
import logging
from openai import OpenAI
from urllib.parse import urlparse
logging.basicConfig(level=logging.INFO)

openai_api_key = os.environ['OPENAI_API_KEY']

def get_yt_text(video_url):
    url_data = urlparse(video_url)
    id = url_data.query[2::]
    text = generate_transcript(id)
    return text

def get_blog_text(blog_url):
    text = blogtext(blog_url)
    return text

def get_summary(text):
    try:
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {
                "role": "system",
                "content": '''You are an expert financial content writer with a deep understanding of investment and trading. Your task is to summarize the provided content, which may be in either English or Hindi, and offer valuable insights and suggestions to traders and investors
                           # Instruction:
                            - Summarize the given content in simple terms.considering that it may be in English or Hindi.
                            - Create bullet points highlighting important topics.
                            - Provide valuable suggestions on market movement and necessary steps for traders and investors.

                            # Summary:
                            - 300 words overall summary
                            - Bullet point 1: [Important topic 1]
                            - Bullet point 2: [Important topic 2]
                            - Bullet point 3: [Important topic 3]
                            - Bullet point 4: [Important topic 4]
                            - upto 10 points 

                            # Valuable Suggestions:
                            - Market Movement Prediction: [Brief prediction on how the market might react to this news]
                            - Necessary Steps for Traders: [Advice on actions traders should consider taking in response to this news]
                            - Necessary Steps for Investors: [Advice on actions investors should consider taking in response to this news]
                            - upto 5 valuable suggestions from above 3 points
    '''
                },
                {
                "role": "user",
                "content": f"{text}"
                }
            ],
            temperature=0,
            max_tokens=3000,
            top_p=1
        )
        if hasattr(response, 'choices') and response.choices:
            first_choice_text = response.choices[0].message.content
        else:
            first_choice_text = ""
        return first_choice_text
    
    except Exception as e:
        logging.error(f"OpenAI API request failed: {e}")
        return "ERROR"
    
if __name__ == "__main__":
    # text = get_text("https://www.youtube.com/watch?v=8i0Lxcmq7rU")
    text = get_yt_text("https://www.youtube.com/watch?v=EQf8sk8krj4")
    # text = blogtext("https://www.businesstoday.in/markets/ipo-corner/story/ipo-alert-ecos-india-mobility-hospitality-files-drhp-with-sebi-to-launch-ipo-423409-2024-03-29")
    # print(text)
    print(get_summary(text))
