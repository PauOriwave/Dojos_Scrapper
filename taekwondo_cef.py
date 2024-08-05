from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

artes_marciales_data = {}

def configure_driver():
    chromium_options = Options()
    chromium_options.binary_location = "/usr/bin/chromium-browser"
    # chromium_options.add_argument("--headless")
    chromium_options.add_argument("--ignore-certicate-errors")
    chromium_options.add_argument("--ignore-ssl-error")
    chromium_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=chromium_options)
    return driver

def taekwondo_cef():
     global artes_marciales_data
     url = "http://barcelonacef.com/"
    