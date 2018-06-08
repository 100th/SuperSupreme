import sys
from SupremeBot import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BotAccount():
    def __init__(self):
        super().__init__()

    def test(self):
        driver = webdriver.PhantomJS('/Users/paramount/Downloads/phantomjs/bin/phantomjs')
        driver.get('https://www.google.co.kr/')

        assert 'Google' in driver.title

        input_element = driver.find_element_by_name('q')
        input_element.send_keys('Python')

        driver.save_screenshot('search_results.png')


if __name__ == "__main__":
    #app = QApplication(sys.argv)
    BotAccount = BotAccount()
    BotAccount.test()
