# Power BI dashboard guide

The included Streamlit dashboard is a working Python dashboard. A Power BI report is **not included as a .pbix file**, because Power BI Desktop creates that file interactively.

After running `python src/train_model.py`, open Power BI Desktop and use **Get Data → Text/CSV** to import:
- `outputs/transaction_predictions.csv`
- `outputs/model_metrics.csv`

Suggested visuals:
1. Cards: total transactions, flagged transactions, flagged rate.
2. Clustered column chart: transaction count by `transaction_type`.
3. Bar chart: flagged count by `merchant_category`.
4. Line chart: transaction count by date.
5. Table: transaction ID, amount, type, category, predicted risk score, predicted label.
6. Slicers: transaction type, merchant category, date.

For a demonstration dataset, title the report **Synthetic Transaction Risk Demo** and add a visible note that the data is synthetic. Do not present it as a bank's live fraud system.
