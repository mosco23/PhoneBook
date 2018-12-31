#!/usr/bin/python3

list = dict()
inp = input("Enter for start :) ")
while inp != "exit".lower():
    inp = input("> ").lower()
    if inp == "add".lower():
        get_name = input("Enter the name * > ")
        get_num = input("Enter the phone number * > ")
        get_mail = input("Enter the mail > ")
        list[get_name] = (get_num, get_mail)
