# Write your solution here
def no_shouting(words_list:list):
    newlist = []
    for word in words_list:
        if word.isupper() ==False:
            newlist.append(word)
    
    return newlist

if __name__=="__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)

