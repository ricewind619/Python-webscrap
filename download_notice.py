import tkinter as tk
# import tkinter
from tkinter import messagebox
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


# define 'driver' variable
# driver = webdriver.Chrome(Path)
# open Google Chrome with chromedriver
driver.get(website)

time.sleep(15)

# CODE BLOCK TO LOG IN

driver.find_element(By.XPATH, '//*[@id="uid"]').send_keys('papori')
driver.find_element(By.XPATH, '//*[@id="pswrd"]').send_keys('pn@2023')
driver.find_element(By.XPATH, '//*[@id="login"]').click()

time.sleep(15)

# FILER AND NON FILER CHOOSING


# # select dropdown and select element inside by visible text
determination_of_tax = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a')
determination_of_tax.click()
filers = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/ul/li[1]/a')


filers.click()
# non_filers = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/ul/li[2]/a')
# non_filers.click()
time.sleep(10)

#Set 200 in options 
page = driver.find_element(By.XPATH, '//*[@id="pageCombo"]')
dropdown = Select(page)
dropdown.select_by_value("200")
option_200 = driver.find_element(By.XPATH, '//*[@id="pageCombo"]/option[13]')
option_200.click()
time.sleep(5)

#Go to second page 
print("Scroll to botton and click")
elem = driver.find_element(By.TAG_NAME, "html")
elem.send_keys(Keys.END)
print("Srolled to bottom")
next_page_button = driver.find_element(By.CSS_SELECTOR,"#pagination > div.pageRight > div.pageNav > span.lnk.right")
print("Next page button found")
driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
driver.execute_script("arguments[0].click();",next_page_button)
print("NEXT PAGE BUTTON CLICKED")
time.sleep(5)

#Go to third page 
print("Scroll to botton and click")
elem = driver.find_element(By.TAG_NAME, "html")
elem.send_keys(Keys.END)
print("Srolled to bottom")
next_page_button = driver.find_element(By.CSS_SELECTOR,"#pagination > div.pageRight > div.pageNav > span.lnk.right")
print("Next page button found")
driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
driver.execute_script("arguments[0].click();",next_page_button)
print("NEXT PAGE BUTTON CLICKED")
time.sleep(5)

gstn = []
legal_name = []

#LOOP STARTS
# from 229 ROW TO BE CLICKED
# from 1 to 67 i.e. 401 to 467
i = 1
for i in range(1,67):

    print("Scroll to top")
    elem = driver.find_element(By.TAG_NAME, "html")
    elem.send_keys(Keys.HOME)
    # elem.send_keys(Keys.PAGE_DOWN)
    # elem.send_keys(Keys.PAGE_DOWN)
    # elem.send_keys(Keys.PAGE_DOWN)
    # elem.send_keys(Keys.PAGE_DOWN)
    # elem.send_keys(Keys.PAGE_DOWN)
    # elem.send_keys(Keys.PAGE_DOWN)
    # elem.send_keys(Keys.PAGE_DOWN)
    print("Srolled to middle")

    
    # Note_file_button = driver.find_element(By.XPATH,'//*[@id="oicNonComplaintUI"]/tr[1]/td[7]/table/tbody/tr/td/input')
    # Note_file_button.click()
    i_string = str(i)
    
    current_legal_name = driver.find_elements(By.XPATH, f'//*[@id="oicNonComplaintUI"]/tr[{i_string}]/td[3]/span[2]')
    for e in current_legal_name:
        print(e.text)
        legal_name.append(e.text)

    current_gstn = driver.find_elements(By.XPATH, f'//*[@id="oicNonComplaintUI"]/tr[{i_string}]/td[3]/span[1]')
    for e in current_gstn:
        print(e.text)
        gstn.append(e.text)

    #download_file_button = driver.find_element(By.XPATH,f'//*[@id="oicNonComplaintUI"]/tr[{i_string}]/td[7]/table/tbody/tr/td/input')
    download_file_button = driver.find_element(By.XPATH,f'//*[@id="oicNonComplaintUI"]/tr[{i_string}]/td[7]/table/tbody/tr[2]/td/div/input')

    print("Download button exists")
    driver.execute_script("arguments[0].scrollIntoView();",download_file_button )
    driver.execute_script("arguments[0].click();",download_file_button)
    print("Download button clicked")
    time.sleep(3)
    #XPATH of Download button = /html/body/div[4]/div[1]/div/div[3]/div[3]/div[7]/table/tbody/tr[28]/td[7]/table/tbody/tr[2]/td/div/input
    download_popup_button = driver.find_element(By.XPATH,'//*[@id="dwnldDrc01AnnxPdf"]')
    driver.execute_script("arguments[0].scrollIntoView();",download_popup_button )
    driver.execute_script("arguments[0].click();",download_popup_button)
    print("Download popup clicked") 
    #Xpath of Download PDF: //*[@id="dwnldDrc01AnnxPdf"]
    time.sleep(3)

    final_message = "Download complete and iteration number is " + str(i) + "\n"
    #Show pop up message
    w = tk.Tk()
    w.withdraw()
    w.after(1000, w.destroy) # Destroy the widget after 3 seconds
    if messagebox.showinfo("Radio button CORRECTLY CLICKED", final_message):

        w.destroy()

    i += 1

df = pd.DataFrame({'GSTN': gstn, 'Legal Name': legal_name })
print(df)
#df.to_excel('Filer_Data.xlsx', index=False)
df.to_excel('Filer_2017-18_Notices_Page_2.xlsx', index=False)
