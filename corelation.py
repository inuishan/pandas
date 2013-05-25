from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import pandas.io.data as web
all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')
#print all_data    
price = DataFrame({tic: data['Adj Close'] for tic, data in all_data.iteritems()})
volume = DataFrame({tic: data['Volume'] for tic, data in all_data.iteritems()})
returns = price.pct_change()
#print returns
#print returns.tail()
print returns.MSFT.corr(returns.IBM)
print returns.corr()
