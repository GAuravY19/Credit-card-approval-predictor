import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)

os.environ['PATH'] = r'D:/WebScrapping/WebDrivers/'

DRIVER = webdriver.Chrome(options=options)

DRIVER.get('https://www.goibibo.com/')

DRIVER.maximize_window()

try:
    dialogCross = DRIVER.find_element('xpath', '//div//span[@class = "logSprite icClose"]')

    dialogCross.click()

except:
    print("Error aagaya")
