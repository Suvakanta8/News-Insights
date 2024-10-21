import random
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from requests.exceptions import HTTPError

# Hardcoded file path for the proxies file (in the same directory as the script)
PROXY_FILE_PATH = 'proxies.txt'

# Function to read proxies from a text file
def load_proxies_from_file():
    with open(PROXY_FILE_PATH, 'r') as file:
        proxies = [line.strip() for line in file if line.strip()]
    return proxies

# Function to choose a random proxy
def get_random_proxy(proxies_list):
    proxy = random.choice(proxies_list)
    return {
        "http": proxy,
        "https": proxy,
    }

# Modified generate_transcript function to use a proxy
def generate_transcript(id: str) -> str:
    # Load proxies from the file
    proxies_list = load_proxies_from_file()

    proxy = get_random_proxy(proxies_list)  # Get a random proxy

    try:
        # Set up session with a proxy
        with requests.Session() as session:
            session.proxies.update(proxy)
            # Manually set the proxy for YouTubeTranscriptApi requests
            YouTubeTranscriptApi.requests = session  # Set requests to use the session
            
            transcript = YouTubeTranscriptApi.get_transcript(id, languages=['en'])
            
            script = ""
            for text in transcript:
                t = text["text"]
                if t != '[Music]':
                    script += t + " "
            return script
        
    except HTTPError as e:
        print(f"HTTP Error: {e}")
        return None
    except Exception as e:
        print(f"No Transcript found for English or another error occurred: {str(e)}")
        
        # If English transcript not available, try other languages and translate
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(id)
            for transcript in transcript_list:
                # Print Transcript language with language code
                print(f"Translating {transcript.language} to English")

                # Translating the language to English
                transcript = transcript.translate('en')
                translated_text = transcript.fetch()

                # Extract and combine the translated text
                script = extract_text(translated_text)
                return script
        except Exception as inner_e:
            print(f"Error occurred while trying to fetch or translate transcript: {inner_e}")
            return None

# Function to extract text from transcript data
def extract_text(data):
    combined_text = ""
    for item in data:
        combined_text += item['text'] + " "
    return combined_text.strip()

# Example usage
# video_id = 'YOUR_VIDEO_ID'
# print(generate_transcript(video_id))
