# Write your solution here
def longest_series_of_neighbours(number_list:list):
    index = 1
    length = 1
    maxlength = 1

    for number in number_list:
        if index >= len(number_list):
            index -=1
        elif number+1 == number_list[index] or number-1 == number_list[index]:
            length +=1
        else:
            if length > maxlength:
                maxlength = length
            length = 1
        index += 1    
    
    if length > maxlength:
        maxlength = length
    
    return maxlength

if __name__=="__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))