import pandas as pd
from datetime import datetime as dt

url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL&.tsrc=fin-srch'

data = pd.read_html(url, header = 0)
data[0].dropna(inplace = True)
#print(data[0].tail())

#data[0]["Date2"] = [dt.strptime(i, '%b %d, %Y') for i in data[0]["Date"]]
#print(data[0].tail())
#data[0].set_index("Date2", inplace=True)

#string_date_1 = 'Apr 23, 2020'
#print(dt.strptime(string_date_1, '%b %d, %Y'))