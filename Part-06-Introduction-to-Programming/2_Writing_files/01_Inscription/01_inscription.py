# Write your solution here
if True:
    name = input("Whom should I sign this to:")
    file = input("Where shall I save it:")
else:
    name = "Ana"
    file = "inscribed.txt"

with open(file, "w") as new_file:
    new_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")