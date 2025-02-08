# Write your solution here

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")
    if function == "1":
        finnish_word = input("The word in Finnish: ")
        english_word = input("The word in English: ")
        with open("dictionary.txt","a") as dictionary:
            dictionary.write(f"{finnish_word};{english_word} \n")
            print("Dictionary entry added")

    elif function == "2":
        search_term = input("Search term: ")
        with open("dictionary.txt") as file_to_read:
            for row in file_to_read:
                parts = row.split(";")
                if search_term in parts[0]:
                    print(f"{parts[0]} - {parts[1]}")
                elif search_term in parts[1]:
                    print(f"{parts[0]} - {parts[1]}")

    elif function == "3":
        print("Bye!")
        break
