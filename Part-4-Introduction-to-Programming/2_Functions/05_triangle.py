# Copy here code of line function from previous exercise
def line(length, text):
    if text == "":
        print(length*"*")
    else:
        print(length*text[0])

def triangle(size):
    # You should call function line here with proper parameters
    n = 0
    while size > 0:
        line(n+1, "#")
        n += 1
        size -= 1 

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
