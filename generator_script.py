import base64
import io
import requests
from pydub import AudioSegment
from pathlib import Path

name = "Chardonnay"
IPA = "ʃaʁ.dɔ.nɛ"
output_file = f"files/{name}.mp3"

def download_data(IPA, voice="Marlene"):
    """
    :param IPA: the text to be downloaded in IPA notation
    :param voice: voice to be used
    German voices are Marlene, Vicki, Hannah, Hans.
    English voices are found at https://docs.aws.amazon.com/polly/latest/dg/voicelist.html
    :return audio_data: audio data encoded in base64
    """
    url = "https://iawll6of90.execute-api.us-east-1.amazonaws.com/production"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        "Referer": "http://ipa-reader.xyz/",
        "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Origin": "http://ipa-reader.xyz",
        "Connection": "keep-alive",
        "Sec-Fetch-Site": "cross-site",
        "TE": "trailers",
    }
    data = {
        "text": IPA,
        "voice": voice,
    }

    response = requests.post(url, json=data, headers=headers)
    audio_data = response.json().strip().strip('"')
    audio_data = audio_data.replace("\n","")
    #print(f"Audio data: {audio_data}")
    return audio_data

def decode_and_save(base64_string, output_file_path):
    try:
        # Decode the base64 string into raw audio data
        audio_data = base64.b64decode(base64_string)
        
        # Convert the raw audio data into an AudioSegment object
        audio_segment = AudioSegment.from_file(io.BytesIO(audio_data))
        
        # Save the AudioSegment object as an MP3 file
        audio_segment.export(output_file_path, format="mp3")
        
        print("MP3 file generated successfully.")
    except Exception as e:
        print("Error:", e)



if __name__ == "__main__":
    base64_data = download_data(IPA, "Marlene")
    decode_and_save(base64_data, output_file)
