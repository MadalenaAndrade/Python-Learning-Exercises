# wwite your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"

full_names = {}
with open(student_info) as new_file:
    for line in new_file:
        line = line.replace("\n","")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        full_names[parts[0]]=parts[1]+" "+parts[2]

#sum all exercises and convert to points
total_exercise_points = {}
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        sum = 0
        for exercises in parts[1:]:
            sum += int(exercises) 
        #convert to exercise points:
        newsum = 0
        for i in range(10, 0, -1):
            if sum < 40*(i/10):
                newsum = i-1
            elif sum == 40:
                newsum = 10
        total_exercise_points[parts[0]]=newsum

#sum exam points
total_exam_points = {}
with open(exam_points) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        sum = 0
        for point in parts[1:]:
            sum += int(point)
        total_exam_points[parts[0]]=sum

#calculate grades
for id,name in full_names.items():
    total_points = total_exercise_points[id]+total_exam_points[id]
    if 0 < total_points < 15:
        print(f"{name} 0")
    elif total_points < 18:
        print(f"{name} 1")
    elif total_points < 21:
        print(f"{name} 2")
    elif total_points < 24:
        print(f"{name} 3")
    elif total_points < 28:
        print(f"{name} 4")
    else:
        print(f"{name} 5")

