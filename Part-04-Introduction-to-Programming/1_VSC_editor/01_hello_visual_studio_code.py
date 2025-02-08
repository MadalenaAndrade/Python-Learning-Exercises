# Write your solution here
while True:
    name = input("Editor:")
    if name.lower() == "visual studio code":
        print("an excellent choice!")
        break
    elif name.lower() == "word" or name.lower() == "notepad":
        print("awful")
    else:
        print("not good")
        