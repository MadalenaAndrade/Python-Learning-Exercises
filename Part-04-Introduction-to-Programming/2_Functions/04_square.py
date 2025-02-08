# Copy here code of line function from previous exercise
def line(length, text):
    if text == "":
        print(length*"*")
    else:
        print(length*text[0])

def square(size, character):
    # You should call function line here with proper parameters
    column = size
    while column > 0:
        line(size, character)
        column -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")