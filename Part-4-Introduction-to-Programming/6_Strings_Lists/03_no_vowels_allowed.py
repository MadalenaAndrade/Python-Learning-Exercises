# Write your solution here
def no_vowels(string:str):

    newstring = ""

    for character in string:
        if character != "a" and character != "e" and character != "i" and character != "o" and character != "u":
            newstring += character 
    
    return newstring

if __name__=="__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))