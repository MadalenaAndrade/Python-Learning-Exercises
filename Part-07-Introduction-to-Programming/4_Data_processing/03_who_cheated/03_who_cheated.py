# Write your solution here
from datetime import datetime, timedelta
import csv

def cheaters():
    students = {}
    with open("submissions.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            date = datetime.strptime(line[3], "%H:%M")
            if line[0] not in students:
                students[line[0]] = [date]
            else:
                students[line[0]].append(date)

    cheaters = []

    with open("start_times.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            date = datetime.strptime(line[1], "%H:%M")
            name = line[0]
            for student, hour_delivered in students.items():
                for hour in hour_delivered:
                    if name == student and date + timedelta(hours=3) < hour and name not in cheaters:
                        cheaters.append(name)
    
    return cheaters

