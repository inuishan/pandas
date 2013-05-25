from pandas import Series, DataFrame
import pandas as pd
import numpy as np
ser = Series(['a','b',np.nan,'c'])
print ser.isnull()