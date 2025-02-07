# Write your solution here
n = 0
sentence = []
while True:
    word = input("Word:")
    if word in sentence:
        break
    n +=1
    sentence.append(word)
print(f"You typed in {n} different words")
