from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome('C:\Program Files\Chrome Driver\chromedriver')
error_flg = False
target_url = 'https://codeforces.com/problemset/status/4/problem/A/'
driver.get(target_url)  
sleep(3)
try:
    statusinput = driver.find_element_by_id("verdictName")
    statuselement= Select(statusinput)
    statuselement.select_by_value("anyVerdict")
    statusinput.submit()

    for el_t in driver.find_elements_by_xpath('//td/a[@class="view-source"]'):
        print(elem_h3.text)

    print("できた？")
    sleep(3)
except Exception:
    error_flg = True
    print('エラーが発生しました。')