# CAPM Analysis

## Overview
This project implements the Capital Asset Pricing Model (CAPM) to analyze stocks and calculate expected returns.

### Files
- **CAPM_functions.py:** Contains helper functions to create interactive plots, normalize stock prices, calculate daily returns, and compute beta.
- **CAPM_return.py:** Main Streamlit app that takes user input for stocks and time period, downloads data, calls CAPM functions, and displays analysis.
- **requirements.txt:** Python package dependencies.
- **Calculate_Beta.py:** Secondary Streamlit app to analyze a single stock in more detail.

### Usage
The main analysis app can be run with:
```bash
streamlit run CAPM_return.py
