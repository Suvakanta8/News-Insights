import os
import google.generativeai as genai
import streamlit as st
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'google_cred_gemini.json'
gemini_api_key = st.secrets['GEMINI_API_KEY']

genai.configure(api_key=gemini_api_key)

def get_content(user_input):
    prompt = f'''You are an expert financial content writer with a deep understanding of investment and trading. Your task is to write an audience attractive SEO friendly blog by using provided informations from other different websites.
            which is {user_input}
                            # Instruction:
                            Write a 1500-word SEO-optimized article about the information given to you which is same type article from different websites. 
                            Use that information as context , but write a unique informative blog
            #                 Begin with a catchy, SEO-optimized level 1 heading ('#') that captivates the reader. 
            #                 Follow with SEO optimized introductory paragraphs. 
            #                 Then organize the rest of the article into detailed level 2 ('##') heading tags and lower-level heading tags. like ('###','####')
            #                 Include detailed paragraphs under each heading and subheading that provide in-depth information about the topic. 
            #                 Use bullet points, unordered lists, bold text, code blocks (if required) etc to enhance readability and engagement. 
            #                 Use seo friendly keywords in the blog
            #                 Finish the blog with conclusion'''

    generation_config = {
    "temperature": 0.2,
    "top_p": 1,
    "max_output_tokens": 8096,
    }

    model = genai.GenerativeModel('gemini-1.0-pro',generation_config = generation_config)
    answer = model.generate_content(prompt)
    # print(answer.text)
    return(answer.text)
    

if __name__ == "__main__":
    print(get_content("stock market new trend in 2024"))
