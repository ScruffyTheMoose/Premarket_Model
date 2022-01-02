import yahoo_fin.stock_info as si
import pandas as pd
import datetime as dt

# chosen start/end dates
# different companies will have different ranges of available data so this will need to be handled during data processing
start = dt.datetime(2010, 1, 1)
end = dt.datetime(2021, 12, 1)

# ETFs that we'll be collecting data for
stocks = si.tickers_sp500()

# collecting historical data from 2010-01-01 to 2021-12-01 and saving to csv
for symbol in stocks:
    try:
        output = si.get_data(ticker=symbol, start_date=start, end_date=end)
        output.to_csv(path_or_buf=f"stock_data/{symbol}.csv")
    except Exception:
        print(symbol + " produced an error when retrieving data, continuing...")
        stocks.remove(symbol)