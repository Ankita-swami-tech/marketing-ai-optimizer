import requests
import pandas as pd
import os

# Subreddit you want to scrape
SUBREDDIT = "technology"   # change to any subreddit

# Number of posts
LIMIT = 100

def scrape_reddit(subreddit, limit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("❌ Error fetching data:", response.status_code)
        return []

    data = response.json()["data"]["children"]

    posts = []
    for item in data:
        post = item["data"]
        posts.append({
            "Title": post.get("title", ""),
            "URL": "https://www.reddit.com" + post.get("permalink", ""),
            "Author": post.get("author", ""),
            "Upvotes": post.get("ups", 0),
            "Comments": post.get("num_comments", 0),
            "Created_UTC": post.get("created_utc", "")
        })

    return posts


if __name__ == "__main__":
    print("📌 Fetching Reddit posts...")
    posts = scrape_reddit(SUBREDDIT, LIMIT)

    os.makedirs("data", exist_ok=True)

    df = pd.DataFrame(posts)
    df.to_csv("data/reddit_latest.csv", index=False, encoding="utf-8")

    print("✅ Saved 100 Reddit posts → data/reddit_latest.csv")
