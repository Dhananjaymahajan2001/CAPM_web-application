CAPM Analysis
This project implements the Capital Asset Pricing Model (CAPM) to analyze stocks and calculate expected returns.

Overview
The project contains the following files:

CAPM_functions.py: Contains helper functions to create interactive plots, normalize stock prices, calculate daily returns, and compute beta.
CAPM_return.py: Main Streamlit app that takes user input for stocks and time period, downloads data, calls CAPM functions, and displays analysis.
requirements.txt: Python package dependencies.
Calculate_Beta.py: Secondary Streamlit app to analyze a single stock in more detail.
Usage
The main analysis app can be run with:


Copy code
streamlit run CAPM_return.py
This will launch a web interface to select stocks, years of historical data to analyze, and view comparative charts and CAPM analysis.

The single stock analysis can be run with:


Copy code
streamlit run Calculate_Beta.py
This displays a stock's beta, expected return, and regression against the S&P 500.

Customization
The stock options and number of years can be configured directly in CAPM_return.py. Additional analysis functions can be added to CAPM_functions.py.

Requirements
Requires Python and the packages in requirements.txt, including Streamlit, Pandas, Numpy, Plotly etc.

References
Implementation is based on the Capital Asset Pricing Model theory from financial economics.
