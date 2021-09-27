from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv
import pandas as pd

driver = webdriver.Chrome('C://Users//Muhammad Qasim//Desktop//chromedriver//chromedriver.exe')

def getListOfAds():

    listOfIds=[]
    s_url = "https://www.facebook.com/ads/library/?id="
    driver.get('https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&q=nike')
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(7)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(12)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(15)
    br = 0
    for i in driver.find_elements_by_class_name('o0aczdgd'):
        data = i.text
        x = data.lstrip("ID: ")
        final = s_url + x
        listOfIds.append(final)
        br += 1
        if br == 10:
            print(br)
            break

    return listOfIds

def toString(a):
    str1 = ' , '.join(a)
    return str1

def saveData(dataset):
    with open('data.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Media'])
        for player in dataset:

            writer.writerow([player.title,toString(player.media)])


class Ads():

    def __init__(self,url):
        self.url=url
        self.title = None
        self.media = []
        self.code=None

    def getTitle(self):
        try:
            driver.get(self.url)
            self.code=driver.page_source
            time.sleep(5)
            title = driver.find_element_by_class_name('_7jyr')
            soup=BeautifulSoup(title.get_attribute('innerHTML'),'lxml')
            self.title=soup.text
        except:

            self.title="No Title"


        for i in driver.find_elements_by_class_name('_7jys'):
            self.media.append(i.get_attribute("src"))

        if len(self.media)==0:
            for i in driver.find_elements_by_class_name('_8o0a'):
                self.media.append(i.find_element_by_tag_name('video').get_attribute("src"))


listOfIds=getListOfAds()
DataSet=[]
# listOfIds=None
# with open('text') as file:
#     listOfIds=file.readlines()


for i in listOfIds:
    obj=Ads(i)
    obj.getTitle()
    DataSet.append(obj)

saveData(DataSet)
driver.quit()
