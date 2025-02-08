# tee ratkaisu tänne
if True:
    # this is never executed
    student_info = input('Student information: ')
    exercise_data = input('Exercises completed: ')
    exam_points = input('Exam points: ')
else:
    # hard-coded input
    student_info = 'students1.csv'
    exercise_data = 'exercises1.csv'
    exam_points = 'exam_points1.csv'

#converting exercises to points
def convert_points(number:int):
    points = number//4
    return points

#convert total points to grade
def grade(points:int):
    grade_limits = [15, 18, 21, 24, 28]
    grade = 0
    while grade < 5 and points >= grade_limits[grade]:
        grade += 1
    return grade

students = {}
with open(student_info) as file:
    for line in file:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        students[parts[0]]=parts[1]+" "+parts[2].strip()
    
exercises = {}
with open(exercise_data) as file:
    for line in file:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        sum = 0
        for number in parts[1:]:
            sum += int(number)
        exercises[parts[0]]=sum
      
exams = {}
with open(exam_points) as file:
    for line in file:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        exsum = 0
        for number in parts[1:]:
            exsum += int(number)
        exams[parts[0]]=exsum

print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
for id, name in students.items():
    exec_pts = convert_points(exercises[id])
    total = exec_pts+exams[id]
    print(f"{name:30}{exercises[id]:<10}{exec_pts:<10}{exams[id]:<10}{total:<10}{grade(total):<10}")

