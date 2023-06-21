import time                                             # needed for the sleep function
from bs4 import BeautifulSoup                           # used to parse the HTML
from selenium import webdriver                          # used to render the web page
from selenium.webdriver.chrome.service import Service   # Service is only needed for ChromeDriverManager

import functools                                        # used to create a print function that flushes the buffer
flushprint = functools.partial(print, flush=True)       # create a print function that flushes the buffer immediately

def asyncGetWeather(url):
        
        #change '/usr/local/bin/chromedriver' to the path of your chromedriver executable
        service = Service(executable_path='C:/webdrivers/chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        
        driver = webdriver.Chrome(service=service,options=options)  # run ChromeDriver
        flushprint("Getting page...")
        driver.get(url)                                             # load the web page from the URL
        flushprint("waiting 3 seconds for dynamic data to load...")
        time.sleep(3)                                               # wait for the web page to load
        flushprint("Done ... returning page source HTML")
        render = driver.page_source                                 # get the page source HTML
        driver.quit()                                               # quit ChromeDriver
        return render                                               # return the page source HTML