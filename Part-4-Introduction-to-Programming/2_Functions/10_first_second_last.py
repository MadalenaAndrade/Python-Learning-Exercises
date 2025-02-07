#see model solution!!!
# Write your solution here
def first_word(sentence):
    space = sentence.find(" ")
    firstword = sentence[0:space]
    return firstword

def second_word(sentence):
    space = sentence.find(" ")
    sentence = sentence[space+1:]
    secondspace = sentence.find(" ")
    if secondspace == -1:
        return sentence
    else: 
        secondword = sentence[0:secondspace]
        return secondword

def last_word(sentence):
    cutsentence = sentence
    while cutsentence[len(cutsentence)-1] != " ":
        cutsentence = cutsentence[0:len(cutsentence)-1]
    lastword = sentence[len(cutsentence):len(sentence)]
    return lastword


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word("first second"))
    print(last_word(sentence))