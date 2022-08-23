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


driver.get('https://signup.live.com/')
time.sleep(3)


driver.find_element_by_xpath('//*[@id="liveSwitch"]').click()

driver.find_element_by_xpath('//*[@id="MemberName"]').send_keys('mukhtar360rr')

driver.find_element_by_xpath('//*[@id="iSignupAction"]').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="PasswordInput"]').send_keys('mannu_8311')

driver.find_element_by_xpath('//*[@id="iSignupAction"]').click()

time.sleep(5)

driver.find_element_by_xpath('//*[@id="FirstName"]').send_keys('rishab')

driver.find_element_by_xpath('//*[@id="LastName"]').send_keys('sharma')

driver.find_element_by_xpath('//*[@id="iSignupAction"]').click()

time.sleep(5)

driver.find_element_by_xpath('//*[@id="Country"]').send_keys('Iceland')

driver.find_element_by_xpath('//*[@id="BirthMonth"]').send_keys('November')

driver.find_element_by_xpath('//*[@id="BirthDay"]').send_keys('12')

driver.find_element_by_xpath('//*[@id="BirthYear"]').send_keys('1996')

driver.find_element_by_xpath('//*[@id="iSignupAction"]').click()

time.sleep(10)


iframe = driver.find_element_by_xpath("//iframe[@id='enforcementFrame']")
driver.switch_to.frame(iframe)


iframe = driver.find_element_by_xpath("//iframe[@id='fc-iframe-wrap']")
driver.switch_to.frame(iframe)


# print(driver.page_source)

time.sleep(5)


try:
    driver.find_element_by_xpath("//span[@class='fc_meta_audio_btn']").click()
except:
    driver.find_element_by_xpath("/html/body/div[5]/span/a[2]/span").click()

time.sleep(50)