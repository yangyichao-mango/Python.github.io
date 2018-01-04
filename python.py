import requests
import bs4
import re
import time
import pymysql

from selenium import webdriver

con = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    db="python",
    port=3306,
    use_unicode=True,
    charset="utf8"
)
cursor = con.cursor()

driver = webdriver.Chrome()
count = 0
for i in range(1, 16 , 1):
    url = 'https://zh.airbnb.com/s/Shanghai--China/homes?cdn_cn=1&s_tag=ejxIlhR7&allow_override%5B%5D=&section_offset={}'.format(
        str(i))
    driver.get(url)
    # print(i)
    #if i == 1270:
    #   elements = driver.find_elements_by_class_name('mod-1')
    #  for element in elements:
    #     element.click()

    time.sleep(2)
    html = driver.page_source#获取网页的html数据、
    soup = bs4.BeautifulSoup(html,'lxml')#对html进行解析
    r = soup.find_all('div', class_='_v72lrv')

    for tag in r:

        url = 'https://zh.airbnb.com/'+str(tag.find('a',class_="_j4ns53m").get('href'))
        title = str(tag.find('div',class_="_ew0cqip").text)
        priceContent = tag.find('span',class_="_hylizj6")
        priceTmp = priceContent.find_all('span')[2].text
        price = priceTmp.strip().lstrip().rstrip(',')

        # price = str(priceContent.find('span').text)
        type = str(tag.find('small',class_='_5y5o80m').text)

        if tag.find('span',class_='_gb7fydm'):
            comments = tag.find('span',class_='_gb7fydm').text
        else:
            comments = 'NEW'

        print(url)
        print(title)
        print(price[1:].strip().lstrip().rstrip(','))
        print(type)
        print(comments + '\n')

        sql = "INSERT INTO Airbnb_Shanghai(url,title,price,type,comments) values(" \
              + url + "," + title + "," + price[1:] + "," + type + "," + comments +")"
        print(sql)
        cursor.execute(sql)
        con.commit()
