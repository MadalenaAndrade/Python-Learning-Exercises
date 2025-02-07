# write your solution here
def check_dictionary(string:str):
    
    word_file = []
    new_string = ""
    
    with open("wordlist.txt") as file:
        for line in file:
            word_file.append(line.strip().lower()) #strip useless characters and put everything in lower caps
    
    words_list = string.split()

    for word in words_list:
        if word.lower() in word_file:
            new_string += f"{word} "
        else:
            new_string += f"*{word}* "

    print(new_string)

if True:
    text = input("Write text:") 
     
else:
    text = "We use ptython to make a spell checker"
    

check_dictionary(text)
