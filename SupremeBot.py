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

class GetSupreme(QMainWindow, form_class):
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
            #website = webdriver.Chrome(executable_path='/Users/paramount/Downloads/chromedriver', service_args=service_args)

    # Search 버튼 클릭
    def search(self):
        category = self.comboBox.currentText()
        keyword = self.lineEdit_13.text()
        color = self.lineEdit_14.text()
        size = self.lineEdit_15.text()

        #website = webdriver.PhantomJS('/Users/paramount/Downloads/phantomjs/bin/phantomjs')
        #website = webdriver.Chrome('/Users/paramount/Downloads/chromedriver')
        url = "http://www.supremenewyork.com/shop/all/" + category
        site = website.get(url)
        website.get(url)

        assert 'Supreme' in website.title

        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')

        for div in soup.find_all('div', { "class" : "inner-article" }):
            p_keyword = ""
            p_color = ""
            link = ""
            print("test")
            for a in div.find_all('a', href=True, text=True):
                link = a['href']
                print("link")                                 #체크해보려고
            for a in div.find_all(['h1','p']):
                if(a.name=='h1'):
                    p_keyword = a.text
                    print("find 1")
                elif(a.name=='p'):
                    p_color = a.text
                    print("find 2")
                else:
                    print("nothing")

            website.save_screenshot('soup_result.png')

            if(keyword in p_keyword and color == p_color):
                website.visit(link)
            	#website.find_option_by_text(size).first.click()
#               choose_a_size = Select(website.find_element_by_id('size'))
#            	choose_a_size.select_by_visible_text(self.size)
#               if (size == ""):
#                    QMessageBox.about(self, "Error Message", "Sorry. This size is not available.")
#            	website.find_by_name('commit').click()    #아니면 find_element_by_name
        website.save_screenshot('searck_result2.png')

    # Check 버튼 클릭
    def check(self):
        website = webdriver.PhantomJS('/Users/paramount/Downloads/phantomjs/bin/phantomjs')
        website.get('http://www.supremenewyork.com/checkout')

        assert 'Supreme' in website.title

        name = self.lineEdit.text()
        email = self.lineEdit_2.text()
        tel = self.lineEdit_3.text()
        address = self.lineEdit_4.text()
        city = self.lineEdit_5.text()
        zip = self.lineEdit_6.text()
        country = self.lineEdit_7.text()
        type = self.lineEdit_8.text()
        number = self.lineEdit_9.text()
        month = self.lineEdit_10.text()
        year = self.lineEdit_11.text()
        cvc = self.lineEdit_12.text()

        element = website.find_element_by_name("order[billing_name]")
        element.send_keys(name)

        element = website.find_element_by_name("order[email]")
        element.send_keys(email)

        element = website.find_element_by_name("order[tel]")
        element.send_keys(tel)

        element = website.find_element_by_name("order[billing_address]")
        element.send_keys(address)

        element = website.find_element_by_name("order[billing_city]")
        element.send_keys(city)

        element = website.find_element_by_name("order[billing_zip]")
        element.send_keys(zip)

        element = Select(website.find_element_by_name("order[billing_country]"))
        element.select_by_visible_text(country)

        element = Select(website.find_element_by_name("credit_card[type]"))
        element.select_by_visible_text(type)

        element = website.find_element_by_name("credit_card[cnb]")
        element.send_keys(number)

        element = Select(website.find_element_by_name("credit_card[month]"))
        element.select_by_visible_text(month)

        element = Select(website.find_element_by_name("credit_card[year]"))
        element.select_by_visible_text(year)

        element = website.find_element_by_name("credit_card[vval]")
        element.send_keys(cvc)

        website.find_element_by_class_name("terms").click()

        website.save_screenshot('check_screenshot.png')

        # if 써서?
        QMessageBox.about(self, "Success Message", "Congratulation. We bought it successfully.")

        website.save_screenshot('check_result.png')

    # 원 샷 버튼 클릭
    def one_shot(self):
        self.search()
        sleep(1)                # if 문 써서?
        self.check()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GetSupreme = GetSupreme()
    GetSupreme.show()
    app.exec_()
#    if (search(self) == False):
#        QMessageBox.about(self, "Error Message", "Sorry. We can't find this item on website.")

"""
버려진 함수
self.lineEdit.textChanged.connect(self.account_changed)
def account_changed(self, info):
    self.info = self.lineEdit.text()
"""
