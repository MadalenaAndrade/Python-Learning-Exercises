# write your solution here
def read_fruits():
    dictionary = {}
    with open("fruits.csv") as new_file:
        for fruit in new_file:
            fruit = fruit.replace("\n","")
            parts = fruit.split(";")
            dictionary[parts[0]]=float(parts[1])
    
    return dictionary