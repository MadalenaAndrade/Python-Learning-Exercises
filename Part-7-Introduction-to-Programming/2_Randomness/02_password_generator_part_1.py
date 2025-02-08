# Write your solution here
from string import ascii_lowercase
from random import choice

def generate_password(length):
    abc = []
    for character in ascii_lowercase:
        abc += character
    
    password = ""
    for i in range(0, length):
        password += choice(abc)

    return password
        

if __name__=="__main__":
    generate_password(2)