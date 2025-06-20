# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):
        self.persons = []
    
    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return True if not self.persons else False
    
    def print_contents(self):
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {sum(person.height for person in self.persons)} cm")
        for person in self.persons:
            print(person)

    def shortest(self):
        if self.is_empty():
            return None
        
        min_height_person = self.persons[0]
        for person in self.persons:
            if person.height < min_height_person.height:
                min_height_person = person
        
        return min_height_person
    
    def remove_shortest(self):
        if self.is_empty():
            return None
        
        person_index = self.persons.index(self.shortest())
        removed_person = self.persons.pop(person_index)
        return removed_person

if __name__=="__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
