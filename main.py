# -*- coding: utf-8 -*-
"""
EduBridge Mini-Project 3: Loan Eligibility Prediction Suite
Author: Harish (Haris87-star)
Repository: https://github.com/Haris87-star/edubridge-miniproject3
"""

import sys

def main():
    print("=" * 60)
    print("  EduBridge Mini-Project 3: Loan Eligibility Prediction")
    print("  Author: Harish (GitHub: @Haris87-star)")
    print("=" * 60)
    print("Select an implementation to run:")
    print("  1. Scikit-Learn Logistic Regression Pipeline (Li.py)")
    print("  2. Custom BFGS Optimization Logistic Regression (eligibilityy.py)")
    print("  3. Run Both Models")
    print("=" * 60)

    choice = sys.argv[1] if len(sys.argv) > 1 else "3"

    if choice in ("1", "3"):
        print("\n--> Running Scikit-Learn Pipeline (Li.py)...")
        import Li
    if choice in ("2", "3"):
        print("\n--> Running Custom BFGS Optimization (eligibilityy.py)...")
        import eligibilityy

    print("\nExecution completed successfully!")

if __name__ == "__main__":
    main()
