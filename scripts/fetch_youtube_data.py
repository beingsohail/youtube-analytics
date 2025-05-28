import requests
import json
import os


with open('config/config.json') as f:
        config = json.load(f)

RAPID_API_KEY = config["rapidapi_key"]

base_url = "https://youtube138.p.rapidapi.com"

def fetch_channel_videos(channel_id):

    url = f"{base_url}/channel/videos/"

    querystring = {
        "id":channel_id, 
        "filter":"videos_latest", 
        "hl":"en", 
        "gl":"US"
    }

    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "youtube138.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    # Save response to data/raw
    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/youtube_raw_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Data saved to data/raw/youtube_raw_data.json")

if __name__ == '__main__':
    channel_id = "UCJ5v_MCY6GNUBTO8-D3XoAg" 
    fetch_channel_videos(channel_id)
