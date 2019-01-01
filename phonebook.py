#!/usr/bin/python3
from os import system, chdir, listdir, getenv

system("clear")
home_dc = getenv("HOME")
chdir(home_dc)
ls = listdir()
if ".Phone_Lists.txt" not in ls:
    open(".Phone_Lists.txt", "w+").close()

inp = input("Enter for start :) ")
while inp != "exit".lower():
    inp = input("\n> ").lower()
    if inp == "add".lower():
        file = open(".Phone_Lists.txt", "a")
        get_name = input("\n\tEnter the name * > ")
        get_num = int(input("\n\tEnter the phone number * > "))
        get_mail = input("\n\tEnter the E-mail > ")
        file.write(f"{get_name}\t{get_num}\t{get_mail}\n")
        file.close()
    elif inp == "show".lower():
        file = open(".Phone_Lists.txt")
        print("name\tphoneNumber\tmail")
        for i in file:
            print(i)
    elif inp == "search".lower():
        search_val = input("\nEnter the name for search > ")
        c = len(search_val)
        f = open(".Phone_Lists.txt", "r")
        read = f.readlines()
        for i in read:
            if i[:c] == search_val:
                print(i)
    elif inp == "exit".lower():
        pass
    else:
        print("\ncommand not found :-(")
else:
    print("\nGood Bye :-)\n")
