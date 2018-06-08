from selenium import webdriver

#driver = webdriver.Chrome('/Users/paramount/Downloads/chromedriver')
driver = webdriver.PhantomJS('/Users/paramount/Downloads/phantomjs/bin/phantomjs')

driver.get('http://icanhazip.com/')

print(driver.page_source)

driver.quit()
