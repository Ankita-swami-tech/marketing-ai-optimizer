from googleapiclient.discovery import build
from dotenv import load_dotenv
import pandas as pd
import os

# Load environment variables
load_dotenv()

# Read API key from .env file
API_KEY = os.getenv("YOUTUBE_API_KEY")

if not API_KEY:
    raise ValueError("❌ ERROR: YOUTUBE_API_KEY not found in .env file!")

# Initialize YouTube API client
youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY,
    cache_discovery=False
)

query = "digital marketing"

MAX_RESULTS = 100     # requested results
PER_REQUEST = 50      # YouTube API limit per call

all_items = []
next_page_token = None

while len(all_items) < MAX_RESULTS:
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        order="date",
        maxResults=PER_REQUEST,
        pageToken=next_page_token
    )

    response = request.execute()
    items = response.get("items", [])
    all_items.extend(items)

    next_page_token = response.get("nextPageToken")

    if not next_page_token:
        break  # no more pages

# Trim list to exactly 100 videos
all_items = all_items[:MAX_RESULTS]

# Build DataFrame
data = []
for item in all_items:
    snippet = item["snippet"]
    data.append({
        "title": snippet["title"],
        "channel": snippet["channelTitle"],
        "published_at": snippet["publishedAt"],
        "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
    })

df = pd.DataFrame(data)

# Save CSV to /data folder
os.makedirs("data", exist_ok=True)
df.to_csv("data/youtube_latest.csv", index=False, encoding="utf-8")

print("🔥 Saved 100 YouTube videos → data/youtube_latest.csv")
