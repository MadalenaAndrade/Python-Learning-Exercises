# Write your solution here
from datetime import datetime, timedelta
filename = input("Filename: ")
start_date = input("Starting date: ")
start_date = datetime.strptime(start_date, "%d.%m.%Y")
time_passed = int(input("How many days? "))

print("Please type in screen time in minutes on each day (TV computer mobile):")

dates = {}
for day in range(time_passed):
    day_passed = start_date + timedelta(days = day)
    date = input(f"Screen time {day_passed.strftime("%d.%m.%Y")}: ")
    dates[day_passed.strftime("%d.%m.%Y")] = date

total_minutes = 0
for key, value in dates.items():
    values=value.split(" ")
    for number in values:
        total_minutes += int(number)
    
with open(filename, "w") as new_file:
    new_file.write(f"Time period: {start_date.strftime("%d.%m.%Y")}-{day_passed.strftime("%d.%m.%Y")}\n")
    new_file.write(f"Total minutes: {total_minutes}\n")
    new_file.write(f"Average minutes: {total_minutes/time_passed}\n")
    for key, value in dates.items():
        new_file.write(f"{key}: {value.replace(" ", "/")}\n")

print(f"Data stored in file {filename}")










