from ast import keyword
from os import link
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
services = Service('chromedriver.exe')
driver = webdriver.Chrome(service=services, options=options)

link  = "https://twitter.com/"
keyword = "python"
driver.set_window_size(1920, 1080)
driver.get(link)
time.sleep(5)

driver.find_element(By.XPATH, '//input[@data-testid="SearchBox_Search_Input"]').click()
time.sleep(1)

search = driver.find_element(By.XPATH, '//input[@data-testid="SearchBox_Search_Input"]')
search.send_keys(keyword)
search.send_keys(Keys.ENTER)
time.sleep(5)

for i in range(1, 3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("Scroll ke-", i)
    time.sleep(2)

html = driver.page_source
driver.quit()
time.sleep(3)
soup = BeautifulSoup(html, 'html.parser')

i = 1
tweet_name = []
data_tweet = []
for data in soup.find_all('div', class_="css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu"):
    print("Tweet ke-", i)
    nama_tweet = data.find('div', class_="css-901oao r-1awozwy r-1nao33i r-6koalj r-37j5jr r-a023e6 r-b88u0q r-rjixqe r-bcqeeo r-1udh08x r-3s2u2q r-qvutc0").get_text()
    body_tweet = data.find('div', class_="css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0").get_text()
    tweet_name.append(nama_tweet)
    data_tweet.append(body_tweet)
    i+=1
    print("-------------------------")

df = pd.DataFrame({'Nama': tweet_name, 'Tweet': data_tweet})
write = pd.ExcelWriter('data_tweet.xlsx')
df.to_excel(write, sheet_name='Sheet1', index=False)
write.save()


