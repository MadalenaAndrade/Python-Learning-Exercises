# WRITE YOUR SOLUTION HERE:
class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        checked = []
        counts = []
        for item in my_list:
            if item not in checked:
                counts.append((item, my_list.count(item)))
                checked.append(item)
        greatest = 0
        common_item = ""
        for tupple in counts:
            if tupple[1] > greatest:
                greatest = tupple[1]
                common_item = tupple[0]
        return common_item

    @classmethod
    def doubles(cls, my_list: list):
        checked = []
        counts = []
        for item in my_list:
            if item not in checked:
                counts.append((item, my_list.count(item)))
                checked.append(item)
        count = 0
        for tupple in counts:
            if tupple[1] >= 2:
                count += 1
        return count

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))