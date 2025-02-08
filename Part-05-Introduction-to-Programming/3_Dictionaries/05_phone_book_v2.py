# Write your solution here
def search(contact_list):
    name = input("name: ")
    if name not in contact_list:
        print("no number")
    else:
        for number in contact_list[name]:
            print(number)

def add(contact_list):
    name = input("name:")
    number = input("number:")
    if name not in contact_list:
        contact_list[name]=[]
    contact_list[name].append(number)
    print("ok!")

def main():
    contact_list={}

    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 1:
            search(contact_list)
        if command == 2:
            add(contact_list)
        if command == 3:
            break
    print("quitting...")

main()