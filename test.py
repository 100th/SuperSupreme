import sys
from selenium import webdriver
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from time import sleep
from selenium.webdriver.common.keys import Keys

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
    def SearchKeyword(keywords, texts):
        for i in keywords:
            if i not in texts:
                return False
        return True

    # Search 버튼 클릭
    def search(self):
        category = self.comboBox.currentText()
        keyword = self.lineEdit_13.text()
        color = self.lineEdit_14.text()
        size = self.comboBox_2.currentText()

        print(category)
        print(keyword)
        print(color)
        print(size)

    # Check 버튼 클릭
    def check(self):
        website = webdriver.PhantomJS('/Users/paramount/Downloads/phantomjs/bin/phantomjs')
        website.get('https://okky.kr/user/register')

        assert 'OKKY' in website.title

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
