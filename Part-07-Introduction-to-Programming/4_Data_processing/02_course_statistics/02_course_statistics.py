# Write your solution here
import urllib.request
import json
from math import floor

def transform_url_data(url: str):
    request = urllib.request.urlopen(url)
    data = request.read()
    all_data = json.loads(data)
    return all_data

def retrieve_all():
    all_data = transform_url_data("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    courses = []
    
    for course in all_data:
        if course["enabled"]:
            courses.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))
        else:
            continue
    return courses

def retrieve_course(course_name: str):
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    all_data = transform_url_data(url)

    weeks = 0
    students = []
    hour_total = []
    exercise_total = []
    for week in all_data:
        weeks += 1
        students.append(all_data[week]["students"])
        hour_total.append(all_data[week]["hour_total"])
        exercise_total.append(all_data[week]["exercise_total"])
    
    course_info = {}
    course_info["weeks"] = weeks
    course_info["students"] = max(students)
    course_info["hours"] = sum(hour_total)
    course_info["hours_average"] = floor(sum(hour_total)/max(students))
    course_info["exercises"] = sum(exercise_total)
    course_info["exercises_average"] = floor(sum(exercise_total)/max(students))

    return course_info
