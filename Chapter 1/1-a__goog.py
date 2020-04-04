"""
Example 1-a. Volatility of Google stock over the past 5 years
Volatiilty of Google stock over the past 5 years

1-a__goog.py


Steps:
    1. Download Google stock price data from the Web
    2. Calculate rolling standard deviations of the log returns (volatility)
    3. Plot the stock price data and the results
"""

#Necessary modules
import numpy as np
import pandas as pd
import pandas_datareader.data as web

#Retrieve the stock data
source = web.DataReader("GOOG", data_source = "stooq")
source = source.reindex(index = source.index[::-1])

#Calculate log return
source["log_return"] = np.log(source["Close"] / source["Close"].shift(1))
#shift moves the data one level

#Calculte volatility
source["volatility"] = source.log_return.rolling(252).std() * np.sqrt(252)

#Plot the results
source[["Close", "volatility"]].plot(subplots = True, color = "blue")