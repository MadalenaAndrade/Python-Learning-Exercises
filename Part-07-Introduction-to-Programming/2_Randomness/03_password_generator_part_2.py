# Write your solution here
from string import ascii_lowercase, digits
from random import choice, shuffle


def generate_strong_password(length: int, has_numbers: bool, has_specials: bool):
    password = []
    used_characters = 0
    punctuation = "!?=+-()#"

    #one lower character
    password.append(choice(ascii_lowercase))
    used_characters +=1
    #only lower chars
    if not has_numbers and not has_specials:
        for i in range(length-used_characters):
            password.append(choice(ascii_lowercase))
    #only numbers
    elif has_numbers and not has_specials:
        password.append(choice(digits))
        used_characters +=1
        for i in range(length-used_characters):
            password.append(choice(ascii_lowercase + digits))
    #only specials
    elif has_specials and not has_numbers:
        password.append(choice(punctuation))
        used_characters +=1
        for i in range(length-used_characters):
            password.append(choice(ascii_lowercase+punctuation))
    #has everything
    else:
        password.append(choice(digits))
        password.append(choice(punctuation))
        used_characters +=2
        for i in range(length-used_characters):
            password.append(choice(ascii_lowercase+punctuation+digits))
    
    password.sort()
    strong_password = ""
    for character in password:
        strong_password += character
    return strong_password
    

