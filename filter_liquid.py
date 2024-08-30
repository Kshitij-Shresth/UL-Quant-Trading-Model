last_cols = [c for c in df.columns.unique(0) if c not in ['dollar_volume','volume','open', 'high','low','close']]
aggdata = pd.concat(
    [
        df.unstack('ticker')['dollar_volume'].resample('M').mean().stack().to_frame('dollar_volume'),
        df.unstack()[last_cols].resample('M').last().stack('ticker')
    ],
    axis=1
).dropna()
#Aggregating data to monthly level features in a new dataframe
