from string import punctuation
# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as file:
        contents = file.read()
        contents = "".join([character for character in contents if character not in punctuation]).split()
        return {word: contents.count(word) for word in contents if contents.count(word) >= lower_limit}
    
if __name__=="__main__":
    print(most_common_words("comprehensions.txt", 3))