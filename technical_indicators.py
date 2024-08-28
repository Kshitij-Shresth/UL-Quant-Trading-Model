#Garman-Klass-Yang-Zhang Historical Volatility
df['garman_klass_vol'] = np.sqrt(((np.log(df['high']) - np.log(df['low']))**2)/2 - (2*np.log(2) - 1) * (np.log(df['adj close']) - np.log(df['open']))**2)
#Realtive strength index at a lookback period of 25 
df['rsi'] = df.groupby(level=1)['adj close'].transform(lambda x: pandas_ta.rsi(close=x, length=25))
#Lower, middle and upper Bollinger Bands for the log-adjusted closing prices
df['bb_low'] = df.groupby(level=1)['adj close'].transform(lambda x: pandas_ta.bbands(close=np.log1p(x), length=25).iloc[:, 0])
df['bb_mid'] = df.groupby(level=1)['adj close'].transform(lambda x: pandas_ta.bbands(close=np.log1p(x), length=25).iloc[:, 1])
df['bb_high'] = df.groupby(level=1)['adj close'].transform(lambda x: pandas_ta.bbands(close=np.log1p(x), length=25).iloc[:, 2])
