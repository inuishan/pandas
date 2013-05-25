from pandas import Series, DataFrame
import pandas as pd
import numpy as np
obj = Series([1,-5,2,2,4])
print obj.rank()
print obj.rank(method='first')