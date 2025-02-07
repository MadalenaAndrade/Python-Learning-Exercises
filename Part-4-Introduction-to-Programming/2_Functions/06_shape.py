# Copy here code of line function from previous exercise and use it in your solution
def line(length, text):
    if text == "":
        print(length*"*")
    else:
        print(length*text[0])

def shape(tsize, tcharacter, ssize, scharacter):
    n = 0
    sshape = tsize
    while tsize >= 0:
        line(n, tcharacter)
        tsize -=1
        n += 1
    
    while ssize > 0:
        line(sshape, scharacter)
        ssize -=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "*")