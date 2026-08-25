# Comparative Analysis of Machine Learning Models for Bank Account Fraud Detection

## Project Overview

This project investigates the use of machine learning for detecting fraudulent bank account applications. The main aim is to compare the performance of three machine learning models under severe class imbalance:

- Logistic Regression
- Random Forest
- XGBoost

The project develops a machine learning-based fraud detection pipeline covering data exploration, preprocessing, class imbalance handling, model training, hyperparameter tuning, and model evaluation.

## Dataset

The project uses the **Bank Account Fraud (BAF) Dataset Suite**, specifically the **Base variant** introduced by Jesus et al. (2022).

The dataset contains approximately:

- 1,000,000 bank account application records
- 32 features
- 1.1% fraudulent applications
- 98.9% legitimate applications

The BAF dataset is synthetic but was designed to reproduce realistic characteristics of real-world bank account application fraud while preserving privacy.

Further information about the dataset and its features is available in the [`data`](data/) directory.

## Project Workflow

The main workflow of the project is:

1. Dataset understanding and exploratory data analysis (EDA)
2. Data cleaning and preprocessing
3. Categorical feature encoding
4. Stratified train-test splitting
5. Class imbalance handling
6. Model training
7. Hyperparameter tuning
8. Model evaluation and comparison
9. Selection of the final model

SMOTE is used where appropriate for Logistic Regression and Random Forest, while XGBoost uses class weighting through `scale_pos_weight`.

## Machine Learning Models

### Logistic Regression

Logistic Regression is used as an interpretable baseline model for comparison with the more complex ensemble approaches.

### Random Forest

Random Forest is included as a bagging-based ensemble model capable of capturing non-linear relationships and interactions between features.

### XGBoost

XGBoost is used as a gradient-boosting model suitable for large structured tabular datasets and provides an alternative approach for handling the imbalanced fraud classification problem.

## Model Evaluation

Because the dataset is highly imbalanced, model performance is not assessed using accuracy alone.

The main evaluation metrics include:

- Precision
- Recall
- F1-score
- ROC-AUC
- Average Precision (PR-AUC)
- Confusion Matrix

These metrics provide a more informative assessment of fraud detection performance, particularly for the minority fraud class.

## Repository Structure

```text
ML-models-for-fraud-detection/
│
├── README.md
│
├── data/
│   └── README.md
│
└── notebooks/
    ├── EDA_BankFraud.ipynb
    ├── Model_LogisticRegression.ipynb
    ├── Model_RandomForest.ipynb
    ├── Model_XGBoost.ipynb
    ├── Hyperparameter_Tuning.ipynb
    └── Final_Model_Comparison.ipynb
```

### `data/`

Contains information about the BAF dataset, including descriptions of the features used in the project.

### `notebooks/`

Contains the Jupyter notebooks used for exploratory data analysis, preprocessing, model development, hyperparameter tuning, and final model comparison.

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn
- XGBoost
- Matplotlib

## Final Model

The three machine learning approaches are compared using the same held-out test data. Based on the overall evaluation, **XGBoost was selected as the final model**, providing the strongest overall discrimination and ranking performance among the models investigated.

## Academic Context

This repository contains the implementation developed for an MSc Data Science project at the University of the West of England (UWE Bristol).

The repository is intended to provide a clear and reproducible record of the data analysis and machine learning workflow used in the project.

## Reference

Jesus, S., Pombal, J., Alves, D., Cruz, A.F., Saleiro, P., Ribeiro, R.P., Gama, J. and Bizarro, P. (2022) ‘Turning the tables: Biased, imbalanced, dynamic tabular datasets for ML evaluation’, *Advances in Neural Information Processing Systems*, 35.
