# Write your solution here
def new_person(name: str, age: int):

    if name == "":
        raise ValueError("name is an empty string")
    elif " " not in name:
        raise ValueError("name contains less than two words")
    elif len(name) > 40:
        raise ValueError("name is longer than 40 characters")
    elif age < 0:
        raise ValueError("age is a negative number")
    elif age > 150:
        raise ValueError("age is greater than 150")
    else:
        return (name, age)
        
