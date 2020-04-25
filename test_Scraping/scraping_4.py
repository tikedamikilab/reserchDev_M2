from datetime import datetime as dt
import time
from time import sleep
import itertools
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--headless')
driver = webdriver.Chrome('C:\Program Files\Chrome Driver\chromedriver',options=options)

#ここから問題を選択してidを集める
baseurl = 'https://codeforces.com/problemset/'
submission = "935"
submissionid = "35502951"
page = "A"

url = baseurl + "submission/" + submission + "/" + submissionid
print(url)
driver.get(url)  
sleep(1)

soup = BeautifulSoup(driver.page_source, features="html.parser")

text = [n.get_text() for n in soup.select('ol li span')]
el = [n['class'] for n in soup.select('ol li span')]

elflat = list(itertools.chain.from_iterable(el))
strtext = ' '.join(text)
strel = ' '.join(elflat)

countel = len(elflat)
elli = [n for n in soup.select('ol li')]
countlen = len(elli)

print(strel)

