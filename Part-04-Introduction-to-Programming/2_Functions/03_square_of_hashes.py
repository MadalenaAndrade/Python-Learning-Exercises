# Copy here code of line function from previous exercise
def line(length, text):
    if text == "":
        print(length*"*")
    else:
        print(length*text[0])

def square_of_hashes(size):
    # You should call function line here with proper parameters
    height = size
    while height > 0:
        line(size, "#")
        height -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
