from selenium import webdriver

driver = webdriver.Firefox()

driver.get('http://icanhazip.com/')

print(driver.page_source)

driver.quit()
