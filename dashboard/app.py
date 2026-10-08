"""Simple Streamlit dashboard for the synthetic fraud analytics project."""
from pathlib import Path
import json
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "transactions_demo.csv"
PREDICTIONS = ROOT / "outputs" / "transaction_predictions.csv"
METRICS = ROOT / "outputs" / "model_metrics.json"

st.set_page_config(page_title="Transaction Risk Analytics", layout="wide")
st.title("Fraud Detection & Transaction Risk Analytics")
st.warning("Learning demo only: this app uses synthetic data, not real bank/customer transactions.")

if not DATA.exists():
    st.error("Dataset missing. From the project root, run: python src/generate_data.py")
    st.stop()

df = pd.read_csv(DATA, parse_dates=["timestamp"])
if "is_fraud" not in df.columns:
    st.error("The data file does not contain the expected is_fraud column.")
    st.stop()

st.sidebar.header("Filters")
types = st.sidebar.multiselect("Transaction type", sorted(df["transaction_type"].unique()),
                               default=sorted(df["transaction_type"].unique()))
cats = st.sidebar.multiselect("Merchant category", sorted(df["merchant_category"].unique()),
                              default=sorted(df["merchant_category"].unique()))
filtered = df[df["transaction_type"].isin(types) & df["merchant_category"].isin(cats)]

total = len(filtered)
frauds = int(filtered["is_fraud"].sum())
fraud_rate = (frauds / total * 100) if total else 0
c1, c2, c3 = st.columns(3)
c1.metric("Transactions", f"{total:,}")
c2.metric("Synthetic fraud labels", f"{frauds:,}")
c3.metric("Labelled fraud rate", f"{fraud_rate:.2f}%")

st.subheader("Transaction amount distribution")
st.bar_chart(filtered.groupby("transaction_type")["amount"].mean().sort_values(ascending=False))
st.subheader("Labelled fraud rate by merchant category")
rate = filtered.groupby("merchant_category")["is_fraud"].mean().mul(100).sort_values(ascending=False)
st.bar_chart(rate)
st.subheader("Transaction records")
st.dataframe(filtered.head(300), use_container_width=True)

if PREDICTIONS.exists():
    st.subheader("Model test predictions")
    pred = pd.read_csv(PREDICTIONS)
    st.caption("These are held-out test predictions from the baseline model, using synthetic labels.")
    st.dataframe(pred.head(100), use_container_width=True)
else:
    st.info("Run `python src/train_model.py` to create model evaluation outputs.")

if METRICS.exists():
    with open(METRICS, encoding="utf-8") as f:
        metrics = json.load(f)
    st.subheader("Baseline model evaluation")
    cols = st.columns(4)
    cols[0].metric("Precision", f"{metrics['precision']:.3f}")
    cols[1].metric("Recall", f"{metrics['recall']:.3f}")
    cols[2].metric("F1-score", f"{metrics['f1_score']:.3f}")
    cols[3].metric("Average precision", f"{metrics['average_precision']:.3f}")
    st.caption("Metrics are illustrative because the dataset is synthetic; do not interpret them as real-world fraud performance.")
