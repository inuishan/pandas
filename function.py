from pandas import Series, DataFrame
import pandas as pd
import numpy as np
frame = DataFrame(np.random.randn(4,3),columns=list('abc'))
#print frame
#print np.abs(frame)
f = lambda x: x.max() - x.min()
print frame
print frame.apply(f)
print frame.apply(f,axis=1)
#print frame
#to sort data based on value use order methodn 
