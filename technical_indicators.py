#Garman-Klass-Yang-Zhang Historical Volatility
df['garman_klass_vol'] = np.sqrt(((np.log(df['high']) - np.log(df['low']))**2)/2 - (2*np.log(2) - 1) * (np.log(df['adj close']) - np.log(df['open']))**2)
#Realtive strength index at a lookback period of 25 
df['rsi'] = df.groupby(level=1)['adj close'].transform(lambda x: pandas_ta.rsi(close=x, length=25))

