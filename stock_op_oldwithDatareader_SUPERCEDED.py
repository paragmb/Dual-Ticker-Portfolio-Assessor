
"""Stock Optimizer Application

This is a command line application to optimize stock portfolio.


"""
import sys
import fire
import questionary
import os
import numpy as np
import pandas as pd
import pandas_datareader as web
from datetime import datetime
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation
from matplotlib import pyplot as plt

def get_investor_info():
    """Prompt dialog to get the investor's stock and initial investment information.

    Returns:
        Returns the investor's information.
    """
    print(f"Select 2 Stocks: AAPL, F, TWTR, FB, AAL, AMZN, GOOGL, ^GSPC")
    ticker1 = questionary.text("What's your stock1 symbol/ticker?").ask()
    ticker2 = questionary.text("What's your stock2 symbol/ticker?").ask()
    ratio1 = questionary.text("What's your ratio for stock1?").ask()
    ratio2 = questionary.text("What's your ratio for stock2?").ask()
    inves_amt = questionary.text("What's your investment amount?").ask()

    ticker1 = str(ticker1)
    ticker2 = str(ticker2)
    ratio1 = float(ratio1)
    ratio2 = float(ratio2)
    inves_amt = float(inves_amt)

    return ticker1, ticker2, ratio1, ratio2, inves_amt


def pull_stock_data(ticker1, ticker2):
    """used to grab the stock prices, with yahoo
       basis: 3 years of historical data
    """
    start = datetime(2019, 1, 31)
    symbols_list=[]  
    symbols_list.append(ticker1) 
    symbols_list.append(ticker2)
    stock_data=[]
    #pull price using iex for each symbol in list defined above
    for ticker in symbols_list:
        r = web.DataReader(ticker, 'yahoo', start)
        # add a symbol column
        r['Symbol'] = ticker
        stock_data.append(r)
    df = pd.concat(stock_data, axis=1)
    df = df.reset_index()
    df = df[['Date','Close', 'Symbol']]
    # df = df.set_index('Date')
    df = df.rename(columns={df.columns[1]: "close"})
    df = df.rename(columns={df.columns[2]: "close"})
    print(df)
    print("Testing line 1")
    return df
    
def sharpe_ratio(df):
    sp_df = df.drop(df.columns[[3,4]], axis=1)  
    sp_df = sp_df.set_index('Date') 
    #sp_df = sp_df.rename(columns={sp_df.columns[0]: "close"})
    print(sp_df)
    sp_df = sp_df.pct_change()
    year_trading_days = 252
    average_annual_return = sp_df.mean() * year_trading_days
    annualized_standard_deviation = sp_df.std() * (year_trading_days) ** (1 / 2)
    sharpe_ratios = average_annual_return / annualized_standard_deviation
    print(f"This are the shape ratio {sharpe_ratios}")
    print("test line 2")
    #sharpe_ratios.plot.bar(title="Sharpe Ratios")
    #plt.show()
    
    return sp_df

def fin_forecast(ratio1, ratio2, sp_df):
    """used to forecast 3 years of financial forecast/projection
    """
    print("print test line 6")
    forecast = MCSimulation(
        portfolio_data = sp_df,
        weights = [ratio1, ratio2],
        num_simulation = 500,
        num_trading_days = 252*3
    )
    print("test line 3")
    print(forecast.portfolio_data.head())
    simulation = forecast.portfolio_data
    #return ratio1, ratio2, sp_df
    return simulation

def run():
    """The main function for running the script."""

    
    # Get the investor's information
    ticker1, ticker2, ratio1, ratio2, inves_amt = get_investor_info()

    # used to grab the stock prices, with yahoo
    df = pull_stock_data(ticker1, ticker2)

    print("testing line 5")
    sp_df = sharpe_ratio(df)
    
    fin_forecast(ratio1,ratio2,sp_df)
    
    
if __name__ == "__main__":
    fire.Fire(run)
