# Write your solution here
def create_tuple(x: int, y: int, z: int):
    list=[x,y,z]
    minimum = min(list)
    maximum = max(list)
    all = x+y+z

    return (minimum, maximum, all)



if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
