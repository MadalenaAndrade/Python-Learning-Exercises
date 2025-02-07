# tee ratkaisu tänne
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

def produce_txt(course_items: list, students: dict, exercises: dict, exams: dict):
    with open("results.txt","w") as txt_file:
        #headline
        headline = f"{course_items[0]}, {course_items[1]} credits"
        txt_file.write(headline+"\n")
        character_string = ""
        for character in range(len(headline)):
            character_string += "=" 
        txt_file.write(character_string+"\n")
        #sub_headlines
        headlines = f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}"
        txt_file.write(headlines+"\n")
        #body
        for id, info in students.items():
            exec_pts = convert_points(exercises[id])
            total = exec_pts+exams[id]
            line = f"{students[id]:30}{exercises[id]:<10}{exec_pts:<10}{exams[id]:<10}{total:<10}{grade(total):<10}"
            txt_file.write(line+"\n")

def produce_csv(students: dict, exercises: dict, exams: dict):
    with open("results.csv","w") as csv_file:
        for id, info in students.items():
            exec_pts = convert_points(exercises[id])
            total = exec_pts+exams[id]
            line = f"{id};{students[id]};{grade(total)}"
            csv_file.write(line+"\n")

#start_part 3
#putted inside a function
def transfer_to_dictionaries(student_info: str, exercise_data: str, exam_points: str):
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
    
    return [students, exercises, exams]
#end_part 3

def export_course_items(course_file: str):
    course_items = []
    
    with open(course_file) as new_file:
        for row in new_file:
            parts = row.replace("\n","").split(":")
            course_items.append(parts[1].lstrip())

    return course_items

def create_results():
    students = input("Student information:")
    exercises_completed = input("Exercises completed:")
    exam_points = input("Exam points:")
    courses = input("Course information:")

    course_items = export_course_items(courses)
    all_info_dictionary = transfer_to_dictionaries(students, exercises_completed, exam_points)
    students_dict = all_info_dictionary[0]
    exercises_dict = all_info_dictionary[1]
    exam_points_dict = all_info_dictionary[2]

    produce_txt(course_items, students_dict, exercises_dict, exam_points_dict)
    produce_csv(students_dict, exercises_dict, exam_points_dict)
    print("Results written to files results.txt and results.csv")
    
create_results()