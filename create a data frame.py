import pandas as pd
import numpy as np
# define a date range 
dates = pd.date_range('20160501', periods = 10)
dates
# create a dataframe with above 10 dates as index and colums defined as ABCDE
dataframe = pd.DataFrame(np.random.randn (10,5), index = dates, columns =list ('ABCDE'))
dataframe 
