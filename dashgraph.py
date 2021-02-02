import datetime
import pandas_datareader.data as web

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
df = web.DataReader("TSLA", 'stooq', start, end)


print(df.head())