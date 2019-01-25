#!/usr/bin/python3
import sys
import sqlite3
from PyQt5.QtWidgets import *
from phonebook import PhoneBook


class Window(QTabWidget):
    def __init__(self):
        super().__init__()
        self.window()

    def window(self):
        # Base
        self.setGeometry(420, 170, 500, 350)
        self.setWindowTitle("Phone book ")
        self.setStyleSheet("background-color: #54646E")

        # Create Tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.addTab(self.tab1, "Add")
        self.addTab(self.tab2, "Search")
        self.addTab(self.tab3, "Show")

        # Add Tab Objects
        self.getName = QLineEdit(self.tab1)
        self.getNum = QLineEdit(self.tab1)
        self.getMail = QLineEdit(self.tab1)
        self.getName.setPlaceholderText('Name')
        self.getNum.setPlaceholderText('Phone Number')
        self.getMail.setPlaceholderText('example@mail.com')

        self.addButton = QPushButton("add", self.tab1)
        self.addButton.clicked.connect(self.add)

        horizon = QHBoxLayout()
        horizon.addWidget(self.getName)
        horizon.addWidget(self.getNum)
        horizon.addWidget(self.getMail)
        horizon.addWidget(self.addButton)
        horizon.addStretch()
        self.tab1.setLayout(horizon)

        # Search Tab Objects
        self.search_inp = QLineEdit(self.tab2)
        self.search_inp.setPlaceholderText("Search Here")
        self.search_inp.setGeometry(1, 10, 200, 25)

        self.searchButton = QPushButton("Search", self.tab2)
        self.searchButton.setGeometry(220, 10, 100, 25)
        self.searchButton.clicked.connect(self.search)

        self.showBox = QTextEdit(self.tab2)
        self.showBox.setText("ID\tNAME\tPHONENUMBER   EMAIL")
        self.showBox.setReadOnly(1)
        self.showBox.setGeometry(2.5, 50, 491, 250)

        # Show Tab Objects
        self.textBox = QTextEdit(self.tab3)
        self.textBox.setText("ID NAME PHONENUMBER   EMAIL\n")
        self.textBox.setReadOnly(1)
        self.textBox.setGeometry(2.5, 10, 491, 300)

        self.cBottun = QPushButton("Just Click", self.tab3)
        self.cBottun.move(200, 150)
        self.cBottun.clicked.connect(self.cShow)

        self.show()

    def add(self):
        submit = PhoneBook(self.getName.text(), self.getNum.text(), self.getMail.text())
        submit.submit()

    def search(self):
        db = sqlite3.connect('database.db')
        c = db.cursor()
        c.execute("SELECT * FROM Post WHERE Names='{}'".format(self.search_inp.text()))
        for data in c.fetchall():
            self.showBox.append(str(data))
        db.close()

    def cShow(self):
        self.cBottun.hide()
        db = sqlite3.connect('database.db')
        c = db.cursor()
        c.execute("SELECT * FROM Post")
        for data in c.fetchall():
            self.textBox.append(str(data))


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
