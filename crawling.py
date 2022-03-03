from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import csv
import time

#1. csv file open
csv_name = "main_all.csv"
csv_open = open(csv_name, "w+", encoding="utf-8")
csv_writer = csv.writer(csv_open)
csv_writer.writerow(("drink", "image_url"))

#2. Driver & BeautifulSoup
driver = webdriver.Chrome(ChromeDriverManager().install())

crawling_url = "https://www.startbucks.co.kr/menu/drink_list.do"
driver.get(crawling_url)

#3. Parsing html code
full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')

time.sleep(3)

#4. Get element selector (1)
categories = soup.select('#mCSB_1_container > li')

#5. Get element selector (2)
for i in range(2, len(categories) + 1):
     element = driver.find_element_by_css_selector(f'#mCSB_1_container > li:nth-child({i})')
     category_name = element.text
     time.sleep(2)
     element.click()

     full_html = driver.page_source
     soup = BeautifulSoup(full_html, 'html.parser')

     titles = soup.select(f'#container > div.content > div.product_result_wrap.product_result_wrap01 > div > dl > dd:nth-child(2) > div.product_list > dl > dd:nth-child({(i-1)*2}) > ul > li > dl > dt > a > img')

     #6. print drink_title, image url
     for i, title in enumerate(titles):
          print('title: ', title['alt'])
          print('original src: ', title['src'])
          print('image_url: ', title['src'].split('/')[4:])
          url = crawling_url + '/' + '/'.join(title['src'].split('/')[4:])
