from selenium import webdriver
import urllib.request
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks", "127.0.0.1")
profile.set_preference("network.proxy.socks_port", 9050)
profile.update_preferences()
driver = webdriver.Firefox(executable_path="/Users/paramount/Downloads/geckodriver")
driver.get('http://icanhazip.com/')
print(driver.page_source)
driver.quit()
