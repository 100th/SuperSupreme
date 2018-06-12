import sys
from selenium import webdriver
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from time import sleep
from selenium.webdriver.common.keys import Keys
import datetime
import requests
from bs4 import BeautifulSoup

form_class = uic.loadUiType("SuperSupreme.ui")[0]

class QtDesigner(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.checkBox.clicked.connect(self.bypass_ip)

        self.pushButton.clicked.connect(self.check)
        self.pushButton_2.clicked.connect(self.search)
        self.pushButton_3.clicked.connect(self.one_shot)

    # 현재 시간 표시
    def timeout(self):
        current_time = QTime.currentTime()
        text_time = current_time.toString("hh:mm:ss")
        time_msg = "Current Time : " + text_time
        self.statusbar.showMessage(time_msg)

    # IP 우회 접속 체크 박스
    def bypass_ip(self):
        if self.checkBox.isChecked():
            service_args = [ '--proxy=localhost:9150', '--proxy-type=socks5', ]
            website = webdriver.PhantomJS(executable_path='/Users/paramount/Downloads/phantomjs/bin/phantomjs', service_args=service_args)
            #website.get('https://www.supremenewyork.com/shop')
            #website.save_screenshot('search_results.png')


    # 찾고자 하는 물품 키워드 검색
#    def SearchKeyword(keyword, texts):
#        for i in keyword:
#            if i not in texts:
#                return False
#        return True

#    	pageRequest = requests.get(category_url)
#    	soup = BeautifulSoup(pageRequest.content, "html.parser")
#    	links = soup.select("div.turbolink_scroller a")
#    	select_item = soup.select("div.inner-article h1 a.name-link")

#		pageRequest2 = requests.get('http://www.supremenewyork.com' + url)
#		soup2 = BeautifulSoup(pageRequest2.content, "html.parser")
#		itemName = soup2.find_all(itemprop="name")
#		itemColour = soup2.find_all(class_="style")
#		list1.append(itemName[0].text + ' ' + itemColour[0].text)
#		nameOfProduct = (itemName[0].text)
#		colourOfProduct = (itemColour[0].text)
#		dictionary[nameOfProduct + ' ' + colourOfProduct] = url

    # Search 버튼 클릭
    def search(self, link):
        category = self.comboBox.currentText()
        keyword = self.lineEdit_13.text()
        color = self.lineEdit_14.text()
        size = self.lineEdit_15.text()

        website = webdriver.PhantomJS('/Users/paramount/Downloads/phantomjs/bin/phantomjs')
        #website = webdriver.Chrome('/Users/paramount/Downloads/chromedriver')
        website.get("http://www.supremenewyork.com/shop/all/" + category)


#       select_item = soup.select("div.inner-article h1 a.name-link")
        soup = BeautifulSoup(html, 'lxml')
        select_item1 = soup.find_all("div", {"class": "inner-article"})
        select_item2 = select_item1.find_all('h1')
        if keyword in select_item2:
            select_item3 = selectitem1.find_all('p')
            if color in select_item3:
                select_item3.click()


        website.save_screenshot('search_results.png')

        #assert 'Supreme' in website.title

#        link = website.find_elements_by_class_name('name-link')
#        print(link)
#        link.click()

#        i = 0
#        while i < len(link):
#            if (SearchKeyword(color, link[i].text)):
#                print("Color : " + link[i].text)
#                link[i].click()
#                print("[+] Article found")
#               return True
#            i += 2
#        print("[-] Article not found")
#        return False


#       choose_a_size = Select(website.find_element_by_id('size'))
#    	choose_a_size.select_by_visible_text(self.size)
#       sleep(0.5)
        if (size == ""):
            QMessageBox.about(self, "Error Message", "Sorry. This size is not available.")

#    	add_to_basket = website.find_element_by_name("commit")
#    	add_to_basket.click()
#    	sleep(0.5)

#    	checkout = website.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/a[2]')
#    	checkout.click()
#    	sleep(0.5)


#    # Search 버튼 클릭
#    def search(self):
#        category = self.comboBox.currentText()
#        keyword = self.lineEdit_13.text()
#        color = self.lineEdit_14.text()
#        size = self.lineEdit_15.text()
#
#        if(keyword == ""):
#            QMessageBox.about(self, "Error Message", "Sorry. This  is sold out.")
#        else:
#            print(keyword)
#
#        print(category)
#        print(color)
#        print(size)


    # Check 버튼 클릭
    def check(self):
#        website = webdriver.PhantomJS('/Users/paramount/Downloads/phantomjs/bin/phantomjs')
#        website.get('https://okky.kr/user/register')

#        assert 'OKKY' in website.title

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        email = self.lineEdit_3.text()
        fullname = self.lineEdit_4.text()

        input_element = website.find_element_by_name('username')
        input_element.send_keys(username)

        input_element = website.find_element_by_name('password')
        input_element.send_keys(password)

        input_element = website.find_element_by_name('person.email')
        input_element.send_keys(email)

        input_element = website.find_element_by_name('person.fullName')
        input_element.send_keys(fullname)

        website.save_screenshot('search_results.png')

    # 원 샷 버튼 클릭
    def one_shot(self):
        self.search()
        sleep(1)
        self.check()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtDesigner = QtDesigner()
    QtDesigner.show()
    app.exec_()
