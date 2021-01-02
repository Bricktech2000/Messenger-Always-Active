#https://unix.stackexchange.com/questions/9107/how-can-i-run-firefox-on-linux-headlessly-i-e-without-requiring-libgtk-x11-2-0
#to use without a display: sudo apt install xvfb
#then: xvfb-run -a python3 run.py <MessengerID> [Browser]

#https://askubuntu.com/questions/661186/how-to-install-previous-firefox-version
#sudo apt-get install firefox=75.0+build3-0ubuntu1

#download chrome webdriver from:
#sites.google.com/a/chromium.org/chromedriver/home

import os
import sys
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

LOAD_DELAY = 2 #the delay in seconds to load a webpage
REFRESH_DELAY = 10 #the delay in seconds between each page refesh
MESSENGER_LOGIN = 'https://messenger.com/login/' #the login url
MESSENGER_REDIRECT = 'https://www.messenger.com/t/' #the redirection url
USER_SELECTOR = '#email' #the username input box selector
PASS_SELECTOR = '#email' #the password input box selector
SUBMIT_SELECTOR = '#loginbutton' #the submit button selector


if len(sys.argv) != 4:
    print('Error: Usage: run.py <username> <password> <chatID>')
    exit(1)
username = sys.argv[1]
password = sys.argv[2]
id = sys.argv[3]

#https://chromedriver.chromium.org/getting-started
driver = webdriver.Chrome()
driver.get(MESSENGER_LOGIN)
time.sleep(LOAD_DELAY)

usernameInput = driver.find_element_by_css_selector(USER_SELECTOR)
passwordInput = driver.find_element_by_css_selector(PASS_SELECTOR)
submitButton = driver.find_element_by_css_selector(SUBMIT_SELECTOR)
#https://stackoverflow.com/questions/38521136/python-selenium-attributeerror-webelement-object-has-no-attribute-sendkeys
usernameInput.send_keys(username)
passwordInput.send_keys(password)
submitButton.click()
time.sleep(LOAD_DELAY)

driver.get(MESSENGER_REDIRECT + id)

try:
    while True:
        driver.refresh()
        time.sleep(REFRESH_DELAY)
except KeyboardInterrupt:
    driver.quit()
    raise
