"""Train a baseline fraud classifier and write transparent evaluation artifacts."""
from pathlib import Path
import json
import warnings
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report, confusion_matrix, precision_score, recall_score,
    f1_score, average_precision_score, ConfusionMatrixDisplay
)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "transactions_demo.csv"
OUT = ROOT / "outputs"
MODEL_PATH = OUT / "fraud_model.joblib"

def main():
    OUT.mkdir(exist_ok=True)
    if not DATA.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA}. Run python src/generate_data.py first.")

    df = pd.read_csv(DATA, parse_dates=["timestamp"])
    required = {"transaction_id", "timestamp", "amount", "transaction_type",
                "merchant_category", "hour", "day_of_week", "is_weekend", "is_fraud"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Dataset is missing columns: {sorted(missing)}")
    df = df.drop_duplicates(subset=["transaction_id"]).dropna(subset=["is_fraud"])
    df["is_fraud"] = df["is_fraud"].astype(int)

    # Keep IDs and timestamp out of the model; derive only simple available features.
    features = ["amount", "transaction_type", "merchant_category", "hour",
                "day_of_week", "is_weekend"]
    X = df[features]
    y = df["is_fraud"]
    if y.nunique() < 2:
        raise ValueError("Need both fraud and non-fraud labels to train the classifier.")

    numeric = ["amount", "hour", "day_of_week", "is_weekend"]
    categorical = ["transaction_type", "merchant_category"]
    numeric_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])
    preprocessor = ColumnTransformer([
        ("numeric", numeric_pipe, numeric),
        ("categorical", categorical_pipe, categorical),
    ])
    model = Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(class_weight="balanced", max_iter=1000, random_state=42)),
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model.fit(X_train, y_train)
    probabilities = model.predict_proba(X_test)[:, 1]
    # Threshold is explicitly a demo choice, not a production decision.
    predictions = (probabilities >= 0.5).astype(int)

    metrics = {
        "dataset_note": "Synthetic demonstration data; results are illustrative only.",
        "rows_total": int(len(df)),
        "fraud_labels_total": int(y.sum()),
        "fraud_rate_percent": round(float(y.mean() * 100), 3),
        "test_rows": int(len(y_test)),
        "precision": round(float(precision_score(y_test, predictions, zero_division=0)), 4),
        "recall": round(float(recall_score(y_test, predictions, zero_division=0)), 4),
        "f1_score": round(float(f1_score(y_test, predictions, zero_division=0)), 4),
        "average_precision": round(float(average_precision_score(y_test, probabilities)), 4),
        "decision_threshold": 0.5,
    }
    with open(OUT / "model_metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
    pd.DataFrame([metrics]).to_csv(OUT / "model_metrics.csv", index=False)
    with open(OUT / "classification_report.txt", "w", encoding="utf-8") as f:
        f.write("SYNTHETIC DATA DEMO — NOT PRODUCTION PERFORMANCE\n\n")
        f.write(classification_report(y_test, predictions, zero_division=0))

    test_df = df.loc[X_test.index, ["transaction_id", "timestamp", "amount",
        "transaction_type", "merchant_category", "is_fraud"]].copy()
    test_df["predicted_risk_score"] = probabilities.round(4)
    test_df["predicted_fraud"] = predictions
    test_df.to_csv(OUT / "transaction_predictions.csv", index=False)

    cm = confusion_matrix(y_test, predictions, labels=[0, 1])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Not fraud", "Fraud"])
    disp.plot(values_format="d")
    plt.title("Confusion Matrix — Synthetic Demo Data")
    plt.tight_layout()
    plt.savefig(OUT / "confusion_matrix.png", dpi=160)
    plt.close()

    fraud_by_type = df.groupby("transaction_type", as_index=False)["is_fraud"].mean()
    fraud_by_type["fraud_rate_percent"] = fraud_by_type["is_fraud"] * 100
    fraud_by_type.drop(columns="is_fraud").to_csv(OUT / "fraud_rate_by_type.csv", index=False)

    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    print("Training complete.")
    print(json.dumps(metrics, indent=2))
    print(f"Artifacts saved to: {OUT}")
    print("Reminder: these results use synthetic data and are not evidence of real-world performance.")

if __name__ == "__main__":
    main()
