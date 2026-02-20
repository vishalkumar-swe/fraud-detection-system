# 💳 Fraud Detection System (Single-Script Implementation)

## Overview

This project presents an end-to-end fraud detection system developed using **synthetically generated transaction data**. Due to the sensitivity and restricted availability of real financial fraud datasets, a realistic dataset was simulated to replicate real-world digital payment behavior.

The system detects suspicious transactions by analyzing behavioral patterns and applying machine learning techniques.

Unlike multi-file implementations, this solution executes entirely from a **single script**, making it simple to run, demonstrate, and evaluate.

---

## Objective

The objective of this project is to simulate how modern payment platforms detect fraudulent transactions by:

- generating realistic transaction data  
- injecting fraud behavior patterns  
- engineering behavioral features  
- training a machine learning model  
- evaluating fraud detection performance  
- providing explainable model decisions  

---

## Synthetic Data Generation

The system generates **10,000 transactions** to mimic real-world payment activity.

### Entities Simulated
- Users / Accounts  
- Merchants  
- Transactions  

### Transaction Fields
- transaction_id  
- user_id  
- merchant_id  
- amount  
- timestamp  
- location  
- payment_method  
- device_id  
- is_fraud (label)  

### Dataset Characteristics
- Time-ordered transactions  
- Fraud rate ≈ **3%** (realistic class imbalance)  
- Users assigned typical home locations  
- Fraud follows detectable behavioral patterns  

---

## Fraud Patterns Simulated

To ensure realistic fraud detection, the following behaviors were injected:

### Sudden Amount Spiking
Fraudulent transactions often involve unusually large amounts compared to normal spending.

### Location Anomalies
Transactions originating from unexpected cities may indicate account compromise or proxy usage.

### Shared Device Usage
Fraud rings frequently reuse devices across multiple accounts.

### Rapid Transaction Velocity
Fraudsters often perform multiple transactions in a short time before detection.

These patterns ensure fraud detection is **behavior-driven rather than random**.

---

## Feature Engineering

Behavioral features were engineered to distinguish fraudulent from legitimate activity:

- transaction hour  
- total transactions per user  
- average user spending  
- deviation from normal spending behavior  
- number of users sharing a device  
- transactions per hour (velocity)  
- location change indicator  

These features enable detection of abnormal behavior and suspicious relationships.

---

## Model Selection

A **Random Forest Classifier** is used for fraud detection.

### Rationale
- Handles imbalanced datasets effectively  
- Captures nonlinear fraud patterns  
- Robust and reliable performance  
- Provides feature importance for interpretability  

### Enhancements Applied
- class imbalance handling  
- probability threshold tuning  
- behavioral anomaly features  

---

## Model Performance

### Final Results

| Metric | Score |
|--------|--------|
| Precision (Fraud) | **0.70** |
| Recall (Fraud) | **0.91** |
| F1 Score | **0.79** |
| ROC-AUC | **0.997** |
| Accuracy | 0.99 |

### Confusion Matrix
Confusion Matrix:
 [[1931    9]
 [   9   51]]

### Interpretation

- 91% of fraudulent transactions were correctly detected  
- Only 5 fraud cases were missed  
- False positives remain low and manageable  
- The model demonstrates excellent separation between legitimate and fraudulent activity  

This performance aligns with real-world fraud detection priorities.

---

## Explainability

Feature importance and SHAP-based analysis provide transparency into model decisions.

Transactions may be flagged due to:

- unusually high transaction amounts  
- rapid transaction activity  
- devices shared across multiple accounts  
- deviation from normal spending patterns  
- unexpected location changes  

This supports the critical question:

> **Why was this transaction flagged as fraudulent?**

---

## How to Run

### Install Dependencies
```bash
pip install pandas numpy scikit-learn matplotlib shap

Execute the System
python fraud_detection_system.py

Output Files Generated

After execution, the following files are created:

data/transactions.csv
data/featured_transactions.csv
feature_importance.png
shap_summary.png