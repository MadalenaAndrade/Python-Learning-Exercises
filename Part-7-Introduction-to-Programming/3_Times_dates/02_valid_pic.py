# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    validity = True
    #check the lenght
    if len(pic) > 11:
        validity = False

    #check century marker and create full year
    century_marker = pic[6]
    if century_marker == "+":
        year = int("18"+pic[4:6]) 
    elif century_marker == "-":
        year = int("19"+pic[4:6])
    elif century_marker == "A":
        year = int("20"+pic[4:6])
    else:
        validity = False

    #check birth date
    day = int(pic[0:2])
    month = int(pic[2:4])
    try:
        date = datetime(int(year), month, day)
    except:
        validity = False

    #check control character
    birth_and_id = int(pic[0:6]+pic[7:10])
    control_character = pic[10]
    string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    remainder = birth_and_id%31
    if string[remainder] != control_character:
        validity = False
    
    return validity
    

