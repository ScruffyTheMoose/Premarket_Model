import yahoo_fin.stock_info as si
import pandas as pd
import datetime as dt

# chosen start/end dates
# different companies will have different ranges of available data so this will need to be handled during data processing
start = dt.datetime(2010, 1, 1)
end = dt.datetime(2021, 12, 1)

# format for retrieving historical prices in DF format from yahoo and saving to csv for ease-of-use
# output = si.get_data(ticker='VOO', start_date=start, end_date=end)
# output.to_csv(path_or_buf='testcsv.csv')

# ETFs that we'll be collecting data for
etfs = pd.read_csv('etfs.csv')['etfs'].tolist()


# collecting historical data from 2010-01-01 to 2021-12-01 and saving to csv
for symbol in etfs:
    try:
        output = si.get_data(ticker=symbol, start_date=start, end_date=end)
        output.to_csv(path_or_buf=f"etf_data/{symbol}.csv")
    except Exception:
        print(symbol + " produced an error when retrieving data, continuing...")
        etfs.remove(symbol) # removing from list incase we need to use this list later