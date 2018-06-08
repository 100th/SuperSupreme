import sys
from selenium import webdriver
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
"""
service_args = [ '--proxy=localhost:9150', '--proxy-type=socks5', ]
driver = webdriver.PhantomJS(executable_path='/Users/paramount/Downloads/phantomjs/bin/phantomjs', service_args=service_args)

driver.get('https://www.supremenewyork.com/shop')

driver.save_screenshot('search_results.png')
"""
form_class = uic.loadUiType("SuperSupreme.ui")[0]

class QtDesigner(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

    def timeout(self):
        current_time = QTime.currentTime()
        text_time = current_time.toString("hh:mm:ss")
        time_msg = "Current Time : " + text_time
        self.statusbar.showMessage(time_msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtDesigner = QtDesigner()
    QtDesigner.show()
    app.exec_()
