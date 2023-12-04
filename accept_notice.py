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
filers = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/ul/li[1]/a')
filers.click()
# non_filers = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/ul/li[2]/a')
# non_filers.click()
time.sleep(10)

# 236 ELEMENTS TO BE CLICKED 
i = 0
for i in range(225):

    clicked_radio_buttons = 0

    Note_file_button = driver.find_element(By.XPATH,'//*[@id="oicNonComplaintUI"]/tr[1]/td[7]/table/tbody/tr/td/input')
    Note_file_button.click()
    time.sleep(5)
    print("Tax Payer page entered")

    #Goes to next page 
     
    #Prints name of tax payer    
    name = driver.find_element(By.CSS_SELECTOR,"#maintable > div.contentMain > div.contentMainDiv > div:nth-child(30) > div.bs-example > div:nth-child(1) > div > div.row.basic-info > div:nth-child(1) > div" ).text
    print("Name of tax payer is ", name)

    #Total radio buttons check
    total_radio_buttons1 = driver.find_elements(By.CLASS_NAME,"custom-control-input.mainCheck")
    total_radio_buttons2 = driver.find_elements(By.CLASS_NAME,"custom-control-input.mainCheck1")
    radio_buttons_toclick = int(len(total_radio_buttons1) + len(total_radio_buttons2))/3
    print("RADIO BUTTONS TO CHECK FOR ", radio_buttons_toclick)

    #Radio button chosing
    z = driver.find_elements(By.ID,"itemActionId_1_1")
    lenght_z = len(z)
    y = driver.find_elements(By.ID,"itemActionId_2_1")
    lenght_y = len(y)

    a = driver.find_elements(By.ID,"itemActionId_3_1")
    lenght_a = len(a)

    p = driver.find_elements(By.ID,"itemActionId_4_1")
    lenght_p = len(p)
    q = driver.find_elements(By.ID,"itemActionId_5_1")
    lenght_q = len(q)

    b = driver.find_elements(By.ID,"itemActionId_6_1")
    lenght_b = len(b)

    s = driver.find_elements(By.ID,"itemActionId_7_1")
    lenght_s = len(s)
    t = driver.find_elements(By.ID,"itemActionId_8_1")
    lenght_t = len(t)

    c = driver.find_elements(By.ID,"itemActionId_9_1")
    lenght_c = len(c)
    d = driver.find_elements(By.ID,"itemActionId_10_1")
    lenght_d = len(d)

    e = driver.find_elements(By.ID,"itemActionId_11_1")
    lenght_e = len(e)

    f = driver.find_elements(By.ID,"itemActionId_12_1")
    lenght_f = len(f)

    g = driver.find_elements(By.ID,"itemActionId_13_1")
    lenght_g = len(g)
    #RADIO BUTTONS
    #!driver.findElements(By.id("...")).isEmpty()
    driver.find_elements()
    # if (driver.find_element(By.XPATH,'//*[@id="itemActionId_3_1"]').size() != 0):
    
    
    #Z 1
    if (lenght_z > 0):
        z_button = driver.find_element(By.XPATH,'//*[@id="itemActionId_1_1"]')
        driver.execute_script("arguments[0].scrollIntoView();",z_button )
        driver.execute_script("arguments[0].click();",z_button)
        print("Radio Z clicked")
        clicked_radio_buttons += 1
        print("Clicked radio buttons so far: ", clicked_radio_buttons)
        time.sleep(1)    
        # driver.find_element(By.XPATH,'//*[@id="itemActionId_3_1"]').click()

    # Y 2
    if (lenght_y > 0):
        y_button = driver.find_element(By.XPATH,'//*[@id="itemActionId_2_1"]')
        driver.execute_script("arguments[0].scrollIntoView();",y_button )
        driver.execute_script("arguments[0].click();",y_button)
        print("Radio Y clicked")
        clicked_radio_buttons += 1
        print("Clicked radio buttons so far: ", clicked_radio_buttons)
        time.sleep(1)    
        # driver.find_element(By.XPATH,'//*[@id="itemActionId_3_1"]').click()
    
    
    # A 3
    if (lenght_a > 0):
        a_button = driver.find_element(By.XPATH,'//*[@id="itemActionId_3_1"]')
        driver.execute_script("arguments[0].scrollIntoView();",a_button )
        driver.execute_script("arguments[0].click();",a_button)
        print("Radio A clicked")
        clicked_radio_buttons += 1
        print("Clicked radio buttons so far: ", clicked_radio_buttons)  
        time.sleep(1)  
        # driver.find_element(By.XPATH,'//*[@id="itemActionId_3_1"]').click()

    # P 4
    if (lenght_p > 0):
        p_button = driver.find_element(By.XPATH,'//*[@id="itemActionId_4_1"]')
        driver.execute_script("arguments[0].scrollIntoView();",p_button )
        driver.execute_script("arguments[0].click();",p_button)
        print("Radio P clicked")
        clicked_radio_buttons += 1
        print("Clicked radio buttons so far: ", clicked_radio_buttons)  
        time.sleep(1)  
        # driver.find_element(By.XPATH,'//*[@id="itemActionId_3_1"]').click()
    
    # Q 5
    if (lenght_q > 0):
        q_button = driver.find_element(By.XPATH,'//*[@id="itemActionId_5_1"]')
        driver.execute_script("arguments[0].scrollIntoView();",q_button )
        driver.execute_script("arguments[0].click();",q_button)
        print("Radio Q clicked")
        clicked_radio_buttons += 1
        print("Clicked radio buttons so far: ", clicked_radio_buttons)  
        time.sleep(1)  
        # driver.find_element(By.XPATH,'//*[@id="itemActionId_3_1"]').click()
    
    
    
    # B 6
    if (lenght_b > 0):
        b_button = driver.find_element(By.XPATH,'//*[@id="itemActionId_6_1"]')
        driver.execute_script("arguments[0].scrollIntoView();",b_button )
        driver.execute_script("arguments[0].click();",b_button)
        print("Radio B clicked")
        clicked_radio_buttons += 1
        print("Clicked radio buttons so far: ", clicked_radio_buttons)
        time.sleep(1)   
        # driver.find_element(By.XPATH,'//*[@id="itemActionId_6_1"]').click()

    # S 7
    if (lenght_s > 0):
        s_button = driver.find_element(By.XPATH,'//*[@id="itemActionId_7_1"]')
        driver.execute_script("arguments[0].scrollIntoView();",s_button )
        driver.execute_script("arguments[0].click();",s_button)
        print("Radio S clicked")
        clicked_radio_buttons += 1
        print("Clicked radio buttons so far: ", clicked_radio_buttons)
        time.sleep(1)
        # driver.find_element(By.XPATH,'//*[@id="itemActionId_9_1"]').click()

    # T 8
    if (lenght_t > 0):
        t_button = driver.find_element(By.XPATH,'//*[@id="itemActionId_8_1"]')
        driver.execute_script("arguments[0].scrollIntoView();",t_button )
        driver.execute_script("arguments[0].click();",t_button)
        print("Radio T clicked")
        clicked_radio_buttons += 1
        print("Clicked radio buttons so far: ", clicked_radio_buttons)
        time.sleep(1)
        # driver.find_element(By.XPATH,'//*[@id="itemActionId_9_1"]').click()
    
    # C 9
    if (lenght_c > 0):
        c_button = driver.find_element(By.XPATH,'//*[@id="itemActionId_9_1"]')
        driver.execute_script("arguments[0].scrollIntoView();",c_button )
        driver.execute_script("arguments[0].click();",c_button)
        print("Radio C clicked")
        clicked_radio_buttons += 1
        print("Clicked radio buttons so far: ", clicked_radio_buttons)
        time.sleep(1)
        # driver.find_element(By.XPATH,'//*[@id="itemActionId_9_1"]').click()
    
    # D 10
    if (lenght_d > 0):
        d_button = driver.find_element(By.XPATH,'//*[@id="itemActionId_10_1"]')
        driver.execute_script("arguments[0].scrollIntoView();",d_button )
        driver.execute_script("arguments[0].click();",d_button)
        print("Radio D clicked")
        clicked_radio_buttons += 1
        print("Clicked radio buttons so far: ", clicked_radio_buttons)
        time.sleep(1)
        # driver.find_element(By.XPATH,'//*[@id="itemActionId_10_1"]').click()

    # E 11
    if (lenght_e > 0):
        e_button = driver.find_element(By.XPATH,'//*[@id="itemActionId_11_1"]')
        driver.execute_script("arguments[0].scrollIntoView();",e_button )
        driver.execute_script("arguments[0].click();",e_button)
        print("Radio E clicked")
        clicked_radio_buttons += 1
        print("Clicked radio buttons so far: ", clicked_radio_buttons)
        time.sleep(1)
        # driver.find_element(By.XPATH,'//*[@id="itemActionId_11_1"]').click()
    
    # F 12
    if (lenght_f > 0):
        f_button = driver.find_element(By.XPATH,'//*[@id="itemActionId_12_1"]')
        driver.execute_script("arguments[0].scrollIntoView();",f_button )
        driver.execute_script("arguments[0].click();",f_button)
        print("Radio F clicked")
        clicked_radio_buttons += 1
        print("Clicked radio buttons so far: ", clicked_radio_buttons)
        time.sleep(1)
        # driver.find_element(By.XPATH,'//*[@id="itemActionId_12_1"]').click()
    
    # G 13
    if (lenght_g > 0):
        g_button = driver.find_element(By.XPATH,'//*[@id="itemActionId_13_1"]')
        driver.execute_script("arguments[0].scrollIntoView();",g_button )
        driver.execute_script("arguments[0].click();",g_button)
        print("Radio G clicked")
        clicked_radio_buttons += 1
        print("Clicked radio buttons so far: ", clicked_radio_buttons)
        time.sleep(1)
        # driver.find_element(By.XPATH,'//*[@id="itemActionId_12_1"]').click()
    
    print("All Radio buttons clicked")

    if (clicked_radio_buttons == radio_buttons_toclick):
        print( "Radio buttons CORRECTLY CLICKED")

        final_message = "Radio buttons clicked: " + str(clicked_radio_buttons) + "\n" + "Radio buttons to be clicked: " + str(radio_buttons_toclick) + "\n" + "Number of iterations: " + str(i)
        
        #Show pop up message
        w = tk.Tk()
        w.withdraw()
        w.after(1000, w.destroy) # Destroy the widget after 3 seconds
        if messagebox.showinfo("Radio button CORRECTLY CLICKED", final_message):
    
            w.destroy()
        
        print("Scroll to botton and click")
        elem = driver.find_element(By.TAG_NAME, "html")
        elem.send_keys(Keys.END)
        print("Srolled to bottom")
        
        #SUBMIT
        submit_button = driver.find_element(By.XPATH,'//*[@id="submit"]')
        driver.execute_script("arguments[0].scrollIntoView();",submit_button)
        driver.execute_script("arguments[0].click();",submit_button)    
        print("Submit button clicked")
        time.sleep(3)

        #YES CONFIRM
        yes_button = driver.find_element(By.XPATH,'//*[@id="confirm"]/a')
        driver.execute_script("arguments[0].scrollIntoView();",yes_button)
        driver.execute_script("arguments[0].click();",yes_button)    
        print("Yes button clicked")
        time.sleep(3)

        
        #OK BUTTON
        ok_button = driver.find_element(By.XPATH,'//*[@id="ok"]')
        driver.execute_script("arguments[0].scrollIntoView();",ok_button)
        driver.execute_script("arguments[0].click();",ok_button) 
        print("Ok button clicked")
        time.sleep(5)

        #BACK
        back_button = driver.find_element(By.XPATH,'//*[@id="backToList"]')
        driver.execute_script("arguments[0].scrollIntoView();",back_button)
        driver.execute_script("arguments[0].click();",back_button)    
        print("Back button clicked \n")
        time.sleep(5)

        print("CLICKED RADIO BUTTONS: ", clicked_radio_buttons)
        print("RADIO BUTTONS TO CLICK: ", radio_buttons_toclick)
        print("ITERATION DONE ", i)
        print("\n")
        #for page in range(1, loop_end):
    else:
        print("RADIO BUTTON MISMATCH")
        break
    
    # print("Scroll to botton and click")
    # elem = driver.find_element(By.TAG_NAME, "html")
    # elem.send_keys(Keys.END)
    # print("Srolled to bottom")
    
    # #SUBMIT
    # submit_button = driver.find_element(By.XPATH,'//*[@id="submit"]')
    # driver.execute_script("arguments[0].scrollIntoView();",submit_button)
    # driver.execute_script("arguments[0].click();",submit_button)    
    # print("Submit button clicked")
    # time.sleep(5)

    # #YES CONFIRM
    # yes_button = driver.find_element(By.XPATH,'//*[@id="confirm"]/a')
    # driver.execute_script("arguments[0].scrollIntoView();",yes_button)
    # driver.execute_script("arguments[0].click();",yes_button)    
    # print("Yes button clicked")
    # time.sleep(5)

    
    # #OK BUTTON
    # ok_button = driver.find_element(By.XPATH,'//*[@id="ok"]')
    # driver.execute_script("arguments[0].scrollIntoView();",ok_button)
    # driver.execute_script("arguments[0].click();",ok_button) 
    # print("Ok button clicked")
    # time.sleep(10)

    # #BACK
    # back_button = driver.find_element(By.XPATH,'//*[@id="backToList"]')
    # driver.execute_script("arguments[0].scrollIntoView();",back_button)
    # driver.execute_script("arguments[0].click();",back_button)    
    # print("Back button clicked")
    # time.sleep(10)

    # print("ITERATION DONE ", i)
    # #for page in range(1, loop_end):
   


