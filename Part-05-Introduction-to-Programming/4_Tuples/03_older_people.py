# Write your solution here
def older_people(people: list, year: int):

    persons_born = []

    for person in people:
        if person[1]<year:
            persons_born.append(person[0])
    
    return persons_born


if __name__=="__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)
    print(older)