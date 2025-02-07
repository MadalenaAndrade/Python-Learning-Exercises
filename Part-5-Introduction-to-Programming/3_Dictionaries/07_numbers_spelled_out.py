# Write your solution here
def dict_of_numbers():
    numbers_dictionary = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 15:"fifteen", 18:"eighteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 80:"eighty"}

    for key in range(14,20):
        if key != 18 and key != 15:
            numbers_dictionary[key]=numbers_dictionary[key-10]+"teen"
    for key in range(4,10):
        if key != 4 and key != 8 and key != 5:
            numbers_dictionary[key*10]=numbers_dictionary[key]+"ty"

    for n in range(21,100):
        if n!=30 and n!=40 and n!=50 and n!=60 and n!=70 and n!=80 and n!=90:
            if n <30:
                numbers_dictionary[n]=numbers_dictionary[20]+"-"+numbers_dictionary[n-20]
            elif n < 40:
                numbers_dictionary[n]=numbers_dictionary[30]+"-"+numbers_dictionary[n-30]
            elif n < 50:
                numbers_dictionary[n]=numbers_dictionary[40]+"-"+numbers_dictionary[n-40]
            elif n < 60:
                numbers_dictionary[n]=numbers_dictionary[50]+"-"+numbers_dictionary[n-50]
            elif n < 70:
                numbers_dictionary[n]=numbers_dictionary[60]+"-"+numbers_dictionary[n-60]
            elif n < 80:
                numbers_dictionary[n]=numbers_dictionary[70]+"-"+numbers_dictionary[n-70]
            elif n < 90:
                numbers_dictionary[n]=numbers_dictionary[80]+"-"+numbers_dictionary[n-80]
            else:
                numbers_dictionary[n]=numbers_dictionary[90]+"-"+numbers_dictionary[n-90]


    return numbers_dictionary




if __name__=="__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])