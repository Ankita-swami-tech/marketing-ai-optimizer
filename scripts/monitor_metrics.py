from content_engine.metrics_engine import generate_metrics
from content_engine.evaluation_engine import evaluate_performance
from scripts.slack_notifier import send_slack_message

metrics = generate_metrics("outputs/youtube_sentiment.csv")
evaluation = evaluate_performance(metrics)

message = (
    f"📊 *Model Evaluation Report*\n"
    f"Accuracy: {evaluation['accuracy']}%\n"
    f"Recommendation: {evaluation['recommendation']}\n"
    f"Metrics: {metrics}"
)

send_slack_message(message)
