#import
import sys
from turtle import forward
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
#main
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #bar (main)
        bar = QToolBar()
        self.addToolBar(bar)
        #back button
        back_btn = QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        bar.addAction(back_btn)
        #forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        bar.addAction(forward_btn)
        #reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        bar.addAction(reload_btn)
        #home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        bar.addAction(home_btn)
        #url bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        bar.addWidget(self.url_bar)
        #url update bar
        self.browser.urlChanged.connect(self.update_url)
    #function home button
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com/'))
    #function url bar
    def navigate_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    #function update url bar
    def update_url(self, q):
        self.url_bar.setText(q.toString())

#main
app = QApplication(sys.argv)
QApplication.setApplicationName('Simeple Browser')
window = MainWindow()
app.exec_()