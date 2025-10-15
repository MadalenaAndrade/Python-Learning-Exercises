class Course:
    def __init__(self, name: str):
        self.__name = name
        self.__grade = None
        self.__credits = None

    def name(self):
        return self.__name
    
    def grade(self):
        return self.__grade
    
    def add_grade(self, grade: int):
        if not self.__grade or (self.__grade and grade > self.__grade):
            self.__grade = grade
       
    def credits(self):
        return self.__credits
    
    def add_credits(self, credits: int):
        self.__credits = credits

class CourseRecords:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.__courses:
            self.__courses[name] = Course(name)
        
        self.__courses[name].add_grade(grade)
        self.__courses[name].add_credits(credits)

    def get_entry(self, name: str):
        if name not in self.__courses:
            return None
        return (self.__courses[name].grade(), self.__courses[name].credits())

    def create_statistic(self):
        completed_courses = 0
        credits = 0
        grades = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
        total_grades = 0
        mean = 0

        for course in self.__courses.values():
            completed_courses += 1
            credits += course.credits()
            grade = course.grade()
            total_grades += grade
            grades[grade] += 1
        
        if completed_courses:
            mean = total_grades/completed_courses

        return {"courses": completed_courses, "credits": credits, "mean": mean, "grades": grades}

class CourseRecordsApp:
    def __init__(self):
        self.__course_records = CourseRecords()

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))

        self.__course_records.add_course(name, grade, credits)

    def get_course_data(self):
        name = input("course: ")
        data = self.__course_records.get_entry(name)
        
        if not data:
            print("no entry for this course")
        else:
            grade, credits = data 
            print(f"{name} ({credits} cr) grade {grade}")

    def get_statistics(self):
        data = self.__course_records.create_statistic()

        print(f"{data["courses"]} completed courses, a total of {data["credits"]} credits")
        print(f"mean {data["mean"]:.1f}")
        print("grade distribution")
        print(f"5: {"x"*data["grades"][5]}")
        print(f"4: {"x"*data["grades"][4]}")
        print(f"3: {"x"*data["grades"][3]}")
        print(f"2: {"x"*data["grades"][2]}")
        print(f"1: {"x"*data["grades"][1]}")

    def run(self):
        while True:
            print("")
            command = input("command: ")

            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.get_statistics()

print("1 add course")
print("2 get course data")
print("3 statistics")
print("0 exit")

app = CourseRecordsApp()
app.run()