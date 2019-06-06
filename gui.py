from database import DataBase
from PyQt5.QtWidgets import QTabWidget, QWidget, QLineEdit, QPushButton, QHBoxLayout, QTextEdit


class Window(QTabWidget):
    def __init__(self):
        super().__init__()

        # Tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        # Appearance Base
        self.background_color = "#000"
        self.window_title = "Phone Book"
        self.loc = {'top': 170, 'left': 420, 'width': 500, 'height': 500}

        # Add Tab Objects
        self.get_name = QLineEdit(self.tab1)
        self.get_num = QLineEdit(self.tab1)
        self.get_mail = QLineEdit(self.tab1)
        self.addButton = QPushButton("add", self.tab1)

        # Search Tab Objects
        self.search_inp = QLineEdit(self.tab2)
        self.searchButton = QPushButton("Search", self.tab2)
        self.showBox = QTextEdit(self.tab2)

        # Show Tab Objects
        self.textBox = QTextEdit(self.tab3)
        self.cBottun = QPushButton("Just Click", self.tab3)

    def window(self):
        # Base
        self.setWindowTitle(self.window_title)
        self.setStyleSheet(f"background-color: {self.background_color}")
        self.setGeometry(self.loc['left'], self.loc['top'], self.loc['width'], self.loc['height'])

        # Tabs
        self.addTab(self.tab1, "Add")
        self.addTab(self.tab2, "Search")
        self.addTab(self.tab3, "Show")

        # Add Tab Atributies
        self.get_name.setPlaceholderText('Name')
        self.get_num.setPlaceholderText('Phone Number')
        self.get_mail.setPlaceholderText('example@mail.com')

        self.addButton.clicked.connect(self.add)

        horizon = QHBoxLayout()
        horizon.addWidget(self.get_name)
        horizon.addWidget(self.get_num)
        horizon.addWidget(self.get_mail)
        horizon.addWidget(self.addButton)
        horizon.addStretch()
        self.tab1.setLayout(horizon)

        # Search Tab Atributies
        self.search_inp.setPlaceholderText("Search Here")
        self.search_inp.setGeometry(1, 10, 200, 25)

        self.searchButton.setGeometry(220, 10, 100, 25)
        self.searchButton.clicked.connect(self.search)

        self.showBox.setText("ID\tNAME\tPHONENUMBER   EMAIL")
        self.showBox.setReadOnly(True)
        self.showBox.setGeometry(2, 50, 491, 250)

        # Show Tab Atributies
        self.textBox.setText("ID NAME PHONENUMBER   EMAIL\n")
        self.textBox.setReadOnly(True)
        self.textBox.setGeometry(2, 10, 491, 300)

        self.cBottun.move(200, 150)
        self.cBottun.clicked.connect(self.c_show)

        self.show()

    def add(self):
        DataBase(table="USERS", rows="name, number, email", values=f"'{self.get_name.text()}',\
                    '{self.get_num.text()}', '{self.get_mail.text()}'").add()

    def search(self):
        data = DataBase(table="USERS", values=f"name='{self.search_inp.text()}'").search()
        for i in data:
            self.showBox.append(str(i))

    def c_show(self):
        self.cBottun.hide()
        data = DataBase(table="USERS").get()
        for i in data:
            self.textBox.append(str(i))
