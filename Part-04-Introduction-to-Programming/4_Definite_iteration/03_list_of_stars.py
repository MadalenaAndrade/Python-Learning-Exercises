# Write your solution here
def list_of_stars(list:list):
    for item in list:
        print(item*"*")

if __name__ == "__main__":
    mylist=[3, 7, 1, 1, 2]
    result = list_of_stars(mylist)