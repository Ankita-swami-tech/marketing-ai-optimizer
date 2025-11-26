import feedparser
import pandas as pd

def scrape_google_news(keyword="marketing"):
    print(f"🔍 Scraping Google News for: {keyword}")

    url = f"https://news.google.com/rss/search?q={keyword}&hl=en-IN&gl=IN&ceid=IN:en"

    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries:
        articles.append([
            entry.title,
            entry.link,
            entry.published
        ])

    df = pd.DataFrame(articles, columns=["Title", "URL", "Published"])
    df.to_csv("data/google_news_latest.csv", index=False)

    print("🔥 Google News Saved → data/google_news_latest.csv")

# Run
scrape_google_news("marketing")
