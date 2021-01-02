#https://unix.stackexchange.com/questions/9107/how-can-i-run-firefox-on-linux-headlessly-i-e-without-requiring-libgtk-x11-2-0
#to use without a display: sudo apt install xvfb
#then: xvfb-run -a python3 run.py ...

#download chrome webdriver from:
#sites.google.com/a/chromium.org/chromedriver/home

#for linux:
#sudo apt-get install unzip
#wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip
#unzip chromedriver_linux64.zip
#rm chromedriver_linux64.zip
#https://itsfoss.com/install-chrome-ubuntu/
#wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#sudo dpkg -i google-chrome-stable_current_amd64.deb
#rm google-chrome-stable_current_amd64.deb
#https://stackoverflow.com/questions/22558077/unknown-error-chrome-failed-to-start-exited-abnormally-driver-info-chromedri
#Xvfb :99 -ac -screen 0 1280x1024x24 &
#export DISPLAY=:99

#for windows:
#I hate windows CMD just download and unzip manually

import os
import sys
import time
import ctypes
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

LOAD_DELAY = 4 #the delay in seconds to load a webpage
REFRESH_DELAY = 60 #the delay in seconds between each page refesh
MESSENGER_LOGIN = 'https://messenger.com/login/' #the login url
MESSENGER_REDIRECT = 'https://www.messenger.com/t/' #the redirection url
USER_SELECTOR = '#email' #the username input box selector
PASS_SELECTOR = '#pass' #the password input box selector
SUBMIT_SELECTOR = '#loginbutton' #the submit button selector
WRONG_PASS_ELEMENT = '#login_form > div._3403._3404' #the HTML element that appears when a wrong password is submitted


if len(sys.argv) != 4:
    print('Error: Usage: run.py <username> <password> <chatID>')
    exit(1)
username = sys.argv[1]
password = sys.argv[2]
id = sys.argv[3]

#https://stackoverflow.com/questions/63741649/chrome-crashes-when-running-selenium-python3-script-as-sudo
#https://stackoverflow.com/questions/1026431/cross-platform-way-to-check-admin-rights-in-a-python-script-under-windows
try:
 is_admin = os.getuid() == 0
except AttributeError:
 is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

if is_admin:
    print('Error: Chrome Webdriver will crash if this program is run as root.')
    exit(0)

print('Username: ' + username)
print('Password: ' + password)

print('Booting Chrome Driver...')
#https://chromedriver.chromium.org/getting-started
driver = webdriver.Chrome('./chromedriver.exe')
driver.get(MESSENGER_LOGIN)
time.sleep(LOAD_DELAY)

print('Logging in...')
usernameInput = driver.find_element_by_css_selector(USER_SELECTOR)
passwordInput = driver.find_element_by_css_selector(PASS_SELECTOR)
submitButton = driver.find_element_by_css_selector(SUBMIT_SELECTOR)
#https://stackoverflow.com/questions/38521136/python-selenium-attributeerror-webelement-object-has-no-attribute-sendkeys
usernameInput.send_keys(username)
passwordInput.send_keys(password)
submitButton.click()
time.sleep(LOAD_DELAY)

try:
    error = driver.find_element_by_css_selector(WRONG_PASS_ELEMENT)
    print('Login Error: ' + error.get_attribute('innerText'))
    exit(0)
except NoSuchElementException:
    pass

driver.get(MESSENGER_REDIRECT + id)

print('Bot Running.')

while True:
    driver.refresh()
    time.sleep(REFRESH_DELAY)
