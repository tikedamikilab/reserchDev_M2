# scraping3
# submitリストを取得する

import pandas as pd
from datetime import datetime as dt
import time
from urllib import request  # urllib.requestモジュールをインポート
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート

#ここから問題を選択してidを集める
baseurl = 'https://codeforces.com/problemset/'
status = "1329"
problem = "A"
page = str(1)

for i in range(1,10):
    page = str(i)
    url = baseurl + "status/" + status + "/problem/" + problem + "/page/" + page
    print(url)

    data = pd.read_html(url, header = 0)
    data[0].dropna(inplace = True)

    data[0]["datetime"] = [dt.strptime(i, '%b/%d/%Y %H:%M') for i in data[0]["When"]]
    data[0].to_csv("sample_status"+ status + "_problem" + problem + ".csv", header=False, index=False, mode='a')

#data[0].set_index("Date2", inplace=True)
#print(data[0]["datetime"].head())
#string_date_1 = 'Apr 23, 2020'
#print(dt.strptime(string_date_1, '%b %d, %Y'))