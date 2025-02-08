# Write your solution here
def shortest(list:list):
    short = len(list[0])
    word = list[0]
    for string in list:
        if len(string)<short:
            short = len(string)
            word = string    
    return word

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)