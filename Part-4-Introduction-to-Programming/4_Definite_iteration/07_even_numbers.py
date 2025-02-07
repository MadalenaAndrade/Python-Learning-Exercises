# Write your solution here
def even_numbers(list:list):
    even = []
    for index in list:
        if index %2 ==0:
            even.append(index)
    return even

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)

