# Write your solution here
def longest(strings: list):

    longer = ""
    for string in strings:
        if len(string)>len(longer):
            longer = string
    
    return longer


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
