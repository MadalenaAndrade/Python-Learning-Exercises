# Write your solution here
number = int(input("How many items:"))
itemnumber = 1
list = []
while number > 0:
    item = int(input(f"Item {itemnumber}:"))
    list.append(item)
    itemnumber += 1
    number -= 1
print(list)
