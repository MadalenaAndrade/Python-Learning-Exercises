# write your solution here

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

full_names = {}
with open(student_info) as new_file:
    for line in new_file:
        line = line.replace("\n","")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        full_names[parts[0]]=parts[1]+" "+parts[2]

total_of_exercises = {}
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        sum = 0
        for exercises in parts[1:]:
            sum += int(exercises) 
        total_of_exercises[parts[0]]=sum

for id, name in full_names.items():
    print(f"{name} {total_of_exercises[id]}")


