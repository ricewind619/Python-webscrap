from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.keys import Keys

# Topics: Locate a button, select element within dropdown and extract data from a table

# define the website to scrape and path where the chromediver is located
# IIT H link website: http://10.79.9.77:8080/assamScrutinyLive/
# Path C:/Program Files (x86)/chromedriver.exe

website = 'http://10.79.9.77:8080/assamScrutinyLive/'
#Path = 'C:/Program Files (x86)/chromedriver.exe' # write the path here

#SELENIUM FIXES
service = Service()
options = webdriver.ChromeOptions()
#THIS ONE IS TO PREVENT AUTO SHUTDOWN OF CHROME
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

#COMMENT OUT CODE
# website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
# path = '/Users/frank/Downloads/chromedriver' # write the path here


# define 'driver' variable
# driver = webdriver.Chrome(Path)
# open Google Chrome with chromedriver
driver.get(website)

time.sleep(15)

# CODE BLOCK TO LOG IN
# XPaths
# Login id: //*[@id="uid"] 
# Password: //*[@id="pswrd"]
# Sign in button: //*[@id="login"]



driver.find_element(By.XPATH, '//*[@id="uid"]').send_keys('papori')
driver.find_element(By.XPATH, '//*[@id="pswrd"]').send_keys('pn@2023')
driver.find_element(By.XPATH, '//*[@id="login"]').click()

time.sleep(15)

# FILER AND NON FILER CHOOSING
# XPATH FOR DETERMINATION OF TAX: //*[@id="navbarSupportedContent"]/ul/li[2]/a
# XPATH FOR FILERS: //*[@id="navbarSupportedContent"]/ul/li[2]/ul/li[1]/a
# VISIBLE TEXT FOR FILERS: For GSTR-09 Filers 

# # select dropdown and select element inside by visible text
determination_of_tax = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a')
determination_of_tax.click()
# filers = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/ul/li[1]/a')
# filers.click()
non_filers = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/ul/li[2]/a')
non_filers.click()
time.sleep(10)

#select for 200 entries
# xpath for dropdown //*[@id="pageCombo"]
#//*[@id="pageCombo"]/option[13]

page = driver.find_element(By.XPATH, '//*[@id="pageCombo"]')
dropdown = Select(page)
dropdown.select_by_value("200")
option_200 = driver.find_element(By.XPATH, '//*[@id="pageCombo"]/option[13]')
option_200.click()

time.sleep(5)
#//*[@id="pageTo"]
number_of_pages = driver.find_element(By.XPATH, '//*[@id="pageTo"]').text
print("Number of pages is " + str(number_of_pages))
pages_in_number = int(number_of_pages)
loop_end = int(number_of_pages) + 1
##pagination > div.pageRight > div.pageNav > span.lnk.right
next_page_button = driver.find_element(By.CSS_SELECTOR,"#pagination > div.pageRight > div.pageNav > span.lnk.right")
print("Next page button found")
# driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
# driver.execute_script("arguments[0].click();", next_page_button)

serial = []
zone = []
unit = []
circle = []
legal_name = []
trade_name = []
gstn = []
email = []
mobile = []
address = []
activity = []
year_2017_18 = []
year_2018_19 = []


for page in range(1, loop_end):
   


    #SCRAPING TABLE DATA
    #Filer
    #table_total = driver.find_elements(By.XPATH, '//*[@id="oicNonComplaintUI"]/tr')
    #Non Filer
    #//*[@id="srTableUI"]/tr
    table_total = driver.find_elements(By.XPATH, '//*[@id="srTableUI"]/tr')

    #XPaths
    # CORRECT XPATH FULL: //*[@id="oicNonComplaintUI"]/tr[1]/td[1]/span[1]
    # Serial: //*[@id="oicNonComplaintUI"]/tr[1]/td[1]/span[1]
    # Zone: //*[@id="oicNonComplaintUI"]/tr[1]/td[2]/span[1]
    # UNIT: //*[@id="oicNonComplaintUI"]/tr[1]/td[2]/span[2]
    # CIRCLE: //*[@id="oicNonComplaintUI"]/tr[1]/td[2]/span[3]
    # GSTN: //*[@id="oicNonComplaintUI"]/tr[1]/td[3]/span[1]
    # LEGAL NAME: //*[@id="oicNonComplaintUI"]/tr[1]/td[3]/span[2]
    # TRADE NAME: //*[@id="oicNonComplaintUI"]/tr[1]/td[3]/span[3]
    # EMAIL: //*[@id="oicNonComplaintUI"]/tr[1]/td[4]/span[1]
    # MOBILE: //*[@id="oicNonComplaintUI"]/tr[1]/td[4]/span[2]
    # ADDRESS: //*[@id="oicNonComplaintUI"]/tr[1]/td[4]/span[3]
    # 2017-18: //*[@id="oicNonComplaintUI"]/tr[1]/td[6]
    # 2018-19: //*[@id="oicNonComplaintUI"]/tr[1]/td[6]


    # serial = []
    # zone = []
    # unit = []
    # circle = []
    # legal_name = []
    # trade_name = []
    # gstn = []
    # email = []
    # mobile = []
    # address = []
    # activity = []
    # year_2017_18 = []
    # year_2018_19 = []


    for data in table_total:
        serial.append(data.find_element(By.XPATH,'./td[1]/span[1]').text)
        zone.append(data.find_element(By.XPATH,'./td[2]/span[1]').text)
        circle.append(data.find_element(By.XPATH,'./td[2]/span[3]').text)
        unit.append(data.find_element(By.XPATH,'./td[2]/span[2]').text)    
        gstn.append(data.find_element(By.XPATH,'./td[3]/span[1]').text)
        legal_name.append(data.find_element(By.XPATH,'./td[3]/span[2]').text)
        trade_name.append(data.find_element(By.XPATH,'./td[3]/span[3]').text)
        email.append(data.find_element(By.XPATH,'./td[4]/span[1]').text)
        mobile.append(data.find_element(By.XPATH,'./td[4]/span[2]').text)
        address.append(data.find_element(By.XPATH,'./td[4]/span[3]').text)
        print("LOOP ITERATION DONE")
    
    if (int(page)<pages_in_number):
        print("Scroll to botton and click")
        elem = driver.find_element(By.TAG_NAME, "html")
        elem.send_keys(Keys.END)
        print("Srolled to bottom")
        next_page_button = driver.find_element(By.CSS_SELECTOR,"#pagination > div.pageRight > div.pageNav > span.lnk.right")
        print("Next page button found")
        driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
        driver.execute_script("arguments[0].click();",next_page_button)
        # go to next page 
        # //*[@id="pagination"]/div[2]/div[1]/span[3]
        #//*[@id="pagination"]/div[2]/div[1]/span[3]
        #/html/body/div[4]/div[1]/div/div[3]/div[3]/div[8]/div[2]/div[1]/span[3]
        #lnk right
        #next_page_button = driver.find_element(By.CLASS_NAME,"lnk right")
        #next_page_button = driver.find_element(By.XPATH,'//*[@id="pagination"]/div[2]/div[1]/span[3]')
        #next_page_button.click()
        print("NEXT PAGE BUTTON CLICKED")
        time.sleep(5)

# # Bonus: Create Dataframe in Pandas and export to CSV (Excel)
df = pd.DataFrame({'serial': serial, 'zone': zone, 'circle': circle, 'unit': unit, 'gstn': gstn, 'legal name': legal_name, 'trade name': trade_name, 'email': email, 'mobile': mobile, 'address': address })
print(df)
#df.to_excel('Filer_Data.xlsx', index=False)
df.to_excel('Non_Filer_Data.xlsx', index=False)
    
   
    
    





# dropdown = Select(determination_of_tax)
# dropdown.select_by_visible_text('For GSTR-09 Filers')
# dropdown.select_by_visible_text('Spain')


# # locate a button
# all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
# # click on a button
# all_matches_button.click()

# # using the "box" section as a reference to help us locate an element inside
# box = driver.find_element_by_class_name('panel-body')
# # select dropdown and select element inside by visible text
# dropdown = Select(box.find_element_by_id('country'))
# dropdown.select_by_visible_text('Spain')
# # implicit wait (useful in JavaScript driven websites when elements need seconds to load and avoid error "ElementNotVisibleException")
# time.sleep(5)
# # select elements in the table
# matches = driver.find_elements_by_css_selector('tr')

# # storage in a list
# all_matches = [match.text for match in matches]

# #quit drive we opened in the beginning
# driver.quit()

# # Bonus: Create Dataframe in Pandas and export to CSV (Excel)
# df = pd.DataFrame({'goals': all_matches})
# print(df)
# df.to_csv('tutorial.csv', index=False)