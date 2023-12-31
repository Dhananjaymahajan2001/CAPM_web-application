# importing libraries

import plotly.express as px
import numpy as np

# Creating interactive chart

def interactive_plot(df):
    fig = px.line()
    for i in df.columns[1:]:
        fig.add_scatter(x = df['Date'],y=df[i], name = i)
    fig.update_layout(width = 450, margin = dict(l=20,r=20,t=50,b=20), legend = dict(orientation = 'h', yanchor = 'bottom',
        y = 1.02, xanchor = 'right', x=1, ))
    return fig

# Normalization of prices based on initial prices
def normalize(df_2):
    df = df_2.copy()
    for i in df.columns[1:]:
        df[i] = df[i]/df[i][0] # current price of the stock/initial price of the stock
    return df

# Daily Returns
def daily_return(df):
    df_daily_return = df.copy()
    df_daily_return[df.columns[1:]] = (df[df.columns[1:]].pct_change() * 100).fillna(0)
    return df_daily_return

# function to calculate beta
def cal_beta(stocks_daily_return, stock):
    rm = stocks_daily_return['sp500'].mean()*252

    # Fit a polynomial between each stock and the S&P500
    b, a = np.polyfit(stocks_daily_return['sp500'], stocks_daily_return[stock],1)
    return b,a
