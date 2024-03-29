from youtube_transcript_api import YouTubeTranscriptApi

def extract_text(data):
    combined_text = ""
    for item in data:
        combined_text += item['text'] + " "
    return combined_text.strip()

def generate_transcript(id: str) -> str:
 
    try:
        transcript = YouTubeTranscriptApi.get_transcript(id, languages=['en'])
        script = ""
 
        for text in transcript:
            t = text["text"]
            if t != '[Music]':
                    script += t + " "
        return script
        
    except:
        print("No Transcript found for English.")
        # retrieve the available transcripts
        transcript_list = YouTubeTranscriptApi.list_transcripts(id)
 
        # iterate over all available transcripts
        for transcript in transcript_list:
            # Print Transcript language with language code
            print(f"Translating {transcript.language} to english")
 
            # Translating the language to English
            transcript = YouTubeTranscriptApi.list_transcripts(id).find_transcript([transcript.language_code])
            script = extract_text(transcript.translate('en').fetch())
            return script