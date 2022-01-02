import yahoo_fin.stock_info as si
import pandas as pd
import datetime as dt

start = dt.datetime(2015, 1, 1)
end = dt.datetime(2021, 12, 1)

output = si.get_data(ticker='VOO', start_date=start, end_date=end)
output.to_csv(path_or_buf='testcsv.csv')