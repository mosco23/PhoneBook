#!/usr/bin/python3
import sqlite3
from sys import argv
from os import system


class PhoneBook:
    """
    ABOUT\n
    \tThe phone book application for linux with GUI interface and web Version.
    \tAuthor -> Saman Malekian
    \tGithub -> https://github.com/SamanMalekian
    \ttelegram ID -> https://t.me/M4lekian\n
    OPTIONS\n
    \t-h\t-->\tShow this page
    \t-g\t-->\tRun app with GUI interface
    \t-w\t-->\tRun app with WEB version\n
    COMMANDS\n
    \tadd\t -->\tAdd new phone number
    \tshow\t -->\tShow the registered phone numbers
    \tsearch\t -->\tSearch with name in registered phone numbers
    """

    def __init__(self, name=0, num=0, email=0):
        self.name = name
        self.email = email
        self.num = num

    def submit(self):
        db = sqlite3.connect('database.db')
        c = db.cursor()
        sql = "INSERT INTO Post(Names, Numbers, Emails) VALUES('{}', '{}', '{}')".format(
            self.name, self.num, self.email)
        c.execute(sql)
        db.commit()
        db.close()

    def show(self):
        db = sqlite3.connect('database.db')
        c = db.cursor()
        c.execute("SELECT * FROM Post")
        fetched = c.fetchall()
        db.commit()
        db.close()
        print("ID\tNAME\tPHONE NUMBER\tMAIL")
        for i in fetched:
            for y in range(0, 4):
                print(i[y], '\t', end='')
            print()

    def search(self, value):
        db = sqlite3.connect('database.db')
        c = db.cursor()
        c.execute("SELECT * FROM Post WHERE Names='{}'".format(value))
        db.close()
        for data in c.fetchall():
            for i in range(0, 4):
                print(data[i], end='\t')
            print()


def main():
    if "-h" in argv:
        print(PhoneBook.__doc__)
    elif "-g" in argv:
        system("python3 gui.py")
    elif "-w" in argv:
        system("python3 web.py")
    else:
        system("clear")
        inp = input("Press the enter :)")
        while inp != "exit":
            inp = input("\n-> ")
            inp = inp.lower()
            if inp == "add":
                getName = input("\tName -> ")
                getNum = input("\tPhone Number -> ")
                getMail = input("\tEmail -> ")
                submit = PhoneBook(getName, getNum, getMail)
                submit.submit()
            elif inp == "show":
                show = PhoneBook()
                show.show()
            elif inp == "search":
                search_val = input("\nEnter the name for search > ")
                search = PhoneBook()
                search.search(search_val)


if __name__ == "__main__":
    main()
