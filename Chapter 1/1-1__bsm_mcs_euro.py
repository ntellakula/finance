"""
Example 1-1. Monte Carlo valuation of European call option
Monte Carlo valuation of European Call Option
    Black-Scholes-Merton model
    
1-1__bsm_mcs_euro.py
"""

#Necessary modules
import numpy as np

#Parameter values
S0 = 100.   #initial share index value
K = 105.    #strke price
T = 1.0     #time to maturity (1 year)
r = 0.05    #riskless short rate
sigma = 0.2 #volatility of the stock

I = 100000  #number of simulations


#Actual valuation algorithm
z = np.random.standard_normal(I)    #pseudorandom numbers
#index values at maturity - random
ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * z)
hT = np.maximum(ST - K, 0)          #inner values at maturity
C0 = np.exp(-r * T) * np.sum(hT) / I #Monte Carlo estimator

#Result Output
print("Value of the European Call Option %5.3f" % C0)
#First run: 8.011
