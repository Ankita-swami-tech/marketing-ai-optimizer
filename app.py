import streamlit as st
import pandas as pd
from content_engine.metrics_engine import generate_metrics
from content_engine.evaluation_engine import evaluate_performance

st.set_page_config(page_title="Marketing AI Testing Coach")

st.title("📊 Marketing AI – Testing Coach Dashboard")

metrics = generate_metrics("outputs/youtube_sentiment.csv")
evaluation = evaluate_performance(metrics)

st.subheader("Performance Metrics")
st.json(metrics)

st.subheader("Prediction")
st.success(evaluation["prediction"])

st.subheader("Recommendation")
st.info(evaluation["recommendation"])
