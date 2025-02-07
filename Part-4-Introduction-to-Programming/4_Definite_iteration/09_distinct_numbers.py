# Write your solution here
def distinct_numbers(list:list):
    newlist = []
    for index in list:
        if index in newlist:
            index +=1
        else:
            newlist.append(index)
    newlist.sort()
    return newlist

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]