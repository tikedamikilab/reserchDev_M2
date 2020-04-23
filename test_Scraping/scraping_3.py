import pandas as pd
from datetime import datetime as dt

#url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL&.tsrc=fin-srch'
url = 'https://codeforces.com/problemset/'
status = "451"
problem = "A"
page = str(1)

url = url + "status/" + status + "/problem/" + problem + "/page/" + page
print(url)
#url = "https://codeforces.com/problemset/status/451/problem/A/page/1"
data = pd.read_html(url, header = 0)
data[0].dropna(inplace = True)

#print(data[0]["When"].head())

data[0]["datetime"] = [dt.strptime(i, '%b/%d/%Y %H:%M') for i in data[0]["When"]]
print(data[0]["datetime"].head())

data[0].to_csv("status"+ status + "_problem" + problem + ".csv", header=False, mode='a')

#data[0].set_index("Date2", inplace=True)
#string_date_1 = 'Apr 23, 2020'
#print(dt.strptime(string_date_1, '%b %d, %Y'))