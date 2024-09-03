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

#Plotting a risk cluster, color coded based on momentum 

def plot_with_risk_clusters(aggdata):
    colors = {'Low Risk': 'green', 'High Risk': 'red', 'Swing': 'grey'}
        for risk_category, color in colors.items():
        cluster_data = aggdata[aggdata['risk'] == risk_category]
        plt.scatter(cluster_data['rsi'], cluster_data['atr'], color=color, label=risk_category)

#Legend
    plt.xlabel('RSI')
    plt.ylabel('ATR')
    plt.legend()
    plt.grid(True)
    plt.title('Risk Clusters Based on Momentum')
