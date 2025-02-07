# Write your solution here
def remove_smallest(numbers:list):
    smallest=min(numbers)
    newlist = []

    for number in numbers:
        if number != smallest:
            newlist.append(number)
    numbers[:]=newlist
        

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)