import pandas as pd
import pandas.io.data
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import os

#s = pd.Series([1,3,5,np.nan,6,8])
#print s

#dates = pd.date_range('20130101',periods=6)
#print dates

#for date in dates:
#    print date

#df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
#print df

#df2 = pd.DataFrame({ 'A' : 1.,
#                     'B' : pd.Timestamp('20130102'),
#                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
#                     'D' : np.array([3] * 4,dtype='int32'),
#                     'E' : 'foo' })
#print df2

#df = pd.io.data.get_data_yahoo('AAPL',
#                                 start=datetime.datetime(2006, 10, 1),
#                                 end=datetime.datetime(2014, 2, 12))
#aapl.to_csv('data/aapl_ohlc.csv')
#close_px = df['Adj Close']
#mavg = pd.rolling_mean(close_px, 40) ## moving average
#print close_px

#close_px.plot(label='AAPL')
#mavg.plot(label='mavg')
#plt.legend()
#plt.show()

df = pd.io.data.get_data_yahoo(['AAPL', 'GE', 'GOOG', 'IBM', 'KO', 'MSFT', 'PEP'],
                               start=datetime.datetime(2010, 1, 1),
                               end=datetime.datetime(2013, 1, 1))['Adj Close']
rets = df.pct_change()
plt.scatter(rets.PEP, rets.KO)
plt.xlabel('Returns PEP')
plt.ylabel('Returns KO')
plt.show()
