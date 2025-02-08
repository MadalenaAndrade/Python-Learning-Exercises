# Write your solution here
def same_chars(name, character1, character2):
    if character1 < 0 or character2 < 0 or character1 >= len(name) or character2 >= len(name):
        return False
    return name[character1] == name[character2]
   
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))