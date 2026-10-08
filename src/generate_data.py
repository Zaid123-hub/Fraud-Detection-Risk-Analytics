"""Generate reproducible synthetic transaction data for learning only."""
from pathlib import Path
import random
from datetime import datetime, timedelta
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "transactions_demo.csv"

def main(n_rows: int = 2500, seed: int = 42) -> None:
    rng = random.Random(seed)
    start = datetime(2026, 1, 1)
    types = ["POS", "Online", "ATM", "Transfer"]
    type_weights = [40, 35, 10, 15]
    categories = ["Retail", "Grocery", "Travel", "Electronics", "Food", "Digital Services"]
    rows = []
    for i in range(1, n_rows + 1):
        ts = start + timedelta(minutes=rng.randint(0, 120 * 24 * 60))
        ttype = rng.choices(types, weights=type_weights)[0]
        category = rng.choice(categories)
        amount = round(rng.lognormvariate(3.5, 1.0), 2)
        risk = 0.015
        if amount > 700:
            risk += 0.20
        if ts.hour <= 4:
            risk += 0.13
        if ttype in {"Online", "Transfer"}:
            risk += 0.035
        if category in {"Electronics", "Digital Services"}:
            risk += 0.025
        fraud = int(rng.random() < min(risk, 0.65))
        rows.append({
            "transaction_id": f"TX{i:06d}",
            "timestamp": ts.strftime("%Y-%m-%d %H:%M:%S"),
            "amount": amount,
            "transaction_type": ttype,
            "merchant_category": category,
            "hour": ts.hour,
            "day_of_week": ts.weekday(),
            "is_weekend": int(ts.weekday() >= 5),
            "is_fraud": fraud,
        })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUT, index=False)
    print(f"Wrote {len(rows):,} synthetic rows to {OUT}")
    print("Reminder: this is synthetic teaching data, not real banking data.")

if __name__ == "__main__":
    main()
