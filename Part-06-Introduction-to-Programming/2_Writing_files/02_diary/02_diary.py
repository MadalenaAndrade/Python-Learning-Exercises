# Write your solution here
#read everything first and save it
with open("diary.txt") as file:
    content = []
    for row in file:
        content.append(row.replace("\n",""))

#open file for appending
with open("diary.txt", "a") as new_file:
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        option = int(input("Function:"))
        if option == 1:
            new_entry = input("Diary entry:")
            new_file.write(new_entry + "\n")
            content.append(new_entry)
            print("Diary saved")
        elif option == 2:
            print("Entries:")
            for entry in content:
                print(entry)
        elif option == 0:
            print("Bye now!")
            break