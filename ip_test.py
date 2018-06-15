"""
from selenium import webdriver
import urllib.request

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks", "127.0.0.1")
profile.set_preference("network.proxy.socks_port", 9050)
profile.update_preferences()
driver = webdriver.Firefox(executable_path="/Users/paramount/Downloads/geckodriver")
driver.get('http://icanhazip.com/')
print(driver.page_source)
driver.quit()
"""
import socks
import socket
#from urllib.request import urlopen
import urllib.request

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
req = urllib.request
d = req.urlopen("http://icanhazip.com")
d.read()
