df.unstack('ticker')['dollar_volume'].resample('M').mean().stack().to_frame('dollar_volume')
#
