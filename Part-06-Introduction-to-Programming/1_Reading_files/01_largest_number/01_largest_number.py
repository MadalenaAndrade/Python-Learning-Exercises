# write your solution here
#as there are negative numbers we have to start differently as the first number may be lower than 0.
#If all the number were negative, the biggest would be 0 which is not true

def largest():
    
    start = True
    largest = 0
    with open("numbers.txt") as new_file:
        for number in new_file:
            number=int(number.replace("\n",""))
            if start or number > largest: #when it starts the largest is the first number regardless of being 0 or not
                largest = number
                start = False    
    return largest

