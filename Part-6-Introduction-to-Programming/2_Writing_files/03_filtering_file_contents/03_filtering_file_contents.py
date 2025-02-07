# Write your solution here
def filter_solutions():
    with open("solutions.csv") as source, open("correct.csv","w") as correct_file, open("incorrect.csv","w") as incorrect_file:
        #split into parts
        for row in source:
            parts = row.split(";")

            calculation = parts[1]
            result = parts[2]

            #check for operators
            if "+" in calculation:
                operands = calculation.split("+")
                correct = int(operands[0])+int(operands[1]) == int(result) #check if the correct is the same as result returnong wither True or False
            elif "-" in calculation:
                operands = calculation.split("-")
                correct = int(operands[0])-int(operands[1]) == int(result)

            #write a file
            if correct:
                correct_file.write(row)
            else:
                incorrect_file.write(row)
    

