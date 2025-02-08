# Write your solution here
list = []
print(f"The list is now {list}")
n = 0
while True:
    option = input("a(d)d, (r)emove or e(x)it:")
    if option == "x":
        break
    elif option == "d" and n >= 0:
        n +=1
        list.append(n)
        print(f"The list is now {list}")
    elif option == "r" and n > 0:
        n -=1
        list.pop(n) 
        print(f"The list is now {list}")
print("Bye!")
