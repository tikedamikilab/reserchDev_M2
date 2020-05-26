# Scraping5
# 
# 以下の形式のcsvがいる
# 65612362,Nov/24/2019 03:24,deodeo,4A - Watermelon,Perl,Accepted,92 ms,0 KB,2019-11-24 03:24:00
#
# 複数回acがあるときは，最後のac
# -*- coding:utf8  -*-

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
import re

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--headless')
driver = webdriver.Chrome('C:\Program Files\Chrome Driver\chromedriver',options=options)

baseurl = 'https://codeforces.com/problemset/'

#ここから問題を選択してidを集める
#################################
#手書き
submission = ""
page = "A"
#################################

with open('./datasets/python_selectC.csv',encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        submission = row[9]
        submissionid = row[0]
        url = baseurl + "submission/" + submission + "/" + str(submissionid)
        print(url)
        driver.get(url)  
        sleep(1)

        soup = BeautifulSoup(driver.page_source, features="html.parser")

        text = [n.get_text() for n in soup.select('ol li span')]
        sleep(0.2)
        el = [n['class'] for n in soup.select('ol li span')]
        sleep(0.2)
        elflat = list(itertools.chain.from_iterable(el))

        strtext = ' '.join(text)
        strel = ' '.join(elflat)
        countel = len(elflat)
        elli = [n for n in soup.select('ol li')]
        sleep(0.2)
        countlen = len(elli)

        with open('scraping5.csv', 'a',newline='',encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([submissionid, row[8], row[2], row[3],row[4],row[5],countlen, countel, strtext, strel,row[6], row[7], row[9]])
