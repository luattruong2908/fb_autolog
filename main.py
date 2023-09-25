from selenium import webdriver
import random
import pickle
from time import sleep

waittime = random.uniform(3, 5)
driver = webdriver.Firefox()
driver.get('https://www.facebook.com')

sleep(waittime)

try:
    with open('cookies.pkl', 'rb') as file:
        cookies = pickle.load(file)
    for cookie in cookies:
        print(cookie)
        driver.add_cookie(cookie)

except:
   print("can't dump cookie")

sleep(waittime)

driver.get('https://www.facebook.com')

sleep(waittime)

driver.quit()
