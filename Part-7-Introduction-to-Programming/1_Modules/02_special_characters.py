# Write your solution here
def separate_characters(my_string: str):
    from string import ascii_letters, punctuation

    
    part_one = ""
    part_two = ""
    part_three = ""
    for character in my_string:
        if character in ascii_letters:
            part_one += character
        elif character in punctuation:
            part_two += character
        else:
            part_three += character
    
    return part_one, part_two, part_three

if __name__=="__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])   