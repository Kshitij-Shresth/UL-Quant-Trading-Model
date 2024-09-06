# UL-Quant-Trading-Model

![image](https://github.com/user-attachments/assets/bae92b22-e8e8-4304-bf5c-99f6f0fa7682)

This project provides a comprehensive framework for analyzing stock momentum and risk using advanced data processing, clustering, and visualization techniques.  Momentum investing capitalizes on the continuation of existing price trends, where stocks that have performed well in the past are expected to continue performing well in the future. By identifying high-momentum stocks and their associated risk levels, this project provides actionable insights that can be leveraged by traders, investors, and portfolio managers to enhance decision-making processes.

# Key Financial Concepts

## Fama-French 5-Factor Model:

The Fama-French 5-factor model enhances the analysis by accounting for multiple sources of return, including market, size, value, profitability, and investment factors. Incorporating this model allows the project to contextualize momentum within broader market dynamics and adjust for factors that could influence returns beyond momentum alone.

### Implementation: 
By calculating rolling factor betas, the project captures the sensitivity of stocks to these factors over time. Shifting these betas forward aligns them with future returns, providing a forward-looking risk-adjusted view of stock performance.

## Momentum Analysis:

Securities that have performed well in the past continue to perform well in the near term. This project uses momentum as a signal for potential future performance, allowing investors to make informed buy or sell decisions. The Relative Strength Index (RSI) is a popular momentum indicator that measures the speed and change of price movements.

### Implementation: 
By calculating the average Relative Strength Index (RSI) over a three-month period, we identify stocks with high and low momentum, providing a quantitative basis for momentum classification.

## Average True Range:

ATR is used alongside RSI to capture volatility, providing a broader view of a stock's behavior. High ATR values suggest higher volatility, which is crucial for understanding the potential risk associated with a stock.

### Implementation: 
Clustering helps in segmenting stocks into distinct groups based on shared characteristics. This project uses KMeans clustering on features like RSI and Average True Range (ATR) to identify patterns and group stocks with similar risk profiles.

## Risk Categorization:

Understanding the risk profile of stocks is crucial for constructing portfolios that align with an investor’s risk tolerance and investment objectives. By categorizing stocks into 'Green' (high momentum, lower risk) and 'Red' (low momentum, higher risk) the project offers a clear framework for risk assessment.

### Implementation: 
Stocks are classified into risk groups based on their momentum scores. The top 20% in momentum are labeled as 'Green,' indicating strong performance and potential for continued growth. Conversely, the bottom 20% are labeled as 'Red,' signaling potential underperformance or higher risk.

