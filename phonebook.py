#!/usr/bin/python3
import web
from os import system
from gui import Window
from sys import argv, exit
from database import DataBase
from prettytable import PrettyTable
from PyQt5.QtWidgets import QApplication


def main():
    """
    ABOUT\n
    \tThe phone book application for linux with GUI and WEB UI.
    \tAuthor -> Saman Malekian
    \ttelegram ID -> https://t.me/M4lekian
    \tGithub -> https://github.com/SamanMalekian\n
    OPTIONS\n
    \t-h\t-->\tShow this page
    \t-w\t-->\tRun app with WEB UI
    \t-g\t-->\tRun app with Graphical UI\n
    COMMANDS\n
    \tadd\t -->\tAdd new phone number
    \tdelete\t -->\tDelete contacts via id
    \tedit\t -->\tEdit the contact's data
    \tshow\t -->\tShow the registered phone numbers
    \tsearch\t -->\tSearch with name in registered phone numbers
    """
    if "-h" in argv:
        print(main.__doc__)
    elif "-g" in argv:
        app = QApplication(argv)
        a_window = Window()
        a_window.window()
        exit(app.exec_())
    elif "-w" in argv:
        web.app.run(host="127.0.0.1", port=8000)
    else:
        system("clear")
        inp = input("Press the enter :)")
        while inp != "exit":
            inp = (input("\n-> ")).lower()
            data = DataBase(table="USERS").get()
            if inp == "add":
                get_name = input("\tName -> ")
                get_num = input("\tPhone Number -> ")
                get_mail = input("\tEmail -> ")
                DataBase(table="USERS", rows="name, number, email", values=f"'{get_name}',\
                     '{get_num}', '{get_mail}'").add()
            elif inp == "show":
                table = PrettyTable(['id', 'name', 'phone number', 'email address'])
                for i in data:
                    table.add_row([i[0], i[1], i[2], i[3]])
                print(table)
            elif inp == "search":
                value = input("\nEnter the name for search > ")
                search_data = []
                for i in data:
                    find = False
                    for x in i:
                        if value in str(x):
                            find = True
                            break
                    if find:
                        search_data.append(i)
                if len(search_data) != 0:
                    table = PrettyTable(['id', 'name', 'phone number', 'email address'])
                    for i in search_data:
                        table.add_row([i[0], i[1], i[2], i[3]])
                    print(table)
                else: 
                    print("\n\tContact not found !\n")
            elif inp == "delete":
                get_id = input("\tEnter the id -> ")
                try:
                    get_id = int(get_id)
                except ValueError:
                    get_id = input("\tPlease enter the id (or 0 for return) -> ")
                DataBase(table="USERS", rows="id", values=get_id).delete()
            elif inp == "edit":
                get_id = input("\tEnter the id -> ")
                data = DataBase(table="USERS", values=f"id='{get_id}'").search()
                if len(data) > 0:
                    data = data[0]
                    name = input(f"\n\tName ( Current value : {data[1]} ) > ") or data[1]
                    numb = input(f"\n\tphone number ( Current value : {data[2]} ) > ") or data[2]
                    mail = input(f"\n\tEmail address ( Current value : {data[3]} ) > ") or data[3]
                    DataBase(table="USERS", rows="id, name, number, email",
                             values=f"'{data[0]}', '{name}', '{numb}', '{mail}'").replace()
                    print('\ndata`s successfully edited!')
                else:
                    print('\n\tid`s not found !')
                    

if __name__ == "__main__":
    main()
