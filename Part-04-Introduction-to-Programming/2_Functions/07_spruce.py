# Write your solution here
def tree(height, character):
    one_character = character
    while height > 0:
        print(" "*(height-1)+character)
        character += one_character+one_character
        height -= 1
    

def spruce(size):
    print("a spruce!")
    tree(size, "*")
    print(" "*(size-1)+"*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)