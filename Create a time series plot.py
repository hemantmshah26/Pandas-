# Create a timeseries plot for 1 year
timeseries  = pd.Series(np.random.randn(365), index = pd.date_range('1/1/2014', periods = 365))
# perform a cumilative sum
timeseries = timeseries.cumsum()
timeseries.plot()
