#Garman-Klass-Yang-Zhang Historical Volatility
df['garman_klass_vol'] = np.sqrt(((np.log(df['high']) - np.log(df['low']))**2)/2 - (2*np.log(2) - 1) * (np.log(df['adj close']) - np.log(df['open']))**2)
