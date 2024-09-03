#Using our clusters to find high momentum stocks over a set time period

def find_highest_momentum_stocks(aggdata):
    end_date = aggdata.index.get_level_values('date').max()
    start_date = end_date - pd.DateOffset(months=3)   
    recent_data = aggdata[(aggdata.index.get_level_values('date') >= start_date) & (aggdata.index.get_level_values('date') <= end_date)]

#Calculating the average RSI for each stock over the last 3 months
    recent_rsi = recent_data.groupby('ticker')['rsi'].mean()

#Sorting stocks based on such, higher RSI -> higher momentum
    sorted_stocks = recent_rsi.sort_values(ascending=False)


    print("Stocks with highest momentum over the past 3 months:")
    print(sorted_stocks)

find_highest_momentum_stocks(aggdata)
