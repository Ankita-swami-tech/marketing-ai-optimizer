from content_engine.metrics_engine import generate_metrics
from content_engine.evaluation_engine import evaluate_performance
from scripts.slack_notifier import send_slack_message

def main():
    metrics = generate_metrics("outputs/youtube_sentiment.csv")
    evaluation = evaluate_performance(metrics)

    send_slack_message(
        f"""
📊 Testing Coach Report
Prediction: {evaluation['prediction']}
Recommendation: {evaluation['recommendation']}
"""
    )

if __name__ == "__main__":
    main()
