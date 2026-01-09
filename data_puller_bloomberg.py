import pandas as pd
import numpy as np
from xbbg import blp

#Portfolio construction
print(blp.bdp("LLY US Equity", ["EQY_BETA", "EQY_BETA_BMK"]))

stock_selection = pd.read_excel('stockselection.xlsx')
# for types in list(set(stock_selection['Sec Type'])):
stock_selection['api_ticker'] = np.where(
    stock_selection['Sec Type'] = 'Equity',
    stock_selection['Ticker'] +'Equity',
    stock_selection['Ticker']
)

tickers =  list(set(stpcl)
    stock_selection['Ticker'], 
    stock_selection['Weighting'],
    stock_selection['Sec Type']
    )
for tick in tickers:


if tickers:
    print(f'Current porfolio composition is {tickers}')
else: 
    print('No underlying positions selected')



#Pull prices from bloomberg
print(blp.bdh(
    tickers='AAPL US', 
    flds=['High'],
    start_date='2020-01-01',
    end_date='today'
              ))

