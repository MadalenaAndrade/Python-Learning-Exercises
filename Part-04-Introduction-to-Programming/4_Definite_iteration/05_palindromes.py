# Write your solution here
def palindromes(word:str):
    list=[]
    for character in word:
        list.append(character)
    backwards = list[::-1]
    return list == backwards

while True:
    string = input("Please type in a palindrome:")
    if palindromes(string):
        print(f"{string} is a palindrome!")
        break
    print("that wasn't a palindrome")

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
