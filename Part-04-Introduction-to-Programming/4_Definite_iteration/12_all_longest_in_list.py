# Write your solution here
def all_the_longest(list:list):
    longest = 0
    word = ""
    newlist = []
    for string in list:
        if len(string)>longest:
            longest = len(string)
            word = string
    newlist.append(word) 

    for string in list:
        if len(string)==longest and string!=word:
            newlist.append(string)
    return newlist

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)