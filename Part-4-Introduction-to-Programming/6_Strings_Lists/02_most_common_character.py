# Write your solution here
def most_common_character(string:str):

    usedcharacters = ""
    commoncharacter = ""
    maxcount = 0

    for character in string:
        if character not in usedcharacters:
            count = string.count(character)
            usedcharacters += character
            if count > maxcount:
                maxcount = count
                commoncharacter = character

    return commoncharacter

if __name__=="__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
         
