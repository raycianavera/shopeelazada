from logging import error
from flask import Flask, render_template, request    
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homesearch.html")
    
@app.route("/", methods=['POST'])
def getvalue():

     #INPUT FROM USER
    itemB = request.form['sBox']
    
    try:
        itemA = itemB
        #Column variables
        Name = ""
        Price = 0.0
        numRate = 0
        seller =""
        link =""
        img_url = ""

        #OPEN AND INTERACT WITH THE SHOPEE WEBSITE
        
        #chrome_options.add_argument("--headless")
        
        
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        # OR options.add_argument("--disable-gpu")

        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        #driver = webdriver.Chrome(chrome_options=chrome_options)
        
        driver.maximize_window()
        driver.get("https://shopee.ph/?gclid=CjwKCAjwzMeFBhBwEiwAzwS8zJCW11U9mwVk-ITyDKjBU0OfHJ92-eiCx9ANbOcWftFM-hIqf7b2_BoCB-IQAvD_BwE")

        #CLOSE POP-UP
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//div[@class ='shopee-popup__close-btn']"))).click()
        sleep(2)

        #ENTER INPUT IN SEARCH BOX
        search_box = driver.find_element_by_class_name('shopee-searchbar-input__input')
        search_box.send_keys(itemA)
        search_box.send_keys(Keys.ENTER)
        sleep(2)

        #Click 5 star rating
        #fivestar = driver.find_element_by_class_name('_1LYq_U').click()     

        #ARRAY CONTAINER DECLARATION
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
        for i in range(10):
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
            driver.back()
            sleep(3)
            x=x+1

        #WRITE DATA IN CSV FILE
        with open('IMP.csv', 'w', encoding='utf-8') as file:
            Import = csv.writer(file,lineterminator='\n')
            Import.writerows(Categories)
  
        #READ DATA IN CSV FILE
        with open('IMP.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file,lineterminator='\n')
            contents = list(reader)

        shopimg1 = contents[0][5]
        shopname1= contents[0][0]
        shopprice1 = contents[0][1]
        shopratings1 = contents[0][2]
        shopsell1 = contents[0][3]
        shoplink1 = contents[0][4]

        shopimg2 = contents[1][5]
        shopname2= contents[1][0]
        shopprice2 = contents[1][1]
        shopratings2 = contents[1][2]
        shoplink2 = contents[1][4]
        shopsell2 = contents[1][3]

        shopimg3 = contents[2][5]
        shopname3= contents[2][0]
        shopprice3 = contents[2][1]
        shopratings3 = contents[2][2]
        shoplink3 = contents[2][4]
        shopsell3 = contents[2][3]

        shopimg4 = contents[3][5]
        shopname4= contents[3][0]
        shopprice4 = contents[3][1]
        shopratings4 = contents[3][2]
        shoplink4 = contents[3][4]
        shopsell4 = contents[3][3]
        
        shopimg5 = contents[4][5]
        shopname5= contents[4][0]
        shopprice5 = contents[4][1]
        shopratings5 = contents[4][2]
        shoplink5 = contents[4][4]
        shopsell5 = contents[4][3]

        shopimg6 = contents[5][5]
        shopname6= contents[5][0]
        shopprice6 = contents[5][1]
        shopratings6 = contents[5][2]
        shoplink6 = contents[5][4]
        shopsell6 = contents[5][3]

        shopimg7 = contents[6][5]
        shopname7= contents[6][0]
        shopprice7 = contents[6][1]
        shopratings7 = contents[6][2]
        shoplink7 = contents[6][4]
        shopsell7 = contents[6][3]

        shopimg8 = contents[7][5]
        shopname8= contents[7][0]
        shopprice8 = contents[7][1]
        shopratings8 = contents[7][2]
        shoplink8 = contents[7][4]
        shopsell8 = contents[7][3]

        shopimg9 = contents[8][5]
        shopname9= contents[8][0]
        shopprice9 = contents[8][1]
        shopratings9 = contents[8][2]
        shopsell9 = contents[8][3]
        shoplink9 = contents[8][4]
        
        shopimg10 = contents[9][5]
        shopname10= contents[9][0]
        shopprice10 = contents[9][1]
        shopratings10 = contents[9][2]
        shoplink10 = contents[9][4]
        shopsell10 = contents[9][3]
        
        # OPEN AND INTERACT WITH LAZADA WEBSITE
        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        #driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.maximize_window()
        driver.get("https://www.lazada.com.ph/")


        #ENTER INPUT IN SEARCH BOX
        search_box = driver.find_element_by_class_name('search-box__input--O34g')
        search_box.send_keys(itemA)
        search_box.send_keys(Keys.ENTER)
        sleep(3)

        lazCategories = []
        
        
        #driver.find_element_by_xpath('.//div[@class="index__filter-list___1Z8nj"]/div[6]/div[2]/div/ul').click()
        #sleep(0.5)
       

        i = int(1)
        counter = int(1)
        for i in range(10):
            driver.find_element_by_xpath('.//*[@class="index__box___1Ffv-"]/div['+str(counter)+']').click() #open a selected product
            sleep(1)
            lazName = driver.find_element_by_xpath('.//*[@id="module_product_title_1"]/div/div/h1').text
            lazPrice = driver.find_element_by_xpath('.//*[@id="module_product_price_1"]/div/div/span').text
            lazRating = driver.find_element_by_xpath('.//*[@id="module_product_review_star_1"]/div/a[1]').text
            lazlink = driver.current_url
            try:
                lazSeller = driver.find_element_by_xpath('//*[@id="module_seller_info"]/div/div[1]/div[1]/div[2]/a').text
            except:
                lazSeller = '---NO SELLER---'
            try:
                lazimg_div = driver.find_element_by_xpath('.//*[@name="og:image"]') #select image
                lazimg_url = lazimg_div.get_attribute("content") #save image and convert to text/link
            except:
                lazimg_url = None

            lazCategories.append([lazName,lazPrice,lazRating,lazSeller,lazlink,lazimg_url]) 
            driver.back()
            sleep(3)
            counter=counter+1

        #WRITE DATA IN CSV FILE
        with open('lazIMP.csv', 'w', encoding='utf-8') as file:
            Importlaz = csv.writer(file,lineterminator='\n')
            Importlaz.writerows(lazCategories)
  
        #READ DATA IN CSV FILE
        with open('lazIMP.csv', 'r', encoding='utf-8') as file:
            lazreader = csv.reader(file,lineterminator='\n')
            lazcontents = list(lazreader)

        lazimg1 = lazcontents[0][5]
        lazname1= lazcontents[0][0]
        lazprice1 = lazcontents[0][1]
        lazratings1 = lazcontents[0][2]
        lazlink1 = lazcontents[0][4]
        lazsell1 = lazcontents[0][3]

        lazimg2 = lazcontents[1][5]
        lazname2= lazcontents[1][0]
        lazprice2 = lazcontents[1][1]
        lazratings2 = lazcontents[1][2]
        lazlink2 = lazcontents[1][4]
        lazsell2 = lazcontents[1][3]

        lazimg3 = lazcontents[2][5]
        lazname3= lazcontents[2][0]
        lazprice3 = lazcontents[2][1]
        lazratings3 = lazcontents[2][2]
        lazlink3 = lazcontents[2][4]
        lazsell3 = lazcontents[2][3]

        lazimg4 = lazcontents[3][5]
        lazname4= lazcontents[3][0]
        lazprice4 = lazcontents[3][1]
        lazratings4 = lazcontents[3][2]
        lazlink4 = lazcontents[3][4]
        lazsell4 = lazcontents[3][3]
        
        lazimg5 = lazcontents[4][5]
        lazname5= lazcontents[4][0]
        lazprice5 = lazcontents[4][1]
        lazratings5 = lazcontents[4][2]
        lazlink5 = lazcontents[4][4]
        lazsell5 = lazcontents[4][3]
        
        lazimg6 = lazcontents[5][5]
        lazname6= lazcontents[5][0]
        lazprice6 = lazcontents[5][1]
        lazratings6 = lazcontents[5][2]
        lazlink6 = lazcontents[5][4]
        lazsell6 = lazcontents[5][3]

        lazimg7 = lazcontents[6][5]
        lazname7= lazcontents[6][0]
        lazprice7 = lazcontents[6][1]
        lazratings7 = lazcontents[6][2]
        lazlink7 = lazcontents[6][4]
        lazsell7 = lazcontents[6][3]

        lazimg8 = lazcontents[7][5]
        lazname8= lazcontents[7][0]
        lazprice8 = lazcontents[7][1]
        lazratings8 = lazcontents[7][2]
        lazlink8 = lazcontents[7][4]
        lazsell8 = lazcontents[7][3]

        lazimg9 = lazcontents[8][5]
        lazname9= lazcontents[8][0]
        lazprice9 = lazcontents[8][1]
        lazratings9 = lazcontents[8][2]
        lazlink9 = lazcontents[8][4]
        lazsell9 = lazcontents[8][3]
        
        lazimg10 = lazcontents[9][5]
        lazname10= lazcontents[9][0]
        lazprice10 = lazcontents[9][1]
        lazratings10 = lazcontents[9][2]
        lazlink10 = lazcontents[9][4]
        lazsell10 = lazcontents[9][3]

        return render_template("results.html", shopimg1 = shopimg1, shopname1 = shopname1, shopprice1 =shopprice1,
        shopratings1 = shopratings1, shoplink1 = shoplink1, shopimg2 = shopimg2, shopname2 = shopname2,shopprice2 = shopprice2,
        shopratings2 = shopratings2, shoplink2 = shoplink2, shopimg3 = shopimg3, shopname3 = shopname3, shopprice3 = shopprice3,
        shopratings3 = shopratings3, shoplink3 = shoplink3, shopimg4 = shopimg4, shopname4 = shopname4,shopprice4 = shopprice4,
        shopratings4 = shopratings4, shoplink4 = shoplink4, shopimg5 = shopimg5, shopname5 = shopname5, shopprice5 = shopprice5,
        shopratings5 = shopratings5, shoplink5 = shoplink5,
        shopratings6 = shopratings6, shoplink6 = shoplink6, shopimg6 = shopimg6, shopname6 = shopname6,shopprice6 = shopprice6,
        shopratings7 = shopratings7, shoplink7 = shoplink7, shopimg7 = shopimg7, shopname7 = shopname7,shopprice7 = shopprice7,
        shopratings8 = shopratings8, shoplink8 = shoplink8, shopimg8 = shopimg8, shopname8 = shopname8,shopprice8 = shopprice8,
        shopratings9 = shopratings9, shoplink9 = shoplink9, shopimg9 = shopimg9, shopname9 = shopname9,shopprice9 = shopprice9,
        shopratings10 = shopratings10, shoplink10 = shoplink10, shopimg10 = shopimg10, shopname10 = shopname10,shopprice10 = shopprice10,
        lazimg1 = lazimg1, lazname1 = lazname1, lazprice1 = lazprice1, lazratings1 = lazratings1, lazlink1 = lazlink1,
        lazimg2 = lazimg2, lazname2 = lazname2, lazprice2 = lazprice2, lazratings2 = lazratings2, lazlink2 = lazlink2,
        lazimg3 = lazimg3, lazname3 = lazname3, lazprice3 = lazprice3, lazratings3 = lazratings3, lazlink3 = lazlink3,
        lazimg4 = lazimg4, lazname4 = lazname4, lazprice4 = lazprice4, lazratings4 = lazratings4, lazlink4 = lazlink4,
        lazimg5 = lazimg5, lazname5 = lazname5, lazprice5 = lazprice5, lazratings5 = lazratings5, lazlink5 = lazlink5,
        lazimg6 = lazimg6, lazname6 = lazname6, lazprice6 = lazprice6, lazratings6 = lazratings6, lazlink6 = lazlink6,
        lazimg7 = lazimg7, lazname7 = lazname7, lazprice7 = lazprice7, lazratings7 = lazratings7, lazlink7 = lazlink7,
        lazimg8 = lazimg8, lazname8 = lazname8, lazprice8 = lazprice8, lazratings8 = lazratings8, lazlink8 = lazlink8,
        lazimg9 = lazimg9, lazname9 = lazname9, lazprice9 = lazprice9, lazratings9 = lazratings9, lazlink9 = lazlink9,
        lazimg10 = lazimg10, lazname10 = lazname10, lazprice10 = lazprice10, lazratings10 = lazratings10, lazlink10 = lazlink10,
        shopsell1 = shopsell1,  shopsell2 = shopsell2,  shopsell3 = shopsell3,shopsell4 = shopsell4,shopsell5 = shopsell5,shopsell6 = shopsell6, 
        shopsell7 = shopsell7,   shopsell8 = shopsell8, shopsell9 = shopsell9,  shopsell10 = shopsell10,
        lazsell1 = lazsell1, lazsell2 = lazsell2, lazsell3 = lazsell3, lazsell4 = lazsell4, lazsell5 = lazsell5, lazsell6 = lazsell6, lazsell7 = lazsell7,
        lazsell8 = lazsell8,  lazsell9 = lazsell9, lazsell10 = lazsell10           
        )

    except:
        return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)


