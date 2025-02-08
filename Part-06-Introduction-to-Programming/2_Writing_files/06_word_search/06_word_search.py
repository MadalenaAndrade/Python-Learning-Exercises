# Write your solution here
def search_exact_words(search_term: str, words_list: list):
    words = []
    for word in words_list:
        if word == search_term:
            words.append(word)
    
    return words

def search_asterisked_words(search_term: str, words_list: list):
    
    words = []

    for word in words_list:
        if search_term[-1]=="*":
            if word.startswith(search_term[0:len(search_term)-1]):
                words.append(word)
        elif search_term[0]=="*":
            if word.endswith(search_term[1:]):
                words.append(word)
    
    return words          

def search_dotted_words(search_term: str, words_list: list):
    
    words = []
    #1-verify if the word is same lenght, 2- check if not dotted letters are the same
    for word in words_list:
        if len(word) == len(search_term):
            match = True
            for i in range(len(search_term)):
                if search_term[i] != "." and search_term[i] != word[i]:
                    match = False
            if match:
                words.append(word) 
    return words

def turn_to_list(words_list_file: str):
    words = []
    with open(words_list_file) as new_file:
        for row in new_file:
            word = row.strip()
            words.append(word)
    
    return words

def find_words(search_term: str):
    words_list = turn_to_list("words.txt")

    if "." in search_term:
        words = search_dotted_words(search_term, words_list)
    elif "*" in search_term:
        words = search_asterisked_words(search_term, words_list)
    else:
        words = search_exact_words(search_term, words_list)
    
    return words

if __name__=="__main__":
    print(find_words(".a.e"))





