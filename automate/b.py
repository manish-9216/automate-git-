from distutils.log import debug
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
import requests
from bs4 import BeautifulSoup

# install recapcha libraries
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import ffmpy
import urllib
import pydub

# for csv file 
import pandas as pd
import csv

import re

import random
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import sys
import time
import requests

audioToTextDelay = 10
delayTime = 2
audioFile = "\\payload.mp3"
URL = "https://etherscan.io/login"
SpeechToTextURL = "https://speech-to-text-demo.ng.bluemix.net/"

def delay():
    time.sleep(random.randint(2, 3))

def audioToText(audioFile):
    driver.execute_script('''window.open("","_blank")''')
    driver.switch_to.window(driver.window_handles[1])
    driver.get(SpeechToTextURL)

    delay()
    audioInput = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
    audioInput.send_keys(audioFile)

    time.sleep(audioToTextDelay)
    text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div/span')
    while text is None:
        text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div/span')
    result = text.text
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return result


try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    delay()
    # go to website which have recaptcha protection
    driver.get(URL)
    username = driver.find_element_by_id("ContentPlaceHolder1_txtUserName").send_keys("tapendra")
    password = driver.find_element_by_id("ContentPlaceHolder1_txtPassword").send_keys("12345678")

    soup = BeautifulSoup(driver.page_source,'html.parser')
except Exception as e:
    sys.exit(
        "[-] Please update the chromedriver.exe in the webdriver folder according to your chrome version:https://chromedriver.chromium.org/downloads")

g_recaptcha = driver.find_elements_by_class_name('g-recaptcha')[0]
outerIframe = g_recaptcha.find_element_by_tag_name('iframe')
outerIframe.click()

iframes = driver.find_elements_by_tag_name('iframe')
audioBtnFound = False
audioBtnIndex = -1
for index in range(len(iframes)):
    driver.switch_to.default_content()
    iframe = driver.find_elements_by_tag_name('iframe')[index]
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(delayTime)
    try:
        audioBtn = driver.find_element_by_id("recaptcha-audio-button")
        audioBtn.click()
        audioBtnFound = True
        audioBtnIndex = index
        break
    except Exception as e:
        pass
    
if audioBtnFound:
    try:
        while True:
            
            # get the mp3 audio file
            src = driver.find_element_by_id("audio-source").get_attribute("src")
            print("[INFO] Audio src: %s" % src)

            # download the mp3 audio file from the source
            urllib.request.urlretrieve(src, os.getcwd() + audioFile)

            # Speech To Text Conversion
            key = audioToText(os.getcwd() + audioFile)
            print("[INFO] Recaptcha Key: %s" % key)

            driver.switch_to.default_content()
            iframe = driver.find_elements_by_tag_name('iframe')[audioBtnIndex]
            driver.switch_to.frame(iframe)

            # key in results and submit
            inputField = driver.find_element_by_id("audio-response")
            inputField.send_keys(key)
            delay()
            inputField.send_keys(Keys.ENTER)
            delay()
            driver.switch_to.default_content()
            time.sleep(2)

            button = driver.find_element_by_xpath("/html/body/div[1]/main/div/form/div[8]/div[2]/input")
            driver.execute_script("arguments[0].click();", button)
            print("Login Button =>", button)
            
            err = driver.find_elements_by_class_name('rc-audiochallenge-error-message')[0]
            if err.text == "" or err.value_of_css_property('display') == 'none':
                print("[INFO] Success!")
                break
    except Exception as e:
        print(e)
        sys.exit("[INFO] Possibly blocked by google. Change IP,Use Proxy method for requests")
    # time.sleep(5)    
    # driver.switch_to.default_content()
    # login_button = driver.find_element_by_id("ContentPlaceHolder1_btnLogin").click()
else:
    sys.exit("[INFO] Audio Play Button not found! In Very rare cases!")


