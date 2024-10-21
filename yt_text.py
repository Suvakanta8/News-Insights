import random
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from requests.exceptions import HTTPError

# List of proxies
proxies_list = [
    "socks4://142.54.231.38:4145",
    "socks4://51.161.131.84:50827",
    "socks4://192.252.208.70:14282",
    "socks4://142.54.237.34:4145",
    "socks4://191.102.251.29:4153",
    "socks4://88.151.190.251:37540",
    "socks4://200.125.40.38:5678",
    "socks4://215.108.106.191:3128",
    "socks4://117.74.65.207:80",
    "socks4://103.37.82.134:39873",
    "http://87.98.148.98:80"
]

# Function to choose a random proxy
def get_random_proxy():
    proxy = random.choice(proxies_list)
    return {
        "http": proxy,
        "https": proxy,
    }

# Modified generate_transcript function to use a proxy
def generate_transcript(id: str) -> str:
    proxy = get_random_proxy()  # Get a random proxy

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
