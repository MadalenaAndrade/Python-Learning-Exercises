# Write your solution here
def everything_reversed(strings_list:list):

    newlist = []

    for string in strings_list:
        newlist.append(string[::-1]) #reverse the word
        
    newlist = newlist[::-1]
    return newlist

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)