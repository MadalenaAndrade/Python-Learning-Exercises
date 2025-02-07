# Write your solution here
def list_sum(list1:list, list2:list):
    sumlist = []
    for index in range(len(list1)):
        sumlist.append(list1[index]+list2[index])
    return sumlist

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]