# -*- coding: utf-8 -*-
"""
Loan Eligibility Prediction using Custom Logistic Regression (BFGS)
EduBridge Mini-Project 3
Author: Harish (Haris87-star)
Repository: https://github.com/Haris87-star/edubridge-miniproject3
"""

from eligibilityy import df, theta, sigmoid, X, y

if __name__ == "__main__":
    print(f"Model parameters (theta): {theta}")
    print(f"Total applicants evaluated: {len(df)}")
    print(f"Eligible applicants count: {df['eligible'].sum()}")
