# Write your solution here
def line(length, text):
    if text == "":
        print(length*"*")
    else:
        print(length*text[0])


# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")