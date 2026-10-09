# Fraud Detection & Transaction Risk Analytics

A Python-based portfolio project demonstrating transaction data analysis, machine learning, and interactive dashboard development to explore transaction-risk patterns.

The project showcases how data analytics can help identify potentially risky transactions and support business decision-making.

> **Disclaimer:** This project uses synthetic demonstration data, not real bank or customer transactions. The fraud labels and analytical results are illustrative and do not demonstrate real-world fraud-detection performance.

---

## Dashboard Preview

### 1. Dashboard Overview

The dashboard provides summary metrics and visualizations to explore transaction amounts and transaction types.

### 2. Merchant Risk Analysis and Transaction Records

The dashboard also presents labelled fraud rates across merchant categories and allows users to explore individual synthetic transaction records.

## Project Objectives

- Explore transaction data using Python.
- Perform exploratory data analysis to understand transaction patterns.
- Develop a machine-learning classification pipeline.
- Evaluate model performance using appropriate classification metrics.
- Build an interactive dashboard for visualizing transaction data.
- Explore how transaction-risk analytics can support business decisions.

## Key Features

### 1. Data Analysis
- Data inspection and preprocessing using Pandas and NumPy.
- Analysis of transaction amounts and transaction categories.
- Exploration of merchant categories and transaction timing.
- Feature engineering using transaction-related attributes.

### 2. Machine Learning
- Scikit-learn classification pipeline.
- Model training and evaluation.
- Performance assessment using:
  - Precision
  - Recall
  - F1-score
  - Confusion matrix
  - Average precision

### 3. Interactive Dashboard
- Transaction type filters.
- Merchant category filters.
- Summary transaction metrics.
- Transaction amount distribution.
- Labelled fraud rate by merchant category.
- Transaction-level data exploration.

### 4. Business Analytics
- Exploration of transaction-risk patterns.
- Consideration of false positives and false negatives.
- Discussion of customer experience and investigation costs.
- Potential future integration with Excel or Power BI.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Scikit-learn | Machine learning and model evaluation |
| Streamlit | Interactive dashboard |
| CSV | Dataset storage and analytical outputs |
| Git and GitHub | Version control and project hosting |

---

## Project Structure

```text
Fraud_Detection_Risk_Analytics/
│
├── data/
│   └── transactions_demo.csv
│
├── src/
│   ├── generate_data.py
│   └── train_model.py
│
├── dashboard/
│   └── app.py
│
├── outputs/
│
├── screenshots/
│   ├── dashboard-overview.png
│   └── dashboard-analysis.png
│
├── powerbi_guide.md
├── requirements.txt
└── README.md
```

The `outputs/` directory contains generated evaluation results, predictions, and visualizations when produced by the training script.

---

## Installation and Setup

Follow these steps to run the project locally.

### Prerequisites

- Python 3.10 or later
- Git
- A code editor such as VS Code

### Step 1: Clone the Repository

Replace `YOUR-USERNAME` with your GitHub username and ensure the repository name matches your actual repository.

```bash
git clone https://github.com/YOUR-USERNAME/Fraud_Detection_Risk_Analytics.git
```

Navigate to the project directory:

```bash
cd Fraud_Detection_Risk_Analytics
```

### Step 2: Create a Virtual Environment

For macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

For Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Generate the Synthetic Dataset (Optional)

Run the following command from the project root:

```bash
python src/generate_data.py
```

This regenerates the synthetic demonstration dataset.

**Note:** Regenerating the dataset may change the data and the results obtained from subsequent analysis.

### Step 5: Train and Evaluate the Model

```bash
python src/train_model.py
```

The script generates evaluation summaries, predictions, and visualizations in the `outputs/` directory, depending on the implemented pipeline.

### Step 6: Launch the Dashboard

```bash
streamlit run dashboard/app.py
```

Open the local address displayed in your terminal to interact with the dashboard.

Run the dataset generation and model training steps first if the dashboard requires their generated files.

---

## Model Evaluation

The project uses classification evaluation metrics to assess the model.

### Precision

Precision measures the proportion of transactions predicted as positive that are actually positive according to the dataset labels.

Higher precision can mean fewer legitimate transactions are incorrectly flagged.

### Recall

Recall measures the proportion of positive-labelled transactions correctly identified by the model.

Higher recall can mean fewer positive-labelled transactions are missed.

### F1-Score

The F1-score combines precision and recall into a single metric using their harmonic mean.

It is useful when both false positives and false negatives matter.

### Confusion Matrix

A confusion matrix summarizes correct and incorrect predictions for each class.

It helps identify false positives and false negatives.

### Average Precision

Average precision summarizes model performance across different classification thresholds using the precision-recall relationship.

For imbalanced classification problems, these metrics can provide more insight than accuracy alone.

> Actual performance values should be reported only after running the model and verifying its outputs. Results from synthetic data are illustrative and should not be interpreted as evidence of performance on real banking transactions.

---

## Business Relevance

Transaction-risk analytics can help organizations explore unusual patterns and prioritize transactions for further investigation.

This project demonstrates analytical concepts relevant to business decision-making.

### Key Business Considerations

**1. False Positives**

Legitimate transactions may be incorrectly flagged, potentially creating customer inconvenience and additional investigation costs.

**2. False Negatives**

Transactions that should be flagged may go undetected, potentially increasing financial risk.

**3. Customer Experience**

Risk controls should balance the need for investigation with the need to avoid unnecessary disruption to legitimate customers.

**4. Data-Driven Decisions**

Analytical dashboards can help decision-makers explore patterns and identify areas that may warrant further investigation.

**5. Model Monitoring**

A model intended for real-world use would require appropriate validation, monitoring, and periodic evaluation.

These are general business considerations. This synthetic-data project does not establish actual fraud patterns or financial outcomes.

---

## Limitations

- The dataset contains synthetic demonstration data.
- The labels do not represent confirmed real-world fraud.
- Results depend on the assumptions used to generate the dataset.
- Performance on synthetic data does not establish performance on real banking transactions.
- The project is an educational prototype, not a production fraud-detection system.
- Real-world implementation would require suitable data, rigorous validation, security controls, monitoring, and domain expertise.

---

## Future Improvements

Potential improvements include:

- Evaluate a suitable public anonymized fraud dataset and document its source and licence.
- Compare a baseline model with Logistic Regression and a tree-based classifier.
- Use a time-based train-test split when appropriate for the dataset.
- Explore classification threshold tuning based on the relative costs of false positives and false negatives.
- Develop a Power BI dashboard using generated CSV outputs.
- Add automated tests and improved error handling.
- Explore model monitoring and explainability techniques.

These are planned improvements and should not be considered completed features unless implemented.

---

## Learning Outcomes

Through this project, the following skills can be demonstrated, provided the corresponding work has been completed and understood:

- Data cleaning and preprocessing
- Exploratory data analysis
- Feature engineering
- Machine-learning model evaluation
- Interactive data visualization
- Analytical problem-solving
- Interpretation of classification metrics
- Connecting analytical findings with business considerations

---

## Author

**[Sayyed Zaid]**

GitHub: (https://github.com/Zaid123-hub)

---

*This project is intended for educational and portfolio purposes. All findings should be interpreted in the context of the synthetic demonstration dataset.*
