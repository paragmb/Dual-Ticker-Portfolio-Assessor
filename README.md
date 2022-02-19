# Project1 - Dual-Ticker Portfolio Assessor

This is a command-line interface application that gives the user the ability to compare returns on 2 stocks after financial analysis for a sound (preliminary) investment decision (before taking a deep dive) and further consulting a certified financial advisor.

---

## Project Overview

User will be able to choose 2 stock tickers with a capability to enter weight percentages (of investment mix). Based on the input a quantitative analysis (performance, volatility, risk, risk-return) with visuals will be performed. Further, a financial forecasting of cumulative returns will be calculated and based on another user input of initial investment, a projected future value (95% confidence interval) of investment will be presented.

---

## Assumptions

- Quantitative analysis based on 3 years of historical data (01/31/2019 to 01/31/2022)
- Financial forecasting analysis based on 3-yr MCSimulation
- For the weights parameter, user must list the weight of each asset in the order that the assets appear in the DataFrame (hence enter the stock ticker in alphabetcal order  e.g. AAX should be entered before AAY and so on)

---

## Technologies

This project leverages python 3.9.7 with the following main packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entry-point.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

* [alpaca](https://github.com/alpacahq/alpaca-trade-api-python) - For historical stock price data

* [bokeh](https://github.com/bokeh/bokeh) - For interactive graphs from Holoviews etc in Visual Studio

---

## Usage

Ensure the conda dev environment is activated.

Using CLI, please run the python file "stock_op.py". When prompted:

User needs to be ready with the following information: 
- *Stock1 ticker* 
- *Stock2 ticker* 
- *Ratio/weight for Stock1* 
- *Ratio/weight for Stock2*
- *Investment Amount*

---

## Quantitative Analysis

Useful insights can be gained from the quantitative plots. The dip in Apple (AAPL) stock is due to split of shares during that period. Amazon (AMZN) stock has performed better than AAPL during last 3 yrs data. The Sharpe ratio shows the gain in relation to the risk. The returns have gone higher for both stocks after Covid pandemic. The quantitative analysis plots are as follows:

### Daily Return - Portfolio and S&P 500
<img src="Images/Daily_Return_Box.png" width="400" height="300">

### Cumulative Returns - Portfolio and S&P 500
<img src="Images/Daily_Return_Box.png" width="400" height="300">

### Daily Return - Portfolio and S&P 500 (Box Plot)
<img src="Images/Daily_Return_Box.png" width="400" height="300">

### Rolling 21-day Standard Deviation - Portfolio and S&P 500
<img src="Images/Daily_Return_Box.png" width="400" height="300">

### Sharpe Ratios - Portfolio and S&P 500
<img src="Images/Daily_Return_Box.png" width="400" height="300">

---

## Fianancial Forecasting Analysis

Monte Carlo algorithm is used to predict future stock values. Past stock values downloaded using Alpaca APIs are used to create a normal distribution of past daily returns. Monte Carlo algorithm uses past daily return normal distribution to predict future daily values and cumulative returns by randomly selecting values from the distribution and propagating the stock's current value into the future. Cumulative returns are calculated from the future stock values and plotted for 500 simulations. All simulations are numerically different from each other due to the randomly selected daily return values from the normal distribution. Cumulative return probability distribution is also shown as a bar graph to illustrate the most probable future scenario range from all 500 simulations. 95% Confidence interval and its boundary values are also given for information. These boundary values should be evaluated together with the future cumulative return distribution. The financial forecasting analysis plots are as follows:

### Monte Carlo Simulation 
<img src="Images/Daily_Return_Box.png" width="400" height="300">

### Distribution of Cumulative Returns
<img src="Images/Daily_Return_Box.png" width="400" height="300">

### Future Value
<img src="Images/Daily_Return_Box.png" width="400" height="300">

---

## Contributors

Bolaji Ajimotokan, Onur Guvener, Parag Borkar

---

