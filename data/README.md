# Dataset

This project uses the Bank Account Fraud (BAF) dataset introduced by
Jesus et al. (2022). The Base dataset is used for the experiments.

Due to the large file size, the CSV dataset is not stored directly in
this GitHub repository. The dataset can be obtained from the original
dataset source.

## Dataset File

- File used: `Base.csv`
- Number of records: approximately 1 million
- Target variable: `fraud_bool`
- Dataset version: Base

## Dataset Description

The Bank Account Fraud (BAF) dataset is a synthetic dataset based on
real-world bank account opening fraud patterns. It contains applicant,
transaction, device, and behavioural features for fraud detection.

**Dataset:** Bank Account Fraud (BAF) Dataset Suite (Jesus et al., 2022, NeurIPS)
**Source:** [Kaggle — sgpjesus/bank-account-fraud-dataset-neurips-2022](https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips-2022)
**Official repo:** [feedzai/bank-account-fraud](https://github.com/feedzai/bank-account-fraud)


# Feature Dictionary — Bank Account Fraud (BAF) Dataset

**Dataset:** Bank Account Fraud (BAF) Dataset Suite (Jesus et al., 2022, NeurIPS)
**Source:** [Kaggle — sgpjesus/bank-account-fraud-dataset-neurips-2022](https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips-2022)
**Official repo:** [feedzai/bank-account-fraud](https://github.com/feedzai/bank-account-fraud)

This document records the meaning of every column in the dataset, compiled during EDA to support
feature understanding ahead of model development.

> **Note on categorical codes:** Several categorical features (e.g. `housing_status`,
> `employment_status`, `device_os`, `payment_type`) use anonymised codes (e.g. `BA`, `BB`, `BC`)
> rather than human-readable labels. This is intentional — the dataset was built with
> privacy-preserving generation methods, so the original real-world category labels were not
> published. This is noted here as a dataset limitation.

> **Note on negative values:** Some numerical features (e.g. `prev_address_months_count`,
> `session_length_in_minutes`) may contain negative values in the raw dataset. Per the BAF
> dataset documentation, negative values represent missing or unknown data rather than true
> negative measurements. These are handled by clipping to 0 during preprocessing.

---

## 1. Target Variable

| Column | Description | Data Type | Sample Value |
|---|---|---|---|
| `fraud_bool` | Target variable — 0 = legitimate application, 1 = fraudulent application | Integer (Boolean: 0/1) | 0 |

---

## 2. Demographic / Applicant Information

| Column | Description | Data Type | Sample Value |
|---|---|---|---|
| `income` | Applicant's income expressed as a decile (0.1–0.9) rather than an absolute value | Float | 0.3 |
| `customer_age` | Applicant's age grouped into decade bins (e.g. 10, 20, 30, 40...) | Integer | 40 |
| `name_email_similarity` | Similarity score (0–1) between the applicant's name and their email address; low scores can indicate randomly generated or fake emails | Float | 0.986506 |

---

## 3. Address History

| Column | Description | Data Type | Sample Value |
|---|---|---|---|
| `prev_address_months_count` | Number of months the applicant lived at their previous address; -1 indicates unknown/missing | Integer | -1 |
| `current_address_months_count` | Number of months at their current address; short durations can indicate a new or synthetic identity | Integer | 25 |
| `zip_count_4w` | Number of applications from the same zip code in the previous 4 weeks | Integer | 1059 |

---

## 4. Velocity (Application Frequency)

| Column | Description | Data Type | Sample Value |
|---|---|---|---|
| `velocity_6h` | Rate of applications linked to the same device/IP in the previous 6 hours | Float | 13096.035018 |
| `velocity_24h` | Rate of applications linked to the same device/IP in the previous 24 hours | Float | 7850.955007 |
| `velocity_4w` | Rate of applications linked to the same device/IP in the previous 4 weeks | Float | 6742.080561 |

> **Note on large values:** Velocity values appear very large (e.g. 13,096) because the BAF
> dataset is synthetically generated — the original real-world values were anonymised/scaled
> during the generation process. The relative differences between values remain meaningful for
> fraud detection purposes. High velocity values indicate burst-application behaviour consistent
> with automated bot attacks or "bust-out" fraud schemes.

---

## 5. Device & Session Information

| Column | Description | Data Type | Sample Value |
|---|---|---|---|
| `device_os` | Operating system used for the application (anonymised categorical code) | String (categorical) | linux |
| `device_distinct_emails_8w` | Number of distinct email addresses used on the same device in the previous 8 weeks; higher counts can indicate fraud | Integer | 1 |
| `device_fraud_count` | Count of previous confirmed fraud cases linked to the same device | Integer | 0 |
| `session_length_in_minutes` | Time spent completing the application form in minutes | Float | 16.224843 |
| `keep_alive_session` | Whether the session was kept active (1 = yes, 0 = no) | Integer (Boolean: 0/1) | 1 |

---

## 6. Contact / Verification

| Column | Description | Data Type | Sample Value |
|---|---|---|---|
| `phone_home_valid` | Whether the home phone number is valid (1 = valid, 0 = invalid) | Integer (Boolean: 0/1) | 0 |
| `phone_mobile_valid` | Whether the mobile phone number is valid (1 = valid, 0 = invalid) | Integer (Boolean: 0/1) | 1 |
| `has_other_cards` | Whether the applicant already holds another card with the bank (1 = yes, 0 = no) | Integer (Boolean: 0/1) | 0 |
| `email_is_free` | Whether the email is from a free provider e.g. Gmail, Yahoo (1 = free, 0 = paid/corporate) | Integer (Boolean: 0/1) | 1 |
| `foreign_request` | Whether the request originated from a country different from the bank's country (1 = foreign, 0 = domestic) | Integer (Boolean: 0/1) | 0 |

---

## 7. Application / Behavioural

| Column | Description | Data Type | Sample Value |
|---|---|---|---|
| `payment_type` | Type of payment plan selected (anonymised categorical code) | String (categorical) | AA |
| `days_since_request` | Number of days since the application was submitted | Float | 0.006735 |
| `intended_balcon_amount` | Intended transfer amount linked to the application | Float | 102.453711 |
| `bank_branch_count_8w` | Number of applications at the same bank branch in the previous 8 weeks | Integer | 5 |
| `date_of_birth_distinct_emails_4w` | Number of distinct emails associated with the same date of birth in the previous 4 weeks | Integer | 5 |
| `proposed_credit_limit` | Credit limit requested by the applicant | Float | 1500.0 |
| `credit_risk_score` | Bank's internal credit risk score for the applicant | Integer | 163 |
| `bank_months_count` | Number of months the applicant has held an account at their previous bank | Integer | 9 |

---

## 8. Employment & Housing

| Column | Description | Data Type | Sample Value |
|---|---|---|---|
| `employment_status` | Applicant's employment situation (anonymised categorical code) | String (categorical) | CB |
| `housing_status` | Applicant's housing situation (anonymised categorical code e.g. owned/rented) | String (categorical) | BC |

---

## 9. Other / Metadata

| Column | Description | Data Type | Sample Value |
|---|---|---|---|
| `source` | Channel through which the application was submitted | String (categorical: INTERNET / TELEAPP) | INTERNET |
| `month` | Simulated month of the dataset (0–7), used to model temporal drift across 8 months | Integer | 0 |

---

## Limitations

- Exact unit of measurement for velocity features is not specified in public documentation-
  values appear scaled/anonymised as part of the synthetic data generation process.
- Real-world meaning behind anonymised categorical codes (e.g. `employment_status` = CB,
  `housing_status` = BC) cannot be recovered from public documentation; treated as a
  dataset limitation in this study.
- `prev_address_months_count` = -1 indicates missing data, not a true negative value.

---

