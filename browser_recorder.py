from selenium import webdriver
import time

#GLOBALS
DASH_URL= "file:///Users/michael/dash/index.html"
WAIT_TIME = 10

#Create browser object, set kind to google chrome
browser = webdriver.Chrome()

#Open to DASH
browser.get(DASH_URL)

#Wait number of seconds of WAIT_TIME
time.sleep(WAIT_TIME)

#Close browser session
browser.close()
