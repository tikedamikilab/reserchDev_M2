# Scraping4
# 
# 以下の形式のcsvがいる
# 65612362,Nov/24/2019 03:24,deodeo,4A - Watermelon,Perl,Accepted,92 ms,0 KB,2019-11-24 03:24:00

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
import csv

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--headless')
driver = webdriver.Chrome('C:\Program Files\Chrome Driver\chromedriver',options=options)

baseurl = 'https://codeforces.com/problemset/'

with open('sample_status4_problemA.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        #ここから問題を選択してidを集める
        #################################
        #手書き
        submission = "4"
        page = "A"
        #################################
        submissionid = row[0]
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

        with open('source_submission' + submission +'_page'+page+'.csv', 'a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([submissionid, row[8], row[2], row[3],row[4],row[5],row[6],row[7],countlen, countel, strtext, strel])
