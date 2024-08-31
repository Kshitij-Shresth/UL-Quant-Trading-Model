#Using Fama French Factors to assess risk return profile + Rolling factor betas
ffdata = web.DataReader("F-F_Research_Data_5_Factors_2x3", "famafrench", start="2015")[0].drop("RF", axis=1)
ffdata.index = ffdata.index.to_timestamp()
ffdata.index = ffdata.index.tz_localize('UTC')

#Resampling monthly and normalizing the values 
ffdata = ffdata.resample("M").last().div(100)
ffdata.index.name = 'date'
ffdata = ffdata.join(aggdata['return_1m']).sort_index()
