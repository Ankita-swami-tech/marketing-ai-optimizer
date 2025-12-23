import pandas as pd
from content_engine.sentiment_engine import get_sentiment

# Load YouTube trend data
df = pd.read_csv("data/youtube_latest.csv")

# Apply sentiment analysis
df["sentiment_score"] = df["title"].apply(
    lambda x: get_sentiment(str(x))
)

# Categorize sentiment
df["sentiment_label"] = df["sentiment_score"].apply(
    lambda x: "Positive" if x > 0.05 else "Negative" if x < -0.05 else "Neutral"
)

# Save output
df.to_csv("outputs/youtube_sentiment.csv", index=False)
print("✅ Sentiment analysis completed")
