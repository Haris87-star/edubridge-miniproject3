# EduBridge Mini-Project 3: Loan Eligibility Prediction

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Privacy Policy](https://img.shields.io/badge/Privacy%20Policy-Compliant-brightgreen.svg)](PRIVACY.md)
[![Author](https://img.shields.io/badge/Author-Harish-orange.svg)](https://github.com/Haris87-star)
[![Repository](https://img.shields.io/badge/GitHub-edubridge--miniproject3-blue.svg)](https://github.com/Haris87-star/edubridge-miniproject3)

An intelligent binary classification and machine learning system for predicting personal loan approvals based on credit score (CIBIL) and requested loan amount. This repository delivers both an **industry-standard scikit-learn pipeline** and a **first-principles mathematical optimization** of Logistic Regression using BFGS.

---

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Mathematical Foundation](#-mathematical-foundation)
- [Repository Structure](#-repository-structure)
- [Installation & Setup](#-installation--setup)
- [How to Run](#-how-to-run)
- [Outputs & Visualizations](#-outputs--visualizations)
- [Privacy Policy & Data Security](#-privacy-policy--data-security)
- [License](#-license)
- [Author & Acknowledgments](#-author--acknowledgments)

---

## 📖 Project Overview

Determining loan approval requires balancing borrower risk against credit appetite. This project models credit decision-making through two complementary implementations:

1. **Scikit-Learn Machine Learning Pipeline (`Li.py`):**
   - Applies `StandardScaler` to handle disparate feature scales (CIBIL: 300–900 vs. Loan Amount: 5–40 Lakhs).
   - Trains a `LogisticRegression` classifier.
   - Evaluates applicant approval probabilities ($P(\text{Eligible})$).
   - Generates a smooth 2D decision boundary contour plot.

2. **First-Principles Optimization (`eligibilityy.py` / `eligibility.py`):**
   - Implements custom vectorized sigmoid activation and log-likelihood cost function.
   - Leverages Quasi-Newton BFGS numerical minimization (`scipy.optimize.minimize`).
   - Computes explicit linear decision boundaries and generates high-resolution scatter plots.

---

## ⚡ Key Features

- **Dual Implementation:** Choose between rapid scikit-learn pipelines or raw numerical optimization.
- **Decision Boundary Visualization:** Intuitive plots distinguishing eligible vs. non-eligible borrower spaces.
- **Probability Scores:** Provides confidence levels for marginal applicants.
- **Data Privacy by Design:** 100% offline, local compute with synthetic data safeguards.
- **Zero Configuration:** Ready to run out of the box with Python 3.9+.

---

## 📐 Mathematical Foundation

### 1. Hypothesis Function (Sigmoid Activation)
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$
$$h_\theta(x) = \sigma(\theta^T x) = \frac{1}{1 + e^{-(\theta_0 + \theta_1 x_1 + \theta_2 x_2)}}$$

Where:
- $x_1$: CIBIL score (normalized)
- $x_2$: Loan amount requested (normalized)
- $\theta$: Model parameter vector

### 2. Binary Cross-Entropy Cost Function
$$J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} \left[ y^{(i)} \log(h_\theta(x^{(i)})) + (1 - y^{(i)}) \log(1 - h_\theta(x^{(i)})) \right]$$

### 3. BFGS Optimization
Finds optimal parameter vector $\theta^*$:
$$\theta^* = \arg\min_{\theta} J(\theta)$$

### 4. Decision Boundary Equation
At the threshold $P = 0.5$, $\theta^T x = 0$:
$$\theta_0 + \theta_1 x_1 + \theta_2 x_2 = 0 \implies x_2 = -\frac{\theta_0 + \theta_1 x_1}{\theta_2}$$

---

## 📂 Repository Structure

```text
edubridge-miniproject3/
│
├── Li.py                                # Scikit-learn Logistic Regression pipeline & 2D contour plot
├── eligibilityy.py                      # Custom BFGS-based Logistic Regression model
├── eligibility.py                       # Standard entry point and model inspector
├── main.py                              # Unified CLI runner for both implementations
├── requirements.txt                     # Project dependencies
├── LICENSE                              # MIT License
├── PRIVACY.md                           # Comprehensive Data Privacy Policy
├── PRIVACY_POLICY.md                    # Privacy policy reference document
├── .gitignore                           # Git ignore configuration
│
├── Screenshot 2026-10-11 152725 (1).png  # Visual proof and terminal execution output
└── Screenshot 2026-10-12 234117.png     # Visual proof of decision boundary graph
```

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Haris87-star/edubridge-miniproject3.git
   cd edubridge-miniproject3
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 How to Run

### Run Unified Project Runner:
```bash
python main.py
```

### Run Scikit-Learn Pipeline:
```bash
python Li.py
```
*Output:*
```text
accuracy on training data: 0.86

Predictions for new applicants:
   Cibil  LoanAmount  eligible_pred  eligible_prob
0    580           8              0           0.18
1    700          20              1           0.76
2    790          35              1           0.97
```

### Run Custom BFGS Model:
```bash
python eligibilityy.py
# or
python eligibility.py
```

---

## 📊 Outputs & Visualizations

The models generate graphical decision boundaries highlighting approval zones:
- **Green markers:** Eligible applicants ($y = 1$)
- **Red markers:** Ineligible applicants ($y = 0$)
- **Dashed line / Contours:** Decision boundary separating the two risk classes.

### Project Screenshots:
| Output Graph | Execution & Verification |
|:---:|:---:|
| ![Decision Boundary Graph](Screenshot%202026-10-12%20234117.png) | ![Execution Verification](Screenshot%202026-10-11%20152725%20(1).png) |

---

## 🔒 Privacy Policy & Data Security

We take financial data privacy seriously:
- All datasets provided are synthetic or anonymized.
- The models process all data **100% locally** on your machine.
- No network requests, tracking cookies, or cloud analytics are implemented.
- Read our full [PRIVACY.md](PRIVACY.md) for complete details.

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author & Acknowledgments

- **Author:** **Harish**
- **GitHub:** [@Haris87-star](https://github.com/Haris87-star)
- **Email:** `harishhari781823@gmail.com`
- **Course / Program:** EduBridge Machine Learning Mini-Project Series
