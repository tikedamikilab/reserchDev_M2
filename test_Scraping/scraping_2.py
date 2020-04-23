from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('C:\Program Files\Chrome Driver\chromedriver',options=options)
error_flg = False
target_url = 'https://codeforces.com/problemset/status/4/problem/A/'
driver.get(target_url)  
sleep(1)
try:
    statusinput = driver.find_element_by_id("verdictName")
    statuselement= Select(statusinput)
    statuselement.select_by_value("anyVerdict")
    statusinput.submit()

    contestStatus = []
    cnt=0
    for el_tr in driver.find_elements_by_xpath('//tr[not(contains(@class,"first-row"))]'):
        if cnt > 15:
            el_view = el_tr.find_elements_by_xpath('//a[@class="view-source"]')
            print(el_view.text)
        cnt += 1
        print(cnt)
    # for el_view in driver.find_elements_by_xpath('//tr/td/a[@class="view-source"]'):
    #     print(el_view.text)
    #     sleep(1)

    #     el_tr = el_view.find_elements_by_xpath("..")
    #     sleep(1)
    #     el_who = el_tr.find_elements_by_class("rated-user")
    #     print(el_who.text)

    print("できた？")
    sleep(1)
except Exception:
    error_flg = True
    print('エラーが発生しました。')