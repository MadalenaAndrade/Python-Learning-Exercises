# Write your solution here
def change_case(orig_string: str):
    new_string = ""
    for letter in orig_string:
        if letter.isupper():
            new_string += letter.lower()
        elif letter.islower():
            new_string += letter.upper()
        else:
            new_string += letter
    
    return new_string

def split_in_half(orgi_string: str):
    first_half = ""
    letters_list = []

    for letter in orgi_string:
        letters_list.append(letter)
    
    for i in range(int(len(orgi_string)/2)):
        first_half += str(letters_list[i])
    
    second_half = orgi_string.replace(first_half, "")
    return first_half, second_half    

def remove_special_characters(orig_string: str):
    from string import ascii_letters, digits
    
    new_string = ""
    allowed_characters = ascii_letters + digits + " "
    
    for letter in orig_string:
        if letter in allowed_characters:
            new_string += letter
    
    return new_string

if __name__=="__main__":
    my_string = "This is a test, lets see how it goes!!"
    print(remove_special_characters(my_string))