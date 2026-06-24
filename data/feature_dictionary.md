# Feature Dictionary — Bank Account Fraud (BAF) Dataset

**Dataset:** Bank Account Fraud (BAF) Dataset Suite (Jesus et al., 2022, NeurIPS)
**Source:** [Kaggle — sgpjesus/bank-account-fraud-dataset-neurips-2022](https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips-2022)
**Official repo:** [feedzai/bank-account-fraud](https://github.com/feedzai/bank-account-fraud)

This document records the meaning of every column in the dataset, compiled during EDA to support
feature understanding ahead of model development (per supervision meeting feedback, June 2026).

> **Note on categorical codes:** Several categorical features (e.g. `housing_status`,
> `device_os`, `payment_type`) use anonymised codes (e.g. `BA`, `BB`, `BC`) rather than
> human-readable labels. This is intentional — the dataset was built with privacy-preserving
> generation methods (CTGAN + differential privacy), so the original real-world category
> labels were not published. This is noted here as a dataset limitation.

---

## 1. Demographic / Applicant Information

| Column | Description |
|---|---|
| `income` | Applicant's income, expressed as a decile (0.1–0.9) rather than an absolute value |
| `customer_age` | Applicant's age, grouped into decade bins (e.g. 10, 20, 30...) |
| `name_email_similarity` | Similarity score (0–1) between the applicant's name and their email address; low scores can indicate randomly generated or fake emails |

## 2. Address History

| Column | Description |
|---|---|
| `prev_address_months_count` | Number of months the applicant lived at their previous address |
| `current_address_months_count` | Number of months at their current address; short durations can be a fraud risk indicator (new/synthetic identity) |
| `zip_count_4w` | Number of applications from the same zip code in the previous 4 weeks |

## 3. Velocity (Application Frequency)

| Column | Description |
|---|---|
| `velocity_6h` | Rate of applications linked to the same device/IP in the previous 6 hours |
| `velocity_24h` | Rate of applications linked to the same device/IP in the previous 24 hours |
| `velocity_4w` | Rate of applications linked to the same device/IP in the previous 4 weeks |

High velocity values can indicate automated/bot attacks or "bust-out" fraud schemes, where
many applications are opened in a short burst. This is a key fraud signal in the BAF paper
and related work (high feature importance for `velocity_24h` and `velocity_6h` reported in
downstream studies).

## 4. Device & Session Information

| Column | Description |
|---|---|
| `device_os` | Operating system used for the application (anonymised categorical code) |
| `device_distinct_emails_8w` | Number of distinct emails used on the same device in the previous 8 weeks; higher counts can indicate fraud |
| `device_fraud_count` | Count of previous confirmed fraud cases linked to the same device |
| `session_length_in_minutes` | Time spent completing the application form |
| `keep_alive_session` | Whether the session was kept active (boolean) |

## 5. Contact / Verification

| Column | Description |
|---|---|
| `phone_home_valid` | Whether the home phone number is valid |
| `phone_mobile_valid` | Whether the mobile phone number is valid |
| `has_other_cards` | Whether the applicant already holds another card with the bank |
| `email_is_free` | Whether the email is from a free provider (e.g. Gmail, Yahoo) |
| `foreign_request` | Whether the request originated from a country different from the bank's country |

## 6. Application / Behavioural

| Column | Description |
|---|---|
| `payment_type` | Type of payment plan selected (anonymised categorical code) |
| `bank_branch_count_8w` | Number of applications at the same bank branch in the previous 8 weeks |
| `date_of_birth_distinct_emails_4w` | Number of distinct emails associated with the same date of birth in the previous 4 weeks |
| `proposed_credit_limit` | Credit limit requested by the applicant |
| `credit_risk_score` | Bank's internal credit risk score for the applicant |
| `bank_months_count` | Number of months the applicant has held an account at their previous bank |

## 7. Housing

| Column | Description |
|---|---|
| `housing_status` | Applicant's housing situation (anonymised categorical code, e.g. owned/rented) |

## 8. Other / Metadata

| Column | Description |
|---|---|
| `source` | Channel through which the application was submitted (INTERNET / TELEAPP) |
| `month` | Simulated month of the dataset (0–7), used to model temporal drift |
| `fraud_bool` | **Target variable** — 0 = legitimate application, 1 = fraudulent application |

---

## Open Questions / Areas for Further Investigation

- Exact unit of measurement for velocity features (seconds, minutes, or normalised rate) is
  not specified in public documentation — flagged for literature review.
- Why `velocity_24h` shows a lower mean than both `velocity_6h` and `velocity_4w` in EDA —
  possible explanation: daily activity cycles diluting the 24h window. Needs further testing.
- Real-world meaning behind anonymised categorical codes (e.g. `housing_status` categories)
  cannot be recovered from public documentation; treated as a dataset limitation in this study.

---
