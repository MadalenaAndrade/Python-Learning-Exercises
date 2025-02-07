# Write your solution here
resultslist = []
while True:
    results = input("Exam points and exercises completed:")
    if results == "":
        break
    resultslist += results.split() #list with all exam points and number of exercises 

newresultslist = [] #convert to integers
for number in resultslist:
    newresultslist.append(int(number))

#separate exam points and exercises numbers
exam_points = newresultslist[0::2] 
exercises_numbers = newresultslist[1::2]

#convert percentage of exercises to points
exercises_points = []
for number in exercises_numbers:
    exercises_points.append(number//10)

#calculate grade for each item of the lists
grades = []
totalpoints = [] #to calculate average after
index = 0

while index < len(exam_points):
    each_total_points = exam_points[index]+exercises_points[index]
    totalpoints.append(each_total_points)
    if exam_points[index] < 10:
        grades.append(0)
    elif 15 <= each_total_points <= 17:
        grades.append(1)
    elif 18 <= each_total_points <= 20:
        grades.append(2)
    elif 21 <= each_total_points <= 23:
        grades.append(3)
    elif 24 <= each_total_points <= 27:
        grades.append(4)
    elif 28 <= each_total_points <= 30:
        grades.append(5)
    else:
        grades.append(0)
    index += 1

#To calculate pass percentage
converted_list = []
for number in grades:
    if number < 1:
        converted_list.append(0)
    else:
        converted_list.append(1)

percentage = 100/len(exam_points)*sum(converted_list)

#printing program
print("Statistics:")
print(f"Points average: {sum(totalpoints)/len(totalpoints):.1f}")
print(f"Pass percentage: {percentage:.1f}")
print("Grade distribution:")

#grade distribution
#calculate the number of equal grades
five=[]
four=[]
three=[]
two=[]
one=[]
zero=[]
for grade in grades:
    if grade == 5:
        five.append(1)
    elif grade == 4:
        four.append(1)
    elif grade == 3:
        three.append(1)
    elif grade == 2:
        two.append(1)
    elif grade == 1:
        one.append(1)
    else:
        zero.append(1)

print(f"5: {"*"*sum(five)}")
print(f"4: {"*"*sum(four)}")
print(f"3: {"*"*sum(three)}")
print(f"2: {"*"*sum(two)}")
print(f"1: {"*"*sum(one)}")
print(f"0: {"*"*sum(zero)}")



