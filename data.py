data = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
#Downloading S&P 500 stock data 
data['Symbol'] = data['Symbol'].str.replace('.','-')
symbols_list = data['Symbol'].unique().tolist()
#Making the symbols more readable
end_date = '2024-08-25'
start_date = pd.to_datetime(end_date) - pd.DateOffset(years=5)
df = yf.download(tickers=symbols_list, start=start_date, end=end_date)
