#!/usr/bin/python3
from sys import argv
from os import system, chdir, listdir, getenv


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
        file = open(".Phone_Lists.txt", "a")
        file.write(f"{self.name}\t{self.num}\t{self.email}\n")
        file.close()

    def show(self):
        file = open(".Phone_Lists.txt")
        print("\nname\tphoneNumber\tmail\n")
        for i in file:
            print(i)

    def search(self, value):
        c = len(value)
        f = open(".Phone_Lists.txt", "r")
        read = f.readlines()
        for i in read:
            if i[:c] == value:
                print(i)


def main():
    if "-h" in argv:
        print(PhoneBook.__doc__)
    else:
        system("clear")
        home_dc = getenv("HOME")
        chdir(home_dc)
        ls = listdir()
        if ".Phone_Lists.txt" not in ls:
            open(".Phone_Lists.txt", "w+").close()
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
