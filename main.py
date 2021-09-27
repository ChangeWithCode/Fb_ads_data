from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import re

driver = webdriver.Chrome('C://Users//Muhammad Qasim//Desktop//chromedriver//chromedriver.exe')


def getListOfAds():
    listOfIds = []
    xd = []
    driver.get('https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&q=nike')
    time.sleep(5)
    while len(listOfIds) <= 100:
        for i in driver.find_elements_by_class_name('_9cd3'):
            x = [int(s) for s in i.text.split() if s.isdigit()]
            if len(x) == 1:
                listOfIds.append(x)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
    for i in listOfIds:
        xd.append(i[0])
    return set(xd)


class Ads():
    def __init__(self):
        self.driver = None
        self.id = None
        self.title = None
        self.media = []


listOfIds = getListOfAds()
for i in listOfIds:
    print(i)

driver.quit()
