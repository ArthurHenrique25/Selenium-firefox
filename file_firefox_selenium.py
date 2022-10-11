## import base ###

from selenium import webdriver
from selenium .webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


profile = webdriver.FirefoxProfile("C:\\#######\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\qu6b6wn1.default-release")
profile.set_preference("browser.link.open_newwindow", 1)

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),firefox_profile=profile)

driver.get("https://www.google.com")

