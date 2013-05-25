import pandas as pd
import numpy as np
from pandas import Series, DataFrame
#ser = Series([1,2,3,4])
#print ser
#print ser.values
#print ser.index
#ser2 = Series([1,2,3,4], index=[1,2,3,4])
#print ser2[2]
#print ser2[ser2>2]
#print np.exp(ser2)
dict2 = {'a':1,'b':2}
ser = Series(dict2,index=['a','c'])
#print ser
print pd.isnull(ser)
print pd.notnull(ser)
print "Hellelujai"