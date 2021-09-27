# import needed modules
import math
from pandas_datareader import data as pdr
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
# set the start and end dates
start_date = "2019-07-01"
end_date = "2020-08-26"
# obtain stock price
ticker = "KR"
stock = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
#calculate returns 
stock['ret_stock'] =(stock['Adj Close']/stock['Adj Close'].shift(1))-1
#calculate moving averages
stock.dropna(inplace=True) 
stock['avg3m']=stock['ret_stock'].rolling(63).mean()
# get the stock price for KR on June 25
price0825=stock['Adj Close']['2020-08-25']
print(f'the stock price for {ticker} on August 25 is: $',round_up(price0825,2))
# get the predicted stock return on June 26
expected_ret=stock['avg3m']['2020-08-25']
print(f'the expected stock return for {ticker} on August 26 is: $',round_up(expected_ret,2))
# Predict stock price on June 26
expected_price=price0825*(1+expected_ret)
print(f'the expected stock price for {ticker} on August 26 is: $',round_up(expected_price,2))

