# Scraping6
# 
# 以下の形式のcsvがいる
# 65612362,Nov/24/2019 03:24,deodeo,4A - Watermelon,Perl,Accepted,92 ms,0 KB,2019-11-24 03:24:00
#
# 複数回acがあるときは，最後のac
# 
# 問題文を全部集めるやつ
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

#ここから問題を選択してidを集める
#################################
#手書き
# submission = "4"
# page = "A"
#################################

def makeproblemtext(submission, page = 'A', folder = 'datasets_problemText'):

    baseurl = 'https://codeforces.com/problemset/'
    url = baseurl + "problem/" + str(submission) + "/" + str(page)
    print(url)
    driver.get(url)  
    sleep(1)

    soup = BeautifulSoup(driver.page_source, features="html.parser")

    text = [n.get_text() for n in soup.select("div[class='problem-statement'] div p")]
    text_input = [n.get_text() for n in soup.select("div[class='problem-statement'] div[class='input-specification'] p")]
    text_output = [n.get_text() for n in soup.select("div[class='problem-statement'] div[class='output-specification'] p")]
    text_note = [n.get_text() for n in soup.select("div[class='problem-statement'] div[class='note'] p")]

    text_problem = []
    for t in text:
        flag = 0
        for t_in in text_input:
            if t == t_in:
                flag = 1
        for t_out in text_output:
            if t == t_out:
                flag = 1
        for t_note in text_note:
            if t == t_note:
                flag = 1
        if flag == 0:
            text_problem.append(t)

    sleep(0.2)

    with open('./'+ folder +'/scraping6.csv', 'a',newline='',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([submission , ' '.join(text_problem), ' '.join(text_input), ' '.join(text_output), ' '.join(text_note)])

if __name__ == '__main__':
    for i in range(1, 1000):
        makeproblemtext(i, page='C')