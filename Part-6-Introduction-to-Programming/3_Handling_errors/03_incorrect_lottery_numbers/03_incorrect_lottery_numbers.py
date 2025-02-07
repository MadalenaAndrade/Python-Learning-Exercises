# Write your solution here
def filter_incorrect():
    
    weeks = {} #create dict from the file
    with open("lottery_numbers.csv") as file:
        for row in file:
            weeks_numbers = row.replace("\n","").split(";")
            numbers = weeks_numbers[1].split(",")
            weeks[weeks_numbers[0]] = numbers[:]
    
    #first error: incorrect week number
    valid_weeks = list(range(1, 53))
    bad_weeks = []
    for week in weeks:
        try:
            week_integer = int(week[4:]) #if not a number it appends right away
            if week_integer not in valid_weeks:
                bad_weeks.append(week)
        except ValueError:
            bad_weeks.append(week)
    
    for week in bad_weeks:
        weeks.pop(week) #take the bad weeks of the list
    
    #Check if it is numbers, and if it fall in the range
    valid_numbers = list(range(1,40))
    bad_weeks = []

    for week,values in weeks.items():
        for value in values:
            try:
                if int(value) not in valid_numbers:
                    bad_weeks.append(week)
                    break #stop checking the week
            except ValueError:
                bad_weeks.append(week)
                break
    
    for week in bad_weeks:
        weeks.pop(week) #take the bad weeks of the list
    
    #check if there are too few numbers
    bad_weeks = []
    for week,values in weeks.items():
        if len(values) != 7:
            bad_weeks.append(week)

    for week in bad_weeks:
        weeks.pop(week)

    #same number twice
    bad_weeks = []
    for week,values in weeks.items():
        for value in values:
            if values.count(value) > 1:
                bad_weeks.append(week)
                break
    
    for week in bad_weeks:
        weeks.pop(week)

    #create correct file
    with open("correct_numbers.csv","w") as new_file:
        for week, numbers in weeks.items():
            new_file.write(f"{week};{",".join(numbers)}\n")


