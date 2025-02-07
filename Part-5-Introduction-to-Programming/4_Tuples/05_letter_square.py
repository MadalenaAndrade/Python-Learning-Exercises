# Write your solution here

alphabet = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}

layers = int(input("Layers"))

lenght = 1 + 2*(layers-1)
new_lenght=lenght
n = 0
frame = ""
inverted_frame = frame
first_rows = []

for i in range(lenght//2): #print half of the square and save it
    print(f"{frame}{new_lenght*alphabet[layers-n]}{frame[::-1]}")
    first_rows.append(f"{frame}{new_lenght*alphabet[layers-n]}{frame[::-1]}")
    frame += alphabet[layers-n]
    n += 1
    new_lenght -= 2

middle_string = f"{frame}{new_lenght*alphabet[layers-n]}{frame[::-1]}" #middle row
print(middle_string)

for row in first_rows[::-1]: #other half
    print(row)












