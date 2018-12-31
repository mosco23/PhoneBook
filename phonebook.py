#!/usr/bin/python3

list = dict()

get_num = input("Enter the number * > ")
get_name = input("\nEnter the name * > ")
get_mail = input("\nEnter the E-mail > ")

list[get_name] = (get_num, get_mail)
print(list)
