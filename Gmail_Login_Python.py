from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("disable-infobars")

# create a new Chrome session
driver = webdriver.Chrome(executable_path=r"Set path for chromedriver.exe",options=chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()

# navigate to gmail
driver.get("https://mail.google.com/")

#get the username textbox
login_field = driver.find_element_by_name("identifier")
login_field.clear()

#enter username
login_field.send_keys("Enter your mail ID")
login_field.send_keys(u'\ue007') #unicode for enter key
time.sleep(2)

#get the password textbox
password_field = driver.find_element_by_name("password")
password_field.clear()

#enter password
password_field.send_keys("Enter your password here")
password_field.send_keys(u'\ue007') #unicode for enter key
time.sleep(10)
