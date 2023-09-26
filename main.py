from selenium import webdriver
import random
import pickle
from time import sleep

waittime = random.uniform(3, 5)
driver = webdriver.Firefox() #use firefox
driver.get('https://www.facebook.com')

sleep(waittime)

#use cookies file collecting by getcookie.py
try:
    with open('cookies.pkl', 'rb') as file:
        cookies = pickle.load(file)
    for cookie in cookies:
        print(cookie)
        driver.add_cookie(cookie)
except:
   print("can't dump cookie")
   
# use cookies you copy by hand
# try:
#     driver.add_cookie({"name": name, "value": value})
# except:
#     print("can't dump cookie")

sleep(waittime)

driver.get('https://www.facebook.com')

sleep(waittime)

driver.quit()
