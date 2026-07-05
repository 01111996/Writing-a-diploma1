from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

def create_driver():
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--start-maximized')
    
    driver_path = "/usr/bin/chromedriver"
    
    if not os.path.exists(driver_path):
        raise FileNotFoundError(f"ChromeDriver not found at {driver_path}. Check the installation step in test.yml.")
        
    service = Service(executable_path=driver_path)
    return webdriver.Chrome(service=service, options=options)