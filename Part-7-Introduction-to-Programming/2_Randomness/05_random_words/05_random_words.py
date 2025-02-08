# Write your solution here
from random import sample

def words(n: int, beginning: str):
    words_list = []
    
    with open("words.txt") as file:
        for row in file:
            if row.startswith(beginning):
                words_list.append(row.strip()) #list of all words that start with the choosen part

    
    return sample(words_list, n)

if __name__=="__main__":
    print(words(3, "ca"))
