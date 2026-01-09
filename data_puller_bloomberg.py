import pandas as pd
import numpy as np
from xbbg import blp

#Portfolio construction

stock_selection = pd.read_excel('stockselection.xlsx')
tickers =  list(zip(
    stock_selection['Ticker'], 
    stock_selection['Weighting']
    ))

if tickers:
    print(f'Current porfolio composition is {tickers}')
