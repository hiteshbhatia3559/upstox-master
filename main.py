api_key = {"ak": "sW8QnFzjKO3tmY2LTehyg5sztKCTPmN6fzymZKVh", "aks": "97h1eqpunb",
           "oauth": "80a243368dfdc90579ad0bcef9bc8705b5fca013", "username": "164598", "password": "Sanket@123",
           "doy": "1991"}
from upstox_api.api import *
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, Chrome
from webdriver_manager.chrome import ChromeDriverManager
import socket
import csv
import multiprocessing


# This automates the process of getting access token
def openurl_function(api_key):
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get(
        'https://api.upstox.com/index/dialog/authorize?apiKey=sW8QnFzjKO3tmY2LTehyg5sztKCTPmN6fzymZKVh&redirect_uri=http://127.0.0.1&response_type=code')
    driver.find_element_by_id("name").send_keys(api_key["username"])
    driver.find_element_by_id("password").send_keys(api_key["password"])
    driver.find_element_by_id("password2fa").send_keys(api_key["doy"])
    driver.find_element_by_id("password2fa").submit()
    driver.find_element_by_id("allow").submit()
    url = driver.current_url
    code = url.split("=")
    driver.quit()
    print(code[1])
    return code[1]


def write_csv(u, instrument):
    stamp = 0
    u.get_master_contract('NSE_EQ')
    while 1:
        try:
            live_feed = u.get_live_feed(u.get_instrument_by_symbol('NSE_EQ', instrument), LiveFeedType.Full)
            if stamp == 0:
                stamp = live_feed['timestamp']
                with open(instrument + '.csv', 'wb+') as output:
                    writer = csv.writer(output)
                    writer.writerow(live_feed)
                    writer.writerow(live_feed.values())
            else:
                if stamp != live_feed['timestamp']:
                    stamp = live_feed['timestamp']
                    with open(instrument + '.csv', 'wb+') as output:
                        writer = csv.writer(output)
                        writer.writerow(live_feed)
                        writer.writerow(live_feed.values())
                else:
                    print("Timeout on "+instrument)
        except:
            pass

if __name__ == "__main__":
    list_of_instruments = ["TATACHEM", "YESBANK"] # ONLY EDIT THIS, SIMPLY ADD NAMES OF STOCKS YOU WANT TO TRACK
    s = Session(api_key["ak"])
    s.set_redirect_uri('http://127.0.0.1')
    s.set_api_secret(api_key["aks"])
    s.set_code(openurl_function(api_key))
    access_token = s.retrieve_access_token()

    u = Upstox(api_key["ak"], access_token)
    jobs = []
    for instrument in list_of_instruments:
        p = multiprocessing.Process(target=write_csv, args=(u, instrument,))
        jobs.append(p)
        p.start()
