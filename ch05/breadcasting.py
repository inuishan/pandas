from pandas import Series, DataFrame
import pandas as pd
import numpy as np
frame = DataFrame(np.arange(16.).reshape((4,4)),columns=list('abcd'),index=list('efgh'))
#print frame
ser = frame.ix[0]
#print ser
#print frame-ser #broadcasting

#broadcasting over rows
ser3 = frame['d']
print ser3