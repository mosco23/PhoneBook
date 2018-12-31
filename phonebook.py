#!/usr/bin/python3

list = dict()
inp = input("Enter for start :) ")
while inp != "exit".lower():
    inp = input("\n> ").lower()
    if inp == "add".lower():
        get_name = input("\n\tEnter the name * > ")
        get_num = input("\n\tEnter the phone number * > ")
        get_mail = input("\n\tEnter the E-mail > ")
        list[get_name] = (get_num, get_mail)
    else:
        print("\ncommand not found :-(")
else:
    print("\nGood Bye :-)\n")
