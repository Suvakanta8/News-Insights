import streamlit as st
import os
import logging
from openai import OpenAI
logging.basicConfig(level=logging.INFO)

from dotenv import load_dotenv

load_dotenv()
openai_api_key = st.secrets["OPENAI_API_KEY"]

def get_content(text):
    try:
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {
                "role": "system",
                "content": '''You are an expert financial content writer with a deep understanding of investment and trading. Your task is to write an audience attractive SEO friendly blog by using provided informations from other different websites.
                           # Instruction:
                           Write a 1500-word SEO-optimized article about the information given to you which is same type article from different websites. 
                          Use that information as context , but write a unique informative blog
        #                 Begin with a catchy, SEO-optimized level 1 heading ('#') that captivates the reader. 
        #                 Follow with SEO optimized introductory paragraphs. 
        #                 Then organize the rest of the article into detailed level 2 ('##') heading tags and lower-level heading tags. like ('###','####')
        #                 Include detailed paragraphs under each heading and subheading that provide in-depth information about the topic. 
        #                 Use bullet points, unordered lists, bold text, code blocks (if required) etc to enhance readability and engagement. 
        #                 Use seo friendly keywords in the blog
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
