# Here we create our own web browser

# Let's start

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *



class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://bing.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navigbar = QToolBar()
        self.addToolBar(navigbar)

        backButton = QAction('Back', self)
        backButton.triggered.connect(self.browser.back)
        navigbar.addAction(backButton)

        forwardButton = QAction('Forward', self)
        forwardButton.triggered.connect(self.browser.forward)
        navigbar.addAction(forwardButton)

        reloadButton = QAction('Reload', self)
        reloadButton.triggered.connect(self.browser.reload)
        navigbar.addAction(reloadButton)

        homeButton = QAction('Home', self)
        homeButton.triggered.connect(self.navigate_home)
        navigbar.addAction(homeButton)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navigbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)
        

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://CodeWithSomesh.com"))

        

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

App = QApplication(sys.argv)
QApplication.setApplicationName('CodeWithSomesh Browser')
window = MainWindow()
App.exec_()





    




