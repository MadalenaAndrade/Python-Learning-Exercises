# Write your solution here
def sum_of_positives(list:list):
    index = 0
    while len(list)>index:
        if list[index] <= 0:
            list.remove(list[index])
            index -= 1
        index += 1
    return sum(list)

if __name__ == "__main__":
    my_list=[3, -1, -1, -1, 1]
    result=sum_of_positives(my_list)
    print(f"The result is {result}")