# Write your solution here
from datetime import datetime, timedelta
import csv

def final_points():
    with open("start_times.csv") as start, open("submissions.csv") as submissions:
        #read start time and save name with the time
        start_times = {}
        for row in csv.reader(start, delimiter=";"):
            start_times[row[0]] = datetime.strptime(row[1], "%H:%M")
        
        students = {}

        #read and save info of submissions
        for row in csv.reader(submissions, delimiter=";"):
            name, task, points, time = row[0], row[1], int(row[2]), row[3]
            if datetime.strptime(time, "%H:%M") - start_times[name] < timedelta(hours=3):
                if name not in students:
                    students[name] = {}
                if task not in students[name]:
                    students[name][task] = [points]
                else:
                    students[name][task].append(points)
    
        total_points = {}
        for name, task_points in students.items():
            all_points = 0
            for task, points in task_points.items():
                max_point = max(points)
                all_points += max_point
            total_points[name]= all_points

    return total_points


