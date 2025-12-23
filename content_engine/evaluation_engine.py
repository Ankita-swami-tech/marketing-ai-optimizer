def evaluate_performance(metrics):
    sentiment = metrics.get("avg_sentiment", 0)
    engagement = metrics.get("avg_engagement", 0)

    if sentiment < -0.2:
        prediction = "Poor Performance"
        recommendation = (
            "Improve content tone, avoid negativity, "
            "and focus on audience problems."
        )

    elif sentiment < 0.3:
        prediction = "Average Performance"
        recommendation = (
            "Optimize posting time, add stronger CTA, "
            "and improve visuals."
        )

    else:
        prediction = "Good Performance"
        recommendation = (
            "Content is performing well. Maintain strategy "
            "and scale promotion."
        )

    return {
        "prediction": prediction,
        "recommendation": recommendation
    }
