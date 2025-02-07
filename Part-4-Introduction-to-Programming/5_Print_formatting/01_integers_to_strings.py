# Write your solution here
def formatted(floating_points:list):
    
    stringlist = []
    for float in floating_points:
        string = f"{float:.2f}"
        stringlist.append(string)     
    return stringlist

if __name__=="__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)