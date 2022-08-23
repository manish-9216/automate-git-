import imp
import selenium
import random
import os
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import os.path
import random
import urllib
from selenium.webdriver.common.keys import Keys
import sys
import requests
from fake_useragent import UserAgent




# headerless chrome +
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('start-maximized')
# # passing useragent to webdriver

ua = UserAgent(cache=False)
userAgent = ua.random
chrome_options.add_argument(f'user-agent={userAgent}')
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()


def login():
    driver.get('https://signup.live.com/')
    """ for username """
    userID = driver.find_element_by_xpath("//*[@id='app-mount']/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input").send_keys('manish.paragroot@gmail.com')
    """ for password """
    user_password = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys('mannu_9216')
    """enter in login button """
    login = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]').click()

login()

def Invitation():
    """invitation accept """
    driver.get('https://discord.com/invite/96QBSE4j59')
    time.sleep(5)
    # send keys 
    driver.find_element_by_name('username').send_keys('mannu')
    # login button 
    
    # invitation_login = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div[2]/div[2]/button').click()
    elements = driver.find_elements_by_class_name("contents-3ca1mk")[0].click()
    time.sleep(3)
    
    u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=hcaptcha&sitekey={data_sitekey}&pageurl={page_url}&json=1&invisible=1"
    r1 = requests.get(u1)
    print(r1.json())
    time.sleep(10)
    rid = r1.json().get("request")
    u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
    time.sleep(5)
    while True:
        r2 = requests.get(u2)
        print(r2.json())
        if r2.json().get("status") == 1:
            form_tokon = r2.json().get("request")
            break
        time.sleep(5)

    # //textarea[@name="h-captcha-response"]
    driver.execute_script(f'document.getElementsByName("g-recaptcha-response")[0].innerText="{form_tokon}";') 
    # put captcha token into g-recaptcha-response textarea
    driver.execute_script(f'document.getElementsByName("h-captcha-response")[0].innerText="{form_tokon}";')
    
    
    iframe = driver.find_element_by_xpath("//iframe[@title='Main content of the hCaptcha challenge']")
    driver.switch_to.frame(iframe)
    time.sleep(3)
    
    print(driver.page_source)
    # switching iframes 
    # iframe = driver.find_element_by_xpath("//iframe[@title='Main content of the hCaptcha challenge']")
    # driver.switch_to.frame(iframe)
    
    # print(driver.page_source)
    driver.delete_all_cookies()  


    try:
        
        driver.find_element_by_xpath("//div[@class='button-submit button']").click()
    except Exception as e:
        print("errrr",e)
        driver.find_element_by_xpath("//div[@title='Submit Answers']").click()


    time.sleep(500)

    

Invitation()


