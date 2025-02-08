# Write your solution here
from difflib import get_close_matches

user_text = input("Write text: ")

wordlist = []
rephrase = ""
bad_words = []
with open("wordlist.txt") as file:
    for word in file:
        wordlist.append(word.strip())
    text_words = user_text.split(" ")
    
    for word in text_words:
        if word.lower() in wordlist:
            rephrase += f"{word} "
        else:
            rephrase += f"*{word}* "
            bad_words.append(word)

    
print(rephrase)
print("suggestions:")
for word in bad_words:
    possibilities = get_close_matches(word.lower(), wordlist)
    print(f"{word}: {", ".join(possibilities)}")

