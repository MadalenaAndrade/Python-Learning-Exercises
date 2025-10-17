def lengths(list: list):
    return [len(sublist) for sublist in list]

if __name__=="__main__":
    lists = [[1,2,3,4,5], [324, -1, 31, 7],[]]
    print(lengths(lists))