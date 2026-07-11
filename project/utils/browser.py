from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def create_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    
    service = Service('/usr/local/bin/chromedriver')

    return webdriver.Chrome(service=service, options=options)