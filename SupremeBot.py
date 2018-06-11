import sys
from selenium import webdriver
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from time import sleep
from selenium.webdriver.common.keys import Keys

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
            #website.get('https://www.supremenewyork.com/shop')
            #website.save_screenshot('search_results.png')

    """
    # 찾고자 하는 물품 키워드 검색
    def SearchKeyword(keywords, texts):
        for i in keywords:
            if i not in texts:
                return False
        return True
    """

    # Search 버튼 클릭
    def search(self):
        category = self.comboBox.currentText()
        keyword = self.lineEdit_13.text()
        color = self.lineEdit_14.text()
        size = self.lineEdit_15.text()

        website = webdriver.PhantomJS('/Users/paramount/Downloads/phantomjs/bin/phantomjs')
        website.get("http://www.supremenewyork.com/shop/all/" + category)

        assert 'Supreme' in website.title

        link = website.find_elements_by_class_name("name-link")
        """
        i = 0
        while i < len(link):
            if (SearchKeyword(keywords, link[i].text) & (color in link[i+1].text)):
                #print("Texts : " + link[i].text)
                #print("Color : " + link[i+1].text)
                link[i].click()
                return True
            i += 2
        return False
        """
    	choose_a_size = Select(website.find_element_by_id('size'))
    	choose_a_size.select_by_visible_text(self.size)
    	sleep(0.5)

    	add_to_basket = website.find_element_by_name("commit")
    	add_to_basket.click()
    	sleep(0.5)

    	checkout = website.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/a[2]')
    	checkout.click()
    	sleep(0.5)

    # Check 버튼 클릭
    def check(self):
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

"""
버려진 함수
self.lineEdit.textChanged.connect(self.account_changed)
def account_changed(self, info):
    self.info = self.lineEdit.text()
"""
