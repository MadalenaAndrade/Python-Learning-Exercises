# Write your solution here
#Print student information
def print_student(database:dict, name:str):
    if name not in database:
        print(f"{name}: no such person in the database")
    elif database[name]==[]:
        print(f"{name}:")
        print(" no completed courses")
    else:
        course_number = len(database[name]) #calculate how many items on list (aka courses)
        print(f"{name}:")
        print(f" {course_number} completed courses:")
        sum = 0
        for key,value in database.items():
            if key == name:
                for i in range(course_number): #goes to each item (course) in the items list
                    print(f"  {value[i][0]} {value[i][1]}")
                    sum += value[i][1]
        print(f" average grade {sum/course_number}")                

#Add student information
def add_student(database:dict, name:str):
    database[name]=[]

#Add course information
def add_course(database:dict, name:str, course_grade:tuple):
    
    new_grade = course_grade[1]
    new_course = course_grade[0]

    if new_grade == 0: #nothing happens
        return
    if database[name]==[]: #if name has no courses
            database[name].append(course_grade)
            return
    

    for i in range(len(database[name])):
        if new_course==database[name][i][0]: 
            if new_grade > database[name][i][1]: #update only if grade is higher
                database[name][i] = new_course, new_grade
            return
                
    database[name].append(course_grade) #everything else is added 

def summary(database:dict):
    #number of students
    number_of_students = len(database)
    #most courses completed
    most_courses = 0
    for name in database:
        if len(database[name]) > most_courses:
            most_courses = len(database[name])
            most_courses_name = name
    #best average grade
    max_average_grade = 0
    for name in database:
        number_of_courses = len(database[name]) 
        sum = 0
        for i in range(number_of_courses):
            sum += database[name][i][1]
        average = sum/number_of_courses
        if average>max_average_grade:
            max_average_grade = average
            max_average_name = name

    print(f"students {number_of_students}")
    print(f"most courses completed {most_courses} {most_courses_name}")
    print(f"best average grade {max_average_grade} {max_average_name}")

if __name__=="__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)

