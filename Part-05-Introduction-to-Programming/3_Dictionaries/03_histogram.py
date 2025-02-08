# Write your solution here
def histogram(word:str):
    histogram = {}

    for letter in word:
        if letter not in histogram:
            histogram[letter] = []
        histogram[letter].append("*")

    for key, value in histogram.items():
        print(key, end="")
        string = ""
        for asterisk in value:
            string += asterisk 
        print(f" {string}")


if __name__=="__main__":
    histogram("abba")
    histogram("statistically")