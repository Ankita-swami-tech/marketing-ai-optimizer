import pandas as pd
import os

def main():
    input_file = "outputs/youtube_sentiment.csv"
    output_file = "outputs/performance_report.txt"

    if not os.path.exists(input_file):
        print("❌ youtube_sentiment.csv not found. Run sentiment analysis first.")
        return

    df = pd.read_csv(input_file)

    total_posts = len(df)
    avg_sentiment = round(df["sentiment_score"].mean(), 3)
    positive = len(df[df["sentiment_score"] > 0.05])
    negative = len(df[df["sentiment_score"] < -0.05])
    neutral = total_posts - positive - negative

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("PERFORMANCE METRICS REPORT\n")
        f.write("===========================\n")
        f.write(f"Total Posts: {total_posts}\n")
        f.write(f"Average Sentiment Score: {avg_sentiment}\n")
        f.write(f"Positive Posts: {positive}\n")
        f.write(f"Negative Posts: {negative}\n")
        f.write(f"Neutral Posts: {neutral}\n")

    print("✅ Performance metrics report generated successfully")
    print(f"📁 Report saved at: {output_file}")

if __name__ == "__main__":
    main()
