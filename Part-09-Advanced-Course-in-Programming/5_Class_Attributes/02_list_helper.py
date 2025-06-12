# WRITE YOUR SOLUTION HERE:
#model solution used @classmethod, but for me it makes more sense to use @staticmethod
class ListHelper:
    @staticmethod
    def greatest_frequency(my_list: list):
        frequencies = []
        for item in my_list:
            frequencies.append(my_list.count(item))

        index_max = frequencies.index(max(frequencies))
        return my_list[index_max]

    @staticmethod
    def doubles(my_list: list):
        set_numbers = set(my_list) #used set because it filters repetitive numbers

        count = 0
        for number in set_numbers:
            if my_list.count(number) >= 2:
                count += 1
        
        return count
        


if __name__=="__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
