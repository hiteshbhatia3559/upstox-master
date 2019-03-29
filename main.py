api_key = {"ak":"sW8QnFzjKO3tmY2LTehyg5sztKCTPmN6fzymZKVh","aks":"97h1eqpunb","oauth":"80a243368dfdc90579ad0bcef9bc8705b5fca013","username":"164598","password":"Sanket@123","doy":"1991"}
from upstox_api.api import *
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, Chrome
from webdriver_manager.chrome import ChromeDriverManager
import socket

# This automates the process of getting access token
def openurl_function(api_key):
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('https://api.upstox.com/index/dialog/authorize?apiKey=sW8QnFzjKO3tmY2LTehyg5sztKCTPmN6fzymZKVh&redirect_uri=http://127.0.0.1&response_type=code')
    driver.find_element_by_id("name").send_keys(api_key["username"])
    driver.find_element_by_id("password").send_keys(api_key["password"])
    driver.find_element_by_id("password2fa").send_keys(api_key["doy"])
    driver.find_element_by_id("password2fa").submit()
    driver.find_element_by_id("allow").submit()
    url=driver.current_url
    code=url.split("=")
    driver.quit()
    print(code[1])
    return code[1]

def event_handler_quote_update(message):
    print("Quote Update: %s" % str(message))

def get_data()

s = Session(api_key["ak"])
s.set_redirect_uri ('http://127.0.0.1')
s.set_api_secret(api_key["aks"])
s.set_code(openurl_function(api_key))
access_token = s.retrieve_access_token()

u = Upstox(api_key["ak"],access_token)
u.set_on_quote_update(event_handler_quote_update)
u.get_master_contract('NSE_EQ')
tata = u.get_instrument_by_symbol('NSE_EQ', 'TATACHEM')
b = u.get_live_feed(u.get_instrument_by_symbol('NSE_EQ', 'TATACHEM'), LiveFeedType.Full)
print(b)
