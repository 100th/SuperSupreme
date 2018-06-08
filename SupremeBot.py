from selenium import webdriver

service_args = [ '--proxy=localhost:9150', '--proxy-type=socks5', ]
driver = webdriver.PhantomJS(executable_path='/Users/paramount/Downloads/phantomjs/bin/phantomjs', service_args=service_args)

driver.get('https://www.supremenewyork.com/shop')

driver.save_screenshot('search_results.png')
