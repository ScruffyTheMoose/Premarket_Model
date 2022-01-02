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

for symbol in etfs:
    try:
        output = si.get_data(ticker=symbol, start_date=start, end_date=end)
        output.to_csv(path_or_buf=f"etf_data/{symbol}.csv")
    except Exception:
        print(symbol + "is bad, it needs to be killed with fire.")
        etfs.remove(symbol)