from logging import error
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import csv


#INPUT FROM USER

# OPEN AND INTERACT WITH THE SHOPEE WEBSITE
driver = webdriver.Chrome()
itemA = "vaseline"
driver.maximize_window()
#OPEN AND INTERACT WITH THE SHOPEE WEBSITE
#driver.maximize_window()
driver.get("https://shopee.ph/?gclid=CjwKCAjwzMeFBhBwEiwAzwS8zJCW11U9mwVk-ITyDKjBU0OfHJ92-eiCx9ANbOcWftFM-hIqf7b2_BoCB-IQAvD_BwE")

#CLOSE POP-UP
WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//div[@class ='shopee-popup__close-btn']"))).click()
sleep(2)

#ENTER INPUT IN SEARCH BOX
search_box = driver.find_element_by_class_name('shopee-searchbar-input__input')
search_box.send_keys(itemA)
search_box.send_keys(Keys.ENTER)
sleep(2)

fivestar = driver.find_element_by_class_name('_1LYq_U').click()

container =[]
Categories = []


nameContainer = []
#SCROLL DOWN SLOWLY
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 2):
  driver.execute_script("window.scrollTo(0, {});".format(i))


#BACK TO TOP
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")

#GET DATA FROM WEBSITE INDIVIDUALLY
items = driver.find_elements_by_xpath('//div[@class="col-xs-2-4 shopee-search-item-result__item"]')
for item in items:
    Name = item.find_element_by_xpath('.//*[@class="fBhek2 _2xt0JJ"]/div[2]/div/div').text
    nameContainer.append(Name)
    #print(Name)

count = len(nameContainer)
x=int(1)
#original for i in range(count)
for i in range(5):
        driver.find_element_by_xpath('.//*[@class="row shopee-search-item-result__items"]/div['+str(x)+']/a').click()
        sleep(2)
        Name=driver.find_element_by_xpath('.//*[@class="attM6y"]/span').text
        sleep(1)
        Price = driver.find_element_by_xpath('.//*[@class="_3e_UQT"]').text
        try:
            numRate = driver.find_element_by_xpath('.//*[@class="OitLRu"]').text
        except:
            numRate = driver.find_element_by_xpath('.//*[@class="_119xyB"]').text
        seller = driver.find_element_by_xpath('.//*[@class="_3uf2ae"]').text
        link = driver.current_url
        try:
            img_div = driver.find_element_by_xpath('.//*[@property="og:image"]')
            img_url = img_div.get_attribute("content")
        except:
            img_url = None

        Categories.append([Name,Price,numRate,seller,link,img_url])
        print(Name)
        print(Price)
        print(numRate)
        print(seller)
        print(link)
        print(img_url)
        x=x+1
        driver.back()
        sleep(3)