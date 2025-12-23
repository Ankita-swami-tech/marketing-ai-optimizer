import pandas as pd

def generate_metrics(file_path):
    df = pd.read_csv(file_path)

    metrics = {
        "total_posts": len(df),
        "avg_sentiment": round(df["sentiment_score"].mean(), 3),
        "positive_posts": len(df[df["sentiment_score"] > 0.05]),
        "negative_posts": len(df[df["sentiment_score"] < -0.05]),
        "neutral_posts": len(df[
            (df["sentiment_score"] >= -0.05) &
            (df["sentiment_score"] <= 0.05)
        ])
    }
    return metrics
