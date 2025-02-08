# Write your solution here
from string import ascii_uppercase

def run(program: list):
    variables = {letter: 0 for letter in ascii_uppercase} #for loop that creates a key:value for each letter 
    
    #check first all commands to store any location:
    locations = {}
    
    index = 0
    while index < len(program):
        if ":" in program[index]:
            location = program[index].split(":")[0]
            locations[location] = program[(index+1):]
        index += 1

    #reads all commands
    index = 0
    print_values = []
    used_variables = {}

    while index < len(program):
        if "PRINT" in program[index]:
            value = program[index].split()[1] #ignores the [0] that is "PRINT" and saves the value
            if value in ascii_uppercase:
                print_values.append(used_variables[value] if value in used_variables else variables[value]) #if else in the same row!
            else:
                print_values.append(int(value))

        elif "MOV" in program[index]:
            variable, value = program[index].split()[1:] #it splits and stores only the indexs 1 and 2
            if value not in ascii_uppercase: #if value not a letter, updates as an integer in both lists (is stored in used_variable as is now defined)
                used_variables[variable] = int(value)
                variables[variable] = int(value)
            else: #if a letter
                if value in used_variables: #check origin (if it has been previously used or not) and assign new value
                    used_variables[variable] = used_variables[value]
                else:
                    variables[variable] = variables[value]

        elif "ADD" in program[index]:
            variable, value = program[index].split()[1:]
            if value not in ascii_uppercase:
                used_variables[variable] = used_variables[variable] + int(value) if variable in used_variables else int(value)
            else:
                used_variables[variable] = used_variables[variable] + used_variables[value] if variable in used_variables else used_variables[value]

        elif "SUB" in program[index]:
            variable, value = program[index].split()[1:]
            if value not in ascii_uppercase:
                used_variables[variable] = used_variables[variable] - int(value) if variable in used_variables else int(value)
            else:
                used_variables[variable] = used_variables[variable] - used_variables[value] if variable in used_variables else used_variables[value]


        elif "MUL" in program[index]:
            variable, value = program[index].split()[1:]
            if value not in ascii_uppercase:
                used_variables[variable] = used_variables[variable] * int(value) if variable in used_variables else int(value)
            else:
                used_variables[variable] = used_variables[variable] * used_variables[value] if variable in used_variables else used_variables[value]


        elif "JUMP" in program[index]:
            parts = program[index].split()
            location = parts[-1]
            if "IF" in program[index]:
                variable_1, operator, variable_2 = parts[1], parts[2], parts[3]
            
                variable_1 = int(variable_1) if variable_1 not in ascii_uppercase else used_variables[variable_1]
                variable_2 = int(variable_2) if variable_2 not in ascii_uppercase else used_variables[variable_2]
            
                operations = {"==": variable_1 == variable_2, "!=": variable_1 != variable_2, "<": variable_1 < variable_2, "<=": variable_1 <= variable_2, ">": variable_1 > variable_2, ">=": variable_1 >= variable_2}
                if operations[operator]:
                    index = -1
                    program = locations[location]
            else:
                index = -1
                program = locations[location]
        
        elif "END" in program[index]:
            break
        index +=1
    
    return print_values





if __name__=="__main__":
    program4 = ['MOV A 1', 'MOV B 999', 'start:', 'ADD A 1', 'SUB B 1', 'ADD C 1', 'IF A == B JUMP end', 'JUMP start', 'end:', 'PRINT C'] 
    result = run(program4)
    print(result)