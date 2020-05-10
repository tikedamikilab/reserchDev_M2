from urllib import request  # urllib.requestモジュールをインポート
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート

url = 'https://codeforces.com/problemset/status/4/problem/A'
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()

# 得られたsoupオブジェクトを操作していく

findid_all = soup.find_all('a', class_ = 'view-source')
#print(findid_all[0])
for item in findid_all:
    findid = item.text
    print(findid)
