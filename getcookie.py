from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import random
import os
import pickle
from time import sleep

load_dotenv()

waittime = random.uniform(3, 5)
driver = webdriver.Firefox()
driver.get('https://www.facebook.com')

driver.implicitly_wait(waittime)

username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")
email = driver.find_element(By.ID, 'email') 
pass_ = driver.find_element(By.ID, 'pass')
email.send_keys(username)
pass_.send_keys(password)

driver.implicitly_wait(waittime)

pass_.send_keys(Keys.ENTER)

sleep(waittime)

try:
    cookies = driver.get_cookies()
    print(cookies)
    print("Got cookies")
    with open('cookies.pkl', 'wb') as file:
        pickle.dump(cookies, file)
except Exception as e:
    print(e)

sleep(waittime)
driver.quit()

