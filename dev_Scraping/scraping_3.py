# scraping3
# submitリストを取得する
#
# csvへの追記を行うため．実行注意
#

import pandas as pd
from datetime import datetime as dt
import time
from urllib import request  # urllib.requestモジュールをインポート
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート

#ここから問題を選択してidを集める
# baseurl = 'https://codeforces.com/problemset/'
# status = "268"
# problem = "A"
# page = str(1)

def makesolvedcsv(status, problem = 'A', max = 1, folder = "sample_scraping3"):
    for i in range(1,max+1):
        page = str(i)
        baseurl = 'https://codeforces.com/problemset/'
        url = baseurl + "status/" + str(status) + "/problem/" + problem + "/page/" + page
        print(url)

        try:
            data = pd.read_html(url, header = 0)
            data[0].dropna(inplace = True)
            data[0]["datetime"] = [dt.strptime(i, '%b/%d/%Y %H:%M') for i in data[0]["When"]]
            
            data[0].to_csv("./"+folder+"/sample_status"+ str(status) + "_problem" + problem + ".csv", header=False, index=False, mode='a')
        except KeyError as e:
            print('catch KeyError:', e)

if __name__ == '__main__':
    for i in range(1000):
        makesolvedcsv(i, max=5, problem='C')
