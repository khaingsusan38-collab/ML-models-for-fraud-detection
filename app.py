"""
Fraud Detection — Demonstration UI

Run locally with:
    streamlit run app.py

Requires the following files in a `saved_models/` folder next to this script
(all produced by Final_Model_Comparison.ipynb):
    - xgb_model.pkl
    - feature_columns.pkl
    - sample_cases.csv
"""

import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------------------------------------------
# Page setup
# ---------------------------------------------------------------------------
st.set_page_config(page_title="Fraud Detection Demo", page_icon="🔍", layout="centered")
st.title("🔍 Bank Account Fraud Detection — Demo")
st.caption(
    "Comparative Analysis of Machine Learning Models for "
    "Fraud Detection in Financial Transactions"
)
st.write(
    "This demo loads the final trained **XGBoost** model and runs it against "
    "pre-selected example applications from the held-out test set."
)

# ---------------------------------------------------------------------------
# Load model and supporting files (cached so they only load once)
# ---------------------------------------------------------------------------
@st.cache_resource
def load_artifacts():
    model = joblib.load("saved_models/xgb_model.pkl")
    feature_columns = joblib.load("saved_models/feature_columns.pkl")
    return model, feature_columns


@st.cache_data
def load_sample_cases():
    return pd.read_csv("saved_models/sample_cases.csv")


try:
    xgb_model, feature_columns = load_artifacts()
    sample_df = load_sample_cases()
except FileNotFoundError as e:
    st.error(
        f"Could not find a required file: {e}\n\n"
        "Make sure `saved_models/` (with xgb_model.pkl, feature_columns.pkl, "
        "sample_cases.csv) is in the same folder as this script, and that you "
        "have run `Final_Model_Comparison.ipynb` to generate it."
    )
    st.stop()

# ---------------------------------------------------------------------------
# Case selector
# ---------------------------------------------------------------------------
st.subheader("1. Choose an example application")

case_id = st.selectbox("Test-set example:", sample_df["case_id"].tolist())
row = sample_df[sample_df["case_id"] == case_id].iloc[0]

# ---------------------------------------------------------------------------
# Show the selected case's key features
# ---------------------------------------------------------------------------
st.subheader("2. Application details")

# Show a curated subset of the most interpretable features rather than all 32
key_features = [
    "income", "name_email_similarity", "prev_address_months_count",
    "current_address_months_count", "customer_age", "days_since_request",
    "velocity_6h", "velocity_24h", "velocity_4w", "bank_branch_count_8w",
    "date_of_birth_distinct_emails_4w", "credit_risk_score",
    "email_is_free", "phone_home_valid", "phone_mobile_valid",
    "has_other_cards", "proposed_credit_limit", "foreign_request",
    "device_distinct_emails_8w", "device_fraud_count", "month",
]
available_key_features = [f for f in key_features if f in row.index]
st.dataframe(
    row[available_key_features].to_frame(name="Value"),
    use_container_width=True,
)

with st.expander("Show all feature values"):
    st.dataframe(row[feature_columns].to_frame(name="Value"), use_container_width=True)

# ---------------------------------------------------------------------------
# Predict
# ---------------------------------------------------------------------------
st.subheader("3. Run the model")

if st.button("🔮 Predict", type="primary"):
    X_input = row[feature_columns].to_frame().T.astype(float)

    prediction = xgb_model.predict(X_input)[0]
    probability = xgb_model.predict_proba(X_input)[0, 1]

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Fraud probability", f"{probability:.2%}")

    with col2:
        if prediction == 1:
            st.error("⚠️ Predicted: FRAUD")
        else:
            st.success("✅ Predicted: LEGITIMATE")

    true_label = int(row["true_label"])
    true_label_text = "FRAUD" if true_label == 1 else "LEGITIMATE"
    correct = (prediction == true_label)

    st.write(f"**Actual label (ground truth):** {true_label_text}")
    if correct:
        st.info("✅ The model's prediction matches the true label.")
    else:
        st.warning("❌ The model's prediction does NOT match the true label.")

st.divider()
st.caption(
    "Model: XGBoost (default hyperparameters — selected as the final model "
    "based on highest ROC-AUC and Average Precision across the three "
    "compared algorithms). See Final_Model_Comparison.ipynb for full results."
)
