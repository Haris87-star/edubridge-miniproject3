# Privacy Policy

**Effective Date:** October 28, 2026  
**Project:** EduBridge Mini-Project 3 (Loan Eligibility Prediction System)  
**Author & Maintainer:** Harish ([@Haris87-star](https://github.com/Haris87-star))  
**Contact:** harishhari781823@gmail.com  
**Repository:** [https://github.com/Haris87-star/edubridge-miniproject3](https://github.com/Haris87-star/edubridge-miniproject3)

---

## 1. Overview and Purpose

This Privacy Policy outlines how personal data, financial metrics, and user information are handled within **EduBridge Mini-Project 3: Loan Eligibility Prediction System**. We are committed to maintaining the confidentiality, privacy, and integrity of any financial information evaluated by the machine learning models.

---

## 2. Information Handled by the Project

The system operates on quantitative financial features used strictly for binary classification (Loan Approval/Rejection):
- **CIBIL Credit Score:** Numerical credit ratings ranging between 300 and 900.
- **Loan Amount Requested:** Principal borrowing figures requested by applicants (in lakhs or INR).
- **Eligibility Outcome:** Binary target classification ($1 = \text{Eligible}, 0 = \text{Not Eligible}$) and computed probabilities ($P \in [0, 1]$).

### Synthetic Data Principle
All default datasets packaged within this repository (e.g., in `Li.py` and `eligibilityy.py`) are synthetically generated or anonymized sample records for academic and demonstrative purposes. No actual personally identifiable information (PII) of real individuals is collected, stored, or distributed.

---

## 3. Data Processing and Storage Architecture

- **100% Local Execution:** All machine learning operations—including preprocessing, scaling, mathematical optimization via BFGS, and decision boundary visualization—execute exclusively on the user's local machine.
- **No Cloud Offloading:** No applicant details or model parameters are transmitted to third-party APIs, remote servers, or external cloud telemetry endpoints.
- **Zero Tracking:** The software contains no cookies, web beacons, tracking scripts, or analytics beacons.

---

## 4. Fair Lending and Algorithmic Transparency

- **Interpretable Models:** The project utilizes Logistic Regression, a transparent and interpretable statistical learning algorithm. The decision boundaries and odds-ratios can be inspected directly to ensure unbiased evaluations.
- **No Sensitive Demographics:** The algorithms do not ingest protected characteristics such as race, gender, religion, marital status, or nationality. Eligibility is calculated solely based on creditworthiness indicators.

---

## 5. Security Safeguards

- Code is distributed under standard open-source principles allowing full code audits.
- No network ports are opened during execution.
- Any generated plots (`loan_eligibility_plot.png`, `loan_eligibility_scikit_plot.png`) are saved locally in the project directory.

---

## 6. User Rights and Compliance

Under international data privacy standards (including the EU GDPR and the Indian Digital Personal Data Protection Act, 2023):
- Users have the right to access, inspect, and delete any local dataset files used with this software.
- Users can run, modify, or retrain the algorithms on their own private datasets with complete data isolation.

---

## 7. Contact & Inquiries

For any questions, clarifications, or concerns regarding this policy, please open an issue on GitHub or contact:

**Harish**  
GitHub: [@Haris87-star](https://github.com/Haris87-star)  
Email: `harishhari781823@gmail.com`  
Repository: [edubridge-miniproject3](https://github.com/Haris87-star/edubridge-miniproject3)
