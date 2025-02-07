# Write your solution here
contact_list = {}

while True:
    command=int(input("command (1 search, 2 add, 3 quit):"))
    if command == 3:
        print("quitting...")
        break
    if command == 1:
        name = input("name:")
        if name not in contact_list:
            print("no number")
        else:
            print(contact_list[name])
    if command == 2:
        name = input("name:")
        number = input("number:")
        contact_list[name]=number
        print("ok!")